from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car only if a random number between 0 and 100 is less than the car's reliability.
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
