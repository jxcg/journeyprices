from transport_modalities.JourneyModality import JourneyModality
from transport_modalities.units import LITRES_PER_UK_GALLON

class CarJourney(JourneyModality):
    """
    A journey by car. Cost is derived from fuel consumed: distance covered,
    how efficient the car is (mpg), and the local price of fuel.

    car_mpg and pennies_per_litre are required for now; looking these up
    automatically from a number plate or postcode is a future feature (see
    PLAN.md), not implemented yet.

    Ideally would like to supply Postcode A to Postcode B, then distance-miles and minutes will be supplied from ANOTHER engine.

    """

    def __init__(
        self,
        distance_miles: float,
        duration_minutes: float,
        car_mpg: float,
        pennies_per_litre: float,
    ):
        super().__init__(transport_mode="car", distance_miles=distance_miles, duration_minutes=duration_minutes)
        self.car_mpg = car_mpg
        self.pennies_per_litre = pennies_per_litre

    def calculate_cost(self) -> float:
        gallons_used = self.distance_miles / self.car_mpg
        litres_used = gallons_used * LITRES_PER_UK_GALLON
        cost_in_pence = litres_used * self.pennies_per_litre
        return cost_in_pence / 100
