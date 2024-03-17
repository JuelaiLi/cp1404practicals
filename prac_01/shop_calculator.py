total_price = 0
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))
for i in range(num_items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid number of price!")
        price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {num_items} items is ${total_price:.2f}")
