"""Create simulation-relevant classes"""
import matplotlib.pyplot as plt


class PortStaff:
    def __init__(self, location, role):
        self.location = location # (x, y)
        self.role = role  # string


class ControlCenter(PortStaff):
    def __init__(self, location, role, ship_queue):
        super().__init__(location, role)
        self.ship_queue = ship_queue  # number of ships they can manage at once

    def update_stacks(self, ship_queue):
        self.ship_queue = ship_queue
