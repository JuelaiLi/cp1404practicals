
numbers = [3, 1, 4, 1, 5, 9, 2]


print(numbers[0])       # Should be 3
print(numbers[-1])      # Should be 2
print(numbers[3])       # Should be 1
print(numbers[:-1])     # Should be [3, 1, 4, 1, 5, 9]
print(numbers[3:4])     # Should be [1]
print(5 in numbers)     # Should be True
print(7 in numbers)     # Should be False
print("3" in numbers)   # Should be False
print(numbers + [6, 5, 3])  # Should be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


numbers[0] = "ten"      # Change the first element to "ten"
numbers[-1] = 1         # Change the last element to 1


print(numbers[2:])      # Print all elements except the first two
print(9 in numbers)     # Print whether 9 is an element of numbers
