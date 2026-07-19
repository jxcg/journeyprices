from transport_modalities.JourneyModality import JourneyModality


class TrainJourney(JourneyModality):
    """
    A journey by train. Cost is the ticket price, unlike car cost, there's
    no formula to derive it from distance, so it must be supplied (e.g. from
    a fares lookup, once that integration exists).
    """

    def __init__(self, distance_miles: float, duration_minutes: float, ticket_price: float):
        super().__init__(transport_mode="train", distance_miles=distance_miles, duration_minutes=duration_minutes)
        self.ticket_price = ticket_price

    def calculate_cost(self) -> float:
        return self.ticket_price
