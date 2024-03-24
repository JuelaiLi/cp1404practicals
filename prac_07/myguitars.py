from guitar import Guitar, read_guitars_from_file, write_guitars_to_file


def main():
    guitars = read_guitars_from_file('guitars.csv')

    print("Existing guitars:")
    display_guitars(guitars)

    while True:
        print("\nEnter details for a new guitar (or type 'done' to finish):")
        name = input("Name: ")
        if name.lower() == 'done':
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    write_guitars_to_file(guitars, 'guitars.csv')

    print("\nAll guitars (existing and new):")
    display_guitars(guitars)


def display_guitars(guitars):
    """Display guitars in the list"""
    for guitar in guitars:
        print(guitar)


main()
