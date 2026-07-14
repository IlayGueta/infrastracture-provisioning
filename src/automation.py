import json
import logging

from machine import Machine
from infra_simulator import InfrastructureProvisioner
from constants import AVAL_CPUS, AVAL_RAM, DEFAULT_CONFIG_PATH, OS_OPTIONS, LOG_FILENAME, LOGGER_NAME, LOG_DIR
from exceptions import VMNameError


logger = logging.getLogger(LOGGER_NAME)


class InfraAutomation:
    def __init__(self, config_path=DEFAULT_CONFIG_PATH):
        self.config_path = config_path

    @staticmethod
    def initialize_logger():
        logging.basicConfig(
            filename=LOG_DIR + LOG_FILENAME,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def read_config_file(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)

            if not isinstance(json_data, dict):
                json_data = {"machines": []}

            if "machines" not in json_data:
                json_data["machines"] = []

            return json_data

        except (FileNotFoundError, json.JSONDecodeError):
            return {"machines": []}

    def write_to_config_file(self, machine_data):
        json_data = self.read_config_file()
        json_data["machines"].append(machine_data)

        with open(self.config_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)

    def validate_name_machine(self, name):
        machines = self.read_config_file()
        for machine in machines["machines"]:
            if machine["name"] == name:
                logger.error(f"Machine {name} already exists")
                raise VMNameError("Machine name already exists")

    def get_user_input(self):
        created_machines = []

        while True:
            name = input("Enter machine name (or 'done' to finish): ").strip().lower()
            self.validate_name_machine(name)
            if name == "done":
                break

            os_name = input(f"Enter OS {OS_OPTIONS}: ").strip().lower()
            cpu = input(f"Enter CPU (e.g., 2vCPU): Available resources {AVAL_CPUS} vCPUs : ").strip().lower()
            ram = input(f"Enter RAM (e.g., 4GB): Available resources in GB {AVAL_RAM} : ").strip().lower()

            machine = Machine(name=name, os=os_name, cpu=cpu, ram=ram)
            machine_data = machine.to_dict()

            created_machines.append(machine_data)
            self.write_to_config_file(machine_data)

            provisioner = InfrastructureProvisioner(machine)
            provisioner.provision()

        return created_machines

    def run(self):
        self.initialize_logger()
        created_machines = self.get_user_input()
        print("Created machines:", created_machines)



def main():
    print("Welcome to Infra Automation!")
    infra_automation = InfraAutomation(config_path=DEFAULT_CONFIG_PATH)
    infra_automation.run()


if __name__ == "__main__":
    main()
