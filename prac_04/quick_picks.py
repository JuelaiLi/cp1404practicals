import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    quick_picks_count = int(input("How many quick picks? "))
    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)

def generate_quick_pick():
    """Generate a single quick pick of unique, sorted numbers."""
    quick_pick = set()
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.add(number)
    return sorted(quick_pick)

def print_quick_pick(quick_pick):
    """Print a single quick pick, formatted with numbers aligned."""
    for number in quick_pick:
        print(f"{number:2}", end=' ')
    print()

if __name__ == "__main__":
    main()
