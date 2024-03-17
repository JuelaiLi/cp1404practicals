def get_password():
    min_password_length = 8
    max_password_length = 20

    password = input("Enter your password: ")
    while len(password) < min_password_length or len(password) > max_password_length:
        print("Invalid password")
        password = input("Enter your password: ")

    return password

def main():
    password = get_password()
    print("*" * len(password))

if __name__ == "__main__":
    main()
