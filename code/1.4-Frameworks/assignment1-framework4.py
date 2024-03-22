"""Create simulation-relevant classes"""
import matplotlib.pyplot as plt


class LoadedCargo:
    def __init__(self, weight, ship_tag):
        self.weight = weight  # Float value
        self.ship_tag = ship_tag  # string


class DryCargo(LoadedCargo):
    def __init__(self, weight, ship_tag, product_type):
        super().__init__(weight, ship_tag)
        self.product_type = product_type  # contents of the cargo

    def update_product_type(self, product_type):
        self.product_type = product_type


class LiquidCargo(LoadedCargo):
    def __init__(self, weight, ship_tag, hazardous):
        super().__init__(weight, ship_tag)
        self.hazardous = hazardous  # whether special care needs to be taken to transport (oil, chemicals)

    def update_hazardous(self, hazardous):
        self.hazardous = hazardous
