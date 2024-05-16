from enum import Enum

class DER:
    """
    Represents a Distributed Energy Resource (DER) in the VPP.
    """
    def __init__(self, name, type, capacity, cost):
        self.name = name
        self.type = type  # Type of DER power generation
        self.capacity = capacity  # Maximum power generation/consumption
        self.cost = cost  # Cost of power generation/consumption


class DERType(Enum):
    SOLAR = 1
    WIND = 2
    HYDRO = 3
    GEO = 4
    BIO = 5
    FUEL = 6
    NAT_GAS = 7
