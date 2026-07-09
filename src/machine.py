import logging


class Machine:
    def __init__(self, machine_id, name, os, cpu, ram):
        self.machine_id = machine_id
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

        logging.info(f"Machine created: {self.name}")

    def to_dict(self):
        return {
            "id": self.machine_id,
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }