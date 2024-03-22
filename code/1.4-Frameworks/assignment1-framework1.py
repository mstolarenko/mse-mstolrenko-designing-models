"""Create simulation-relevant classes"""
import matplotlib.pyplot as plt


class TransMachinery:
    def __init__(self, top_down_coordinates, human_users):
        self.top_down_coordinates = top_down_coordinates # (x, y)
        self.human_users = human_users  # 0 == autonomous


class ContainerCrane(TransMachinery):
    def __init__(self, top_down_coordinates, human_users, stacks):
        super().__init__(top_down_coordinates, human_users)
        self.stacks = stacks # number of containers on top of each other

    def update_stacks(self, stacks):
        self.stacks = stacks
