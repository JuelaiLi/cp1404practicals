"""
Hexadecimal Colour Codes Lookup
Estimate: 15 minutes
Actual:   12 minutes
"""

# Dictionary of colour names and their hexadecimal codes
COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff",
    "BlueViolet": "#8a2be2",
}
def main():
    """Main function to run the colour code lookup program."""
    print("Colour Code Lookup")
    while True:
        colour_name = input("Enter a colour name (or enter to quit): ")
        if colour_name == "":
            break
        colour_code = lookup_colour(colour_name)
        print(colour_code)

def lookup_colour(colour_name):
    """Look up the hexadecimal code for the given colour name."""
    # Convert the colour name to match the case used in the dictionary
    colour_name = colour_name.title()
    try:
        return COLOUR_CODES[colour_name]
    except KeyError:
        return "Invalid colour name"


if __name__ == "__main__":
    main()
