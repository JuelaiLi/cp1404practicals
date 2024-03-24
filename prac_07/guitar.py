
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Format of the Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar"""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Check vintage"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Comparison based on year"""
        return self.year < other.year


def read_guitars_from_file(file_name):
    """Read guitars from the file and return a list of Guitar objects"""
    guitars = []
    with open(file_name, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def write_guitars_to_file(guitars, file_name):
    """Record information of guitar"""
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
