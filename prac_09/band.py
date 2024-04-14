class Band:
    """Band class for maintaining a list of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band with its musicians and their instruments."""
        musician_strings = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each Musician in the band playing their instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)
