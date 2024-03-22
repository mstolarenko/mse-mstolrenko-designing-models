"""Create simulation-relevant classes"""
import matplotlib.pyplot as plt


class LandTerminal:
    def __init__(self, open_ports, closed_ports):
        self.open_ports = open_ports  # Integer
        self.closed_ports = closed_ports  # Integer


class UnloadedCargo(LandTerminal):
    def __init__(self, open_ports, closed_ports, empty_containers):
        super().__init__(open_ports, closed_ports)
        self.empty_containers = empty_containers  # number of empty containers awaiting transfer, integer

    def update_empty_containers(self, empty_containers):
        self.empty_containers = empty_containers
