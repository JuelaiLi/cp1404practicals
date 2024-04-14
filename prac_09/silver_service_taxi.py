from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """Calculate the fare, adding the flag fall to the Taxi fare."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of this SilverServiceTaxi."""
        return f"{super().__str__()} plus flag fall of ${self.flagfall:.2f}"
