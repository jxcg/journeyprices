from flask import Flask, render_template, request

from transport_modalities.CarJourney import CarJourney
from transport_modalities.Journey import Journey
from transport_modalities.TrainJourney import TrainJourney

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare() -> str:
    journey = Journey(
        origin=request.form["origin"],
        destination=request.form["destination"],
    )

    journey.add_option(
        CarJourney(
            distance_miles=float(request.form["car_distance_miles"]),
            duration_minutes=float(request.form["car_duration_minutes"]),
            car_mpg=float(request.form["car_mpg"]),
            pennies_per_litre=float(request.form["pennies_per_litre"]),
        )
    )
    journey.add_option(
        TrainJourney(
            duration_minutes=float(request.form["train_duration_minutes"]),
            ticket_price=float(request.form["train_ticket_price"]),
        )
    )

    return render_template(
        "results.html",
        journey=journey,
        cheapest=journey.cheapest_option(),
        fastest=journey.fastest_option(),
    )


if __name__ == "__main__":
    app.run(debug=True)
