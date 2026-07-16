import subprocess
import logging
from constants import LOGGER_NAME


logger = logging.getLogger(LOGGER_NAME)


class InfrastructureProvisioner:
    def __init__(self, machine):
        self.machine = machine

    def create_vm(self):
        logger.info(f"Creating virtual machine: {self.machine.name}")

    def install_os(self):
        logger.info(f"Installing operating system: {self.machine.os}")

    def configure_resources(self):
        logger.info(f"Configuring CPU: {self.machine.cpu}")
        logger.info(f"Configuring RAM: {self.machine.ram}")

    def configure_network(self):
        logger.info(f"Configuring network settings for {self.machine.name}...")

    def finish(self):
        logger.info(f"Provisioning completed successfully for Machine - {self.machine.name}.")

    def provision(self):
        logger.info("\nStarting infrastructure provisioning...")
        self.create_vm()
        self.install_os()
        self.configure_resources()
        self.configure_network()
        self.run_install_script()
        self.finish()

    def run_install_script(self):
        logger.info(f"Running installation script for Machine - {self.machine.name}...")
        logger.info("Running installation script")
        try:
            subprocess.run(["sh", "scripts/install_nginx.sh"], check=True)
            logger.info("Installation script completed successfully")
        except subprocess.CalledProcessError as e:
            logger.warning(f"Script failed with return code {e.returncode}, output: {e.output}")