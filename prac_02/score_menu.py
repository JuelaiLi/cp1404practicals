import random

def get_result(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):

    print("*" * int(score))

def get_valid_score():

    while True:
        try:
            score = float(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Score Program!")

    user_score = get_valid_score()

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            user_result = get_result(user_score)
            print(f"Result: {user_result}")
        elif choice == "S":
            show_stars(user_score)
        elif choice == "Q":
            print("Thank you for using the Score Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
