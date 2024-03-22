"""Create simulation-relevant classes"""
import matplotlib.pyplot as plt


class ShipStaff:
    def __init__(self, rank, work_site):
        self.rank = rank # string
        self.work_site = work_site  # (x, y), string


class UpperDeck(ShipStaff):
    def __init__(self, rank, work_site, response_times):
        super().__init__(rank, work_site)
        self.response_times = response_times # float value in minutes for how quickly they can react to events

    def update_response_times(self, response_times):
        self.response_times = response_times


class LowerDeck(ShipStaff):
    def __init__(self, rank, work_site, expertise):
        super().__init__(rank, work_site)
        self.expertise = expertise  # how many years of hands on experience do they have as engineers

    def update_expertise(self, expertise):
        self.expertise = expertise


"""Prepare for Simulation"""
