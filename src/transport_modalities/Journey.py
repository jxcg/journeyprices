from datetime import date

from transport_modalities.JourneyModality import JourneyModality


class Journey:
    """
    A single trip: a fixed location_start and location_end, with one or more
    JourneyModality options attached (e.g. a CarJourney and a TrainJourney)
    for a recommendation engine to compare later.
    """

    def __init__(
        self, location_start: str, location_end: str, created_date: date | None = None
    ):
        self.location_start = location_start
        self.location_end = location_end
        self.created_date = created_date or date.today()
        self.options: list[JourneyModality] = []

    def add_option(self, option: JourneyModality) -> None:
        self.options.append(option)

    def cheapest_option(self) -> JourneyModality:
        return min(self.options, key=lambda option: option.calculate_cost())

    def fastest_option(self) -> JourneyModality:
        return min(self.options, key=lambda option: option.duration_minutes)
