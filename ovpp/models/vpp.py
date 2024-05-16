class VPP:
    """
    Represents the Virtual Power Plant managing a collection of DERs.
    """
    def __init__(self, ders):
        self.ders = ders

    def dispatch(self):
        """
        Simulates dispatching power based on target and DER capacities.
        """
        dispatched_power = 0
        for der in self.ders:
            available_power = der.capacity - dispatched_power
            power_to_dispatch = min(available_power, target_power)
            dispatched_power += power_to_dispatch
            print(f"{der.name} dispatched: {power_to_dispatch:.2f}")
        return dispatched_power
