import random

# Line 1
print(random.randint(5, 20))  # Random integer between 5 and 20
# On line 1, you would see a random integer between 5 and 20 (inclusive).
# The smallest number you could have seen is 5, and the largest is 20.

# Line 2
print(random.randrange(3, 10, 2))  # Random odd number between 3 and 9
# On line 2, you would see a random odd number between 3 and 9 (inclusive).
# The smallest number you could have seen is 3, and the largest is 9.
# No, line 2 could not have produced a 4, as the step is 2 (producing only odd numbers).

# Line 3
print(random.uniform(2.5, 5.5))  # Random float between 2.5 and 5.5
# On line 3, you would see a random floating-point number between 2.5 and 5.5.
# The smallest number you could have seen is 2.5, and the largest is 5.5.

# Additional code
random_number = random.randint(1, 100)  # Random integer between 1 and 100 (inclusive)
print(random_number)
