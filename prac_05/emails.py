"""
Emails to Names
Estimate: 20 minutes
Actual: 15 minutes
"""
def main():
    """
    Main function to run the program.
    """
    emails_to_names = get_emails_and_names()
    print()
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")

def extract_name(email):
    """
    Extracts a presumptive name from an email address.
    """
    # Split the email address at '@' and take the first part
    prefix = email.split('@')[0]
    # Further split by any dots or underscores and capitalize each part
    parts = prefix.replace('.', ' ').replace('_', ' ').title().split()
    # Join the parts back together
    name = ' '.join(parts)
    return name

def get_emails_and_names():
    """
    Collects emails and corresponding names from user input.
    """
    emails_to_names = {}
    email = input("Email: ")
    while email:
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        # If the user says their name is not correct, ask for the correct name
        if confirmation not in ('', 'y', 'yes'):
            name = input("Name: ").title()
        emails_to_names[email] = name
        email = input("Email: ")
    return emails_to_names


# Run the program
if __name__ == "__main__":
    main()
