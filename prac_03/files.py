# Section 1: Writing user's name to "name.txt"
user_name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(user_name)

# Section 2: Reading and printing the name from "name.txt"
with open('name.txt', 'r') as file:
    stored_name = file.read()
    print(f"Your name is {stored_name}")

# Section 3: Reading and adding the first two numbers from "numbers.txt"
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    result = number1 + number2
    print(f"The sum of the first two numbers is: {result}")

# Section 4: Reading and summing all numbers from "numbers.txt"
total_sum = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total_sum += int(line)

print(f"The total sum of all numbers is: {total_sum}")
