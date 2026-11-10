from abc import ABC, abstractmethod


class JourneyModality(ABC):
    """
    Base class for a single way of making a journey (e.g. by car, by train).

    Holds the fields every transport mode needs to be compared on: how long,
    how much, and how convenient. Each mode calculates cost differently, so
    calculate_cost() is left abstract - subclasses must provide their own
    pricing logic.

    distance_miles is optional here: it drives cost for car (fuel used
    scales with distance), but not for train, where the ticket price is
    entered directly rather than derived.
    """

    def __init__(
        self,
        transport_mode: str,
        duration_minutes: float,
        distance_miles: float | None = None,
    ):
        self.transport_mode = transport_mode
        self.duration_minutes = duration_minutes
        self.distance_miles = distance_miles
        self.convenience_score: float | None = None

    @abstractmethod
    def calculate_cost(self) -> float:
        """Return the monetary cost of this journey option, in pounds."""
        raise NotImplementedError
