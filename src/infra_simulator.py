import subprocess

class InfrastructureProvisioner:
    def __init__(self, machine):
        self.machine = machine

    def create_vm(self):
        print(f"Creating virtual machine: {self.machine.name}")

    def install_os(self):
        print(f"Installing operating system: {self.machine.os}")

    def configure_resources(self):
        print(f"Configuring CPU: {self.machine.cpu}")
        print(f"Configuring RAM: {self.machine.ram}")

    def configure_network(self):
        print("Configuring network settings...")

    def finish(self):
        print("Provisioning completed successfully.")

    def provision(self):
        print("\nStarting infrastructure provisioning...")
        self.create_vm()
        self.install_os()
        self.configure_resources()
        self.configure_network()
        self.run_install_script()
        self.finish()

    def run_install_script(self):
        print("Running installation script...")
        subprocess.run(["bash", "scripts/install.sh"],check=True )
        print("Installation script completed successfully.")