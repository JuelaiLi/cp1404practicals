def main():
    name = input("Enter name: ")
    display_menu()
    choice = input(">>> ").upper()
    while choice != 'Q':
        determine_choice(choice, name)
        display_menu()
        choice = input(">>> ").upper()
    print("Finished.")


def display_menu():
    print("(H)ello\n(G)oodbye\n(Q)uit")


def determine_choice(choice, name):
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")


main()
