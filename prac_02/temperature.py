def celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit - 32) * 5/9

def main():
    celsius_temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is {fahrenheit_temperature:.2f} degrees Fahrenheit.")

    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} degrees Fahrenheit is {celsius_temperature:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()
