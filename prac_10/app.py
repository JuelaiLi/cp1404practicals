from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32


@app.route('/celsius_to_fahrenheit/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"The temperature {celsius} Celsius is {fahrenheit:.2f} Fahrenheit."
    except ValueError:
        return "Invalid input. Please enter a valid Celsius temperature."


if __name__ == '__main__':
    app.run(debug=True)
