import json
import uuid
import logging
from machine import Machine
from infra_simulator import InfrastructureProvisioner

logging.basicConfig(
    filename="logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Logging system started")

OS_OPTIONS = ["ubuntu", "centos"]
AVAL_CPUS = [1, 2, 4, 8, 16]
AVAL_RAM = [2, 4, 8, 16, 32, 64]


def get_valid_input(message, validator, *args):
    while True:
        value = input(message).strip().lower()
        try:
            validator(value, *args)
            return value
        except Exception as error:
            print(error)


def get_user_input():
    machines = []

    while True:
        while True:
            name = input("Enter machine name (or 'done' to finish): ").strip().lower()
            if name == "done":
                write_to_file("configs/instances.json", machines)
                return machines
            try:
                validate_vm_name(name)
                validate_unique_machine_name( name,machines,"configs/instances.json")
                break
            except Exception as error:
                print(error)


        os = get_valid_input("Enter OS (Ubuntu/CentOS): ",validate_vm_os )
        cpu = get_valid_input(f"Enter CPU (e.g., 2vCPU): Minimum - {min(AVAL_CPUS)}vCPU Maximum - {max(AVAL_CPUS)}vCPU: ",validate_vm_resource,"vcpu",AVAL_CPUS,"CPU")
        ram = get_valid_input(f"Enter RAM (e.g., 4GB): Minimum - {min(AVAL_RAM)}GB Maximum - {max(AVAL_RAM)}GB: ",validate_vm_resource,"gb",AVAL_RAM,"RAM" )
        machine_id = str(uuid.uuid4())
        machine = Machine(machine_id, name, os, cpu, ram)
        machines.append(machine.to_dict())
        write_to_file("configs/instances.json", machines)
        provisioner = InfrastructureProvisioner(machine)
        provisioner.provision()
        return machines


def validate_instance_input(instance_data):
    validate_vm_name(instance_data["name"])
    validate_vm_os(instance_data["os"])

    validate_vm_resource( instance_data["cpu"],"vcpu",AVAL_CPUS,"CPU")
    validate_vm_resource(instance_data["ram"],"gb",AVAL_RAM,"RAM" )


def validate_vm_name(name):
    if not name:
         raise Exception("VM name cannot be empty")

    if len(name) > 10:
        raise Exception("VM name should be up to 10 letters")


def validate_unique_machine_name(name, machines, filename):
    for machine in machines:
        if machine["name"] == name:
            raise Exception("Machine name already exists in current session")

    try:
        with open(filename, "r") as file:
            json_data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        json_data = {"machines": []}

    for machine in json_data["machines"]:
        if machine["name"] == name:
            raise Exception("Machine name already exists in file")


def validate_vm_os(os):
    if not os:
        raise Exception("OS cannot be empty")
    if os not in OS_OPTIONS:
        raise Exception("OS must be ubuntu or centos")


def validate_vm_resource(value, unit, available_values, resource_name):
    data = value.split(unit)

    if len(data) != 2:
        raise Exception(f"{resource_name} should be in {unit}")

    try:
        number = int(data[0])
    except ValueError:
        raise Exception(f"{resource_name} value has to be a number")

    if number <= 0:
        raise Exception(f"{resource_name} number must be greater than 0")

    if number not in available_values:
        raise Exception(f"{resource_name} is not in the available list")


def write_to_file(filename, machines):
    try:
        with open(filename, "r") as file:
            json_data = json.load(file)
            if "machines" not in json_data:
                json_data["machines"] = []

    except (FileNotFoundError, json.JSONDecodeError):
        json_data = {
            "machines": []
        }

    json_data["machines"].extend(machines)

    with open(filename, "w") as file:
        json.dump(json_data, file, indent=4)

def main():
    machines = get_user_input()
    print(machines)


if __name__ == "__main__":
    main()