import random

# CONSTANTS
STARTING_PRICE = 10.00
MAX_DAYS = 425
PRICE_RANGE = (1, 100)
MAX_INCREASE = 17.5
OUTPUT_FILE = "stock_simulation_output.txt"

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

# Initialize variables
current_price = STARTING_PRICE

# Print starting price to the console and write it to the file
print(f"Starting price: ${current_price:,.2f}")
print(f"Starting price: ${current_price:,.2f}", file=out_file)

# Simulate stock prices for each day
for day in range(1, MAX_DAYS + 1):
    price_increase = current_price * (random.uniform(0, MAX_INCREASE) / 100)
    price_direction = random.choice([-1, 1])
    current_price += price_increase * price_direction

    # Ensure the price stays within the defined range
    current_price = max(min(current_price, PRICE_RANGE[1]), PRICE_RANGE[0])

    # Print the simulated price to the console and write it to the file
    print(f"On day {day} price is: ${current_price:,.2f}")
    print(f"On day {day} price is: ${current_price:,.2f}", file=out_file)

# Close the file
out_file.close()
