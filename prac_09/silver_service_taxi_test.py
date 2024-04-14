from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi('Hummer', 200, 2)

silver_taxi.drive(18)

assert silver_taxi.get_fare() == 48.78

print(silver_taxi)
