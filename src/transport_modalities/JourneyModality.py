from abc import ABC, abstractmethod


class JourneyModality(ABC):
    """
    Base class for a single way of making a journey (e.g. by car, by train).

    Holds the fields every transport mode needs to be compared on: how far,
    how long, how much, and how convenient. Each mode calculates cost
    differently, so calculate_cost() is left abstract - subclasses must
    provide their own pricing logic.
    """

    def __init__(self, transport_mode: str, distance_miles: float, duration_minutes: float):
        self.transport_mode = transport_mode
        self.distance_miles = distance_miles
        self.duration_minutes = duration_minutes
        self.convenience_score: float | None = None

    @abstractmethod
    def calculate_cost(self) -> float:
        """Return the monetary cost of this journey option, in pounds."""
        raise NotImplementedError