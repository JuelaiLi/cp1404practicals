from unreliable_car import UnreliableCar

test_car = UnreliableCar('Test Car', 100, 50)

distance_driven = test_car.drive(40)
print(f"Attempted to drive 40km, drove {distance_driven}km")
