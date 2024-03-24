import datetime
from project import Project


def main():
    projects = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(file_name, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please choose again.")


def load_projects(file_name):
    """Load projects from the file"""
    projects = []
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    if len(lines) <= 1:
        print(f"No projects found in {file_name}.")
    else:
        for line in lines[1:]:
            data = line.strip().split('\t')
            name = data[0]
            start_date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
            priority = int(data[2])
            cost_estimate = float(data[3])
            completion_percentage = int(data[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        print(f"Loaded {len(projects)} projects from {file_name}")
    return projects


def save_projects(file_name, projects):
    """Save projects to the file"""
    try:
        with open(file_name, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                           f"{project.cost_estimate:.2f}\t{project.completion_percentage}\n")
        print(f"Projects saved to {file_name}")
    except IOError:
        print(f"Error saving to {file_name}")


def display_projects(projects):
    """Display incomplete and completed projects"""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    """Filter projects by start date"""
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    try:
        priority = int(priority)
        cost_estimate = float(cost_estimate)
        completion_percentage = int(completion_percentage)
        projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        print("Project added successfully.")
    except ValueError:
        print("Invalid input format.")


def update_project(projects):
    """ Update the project's percentage, priority"""
    print("Choose a project to update:")
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            new_completion = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_completion:
                try:
                    new_completion = int(new_completion)
                    project.update_completion(new_completion)
                except ValueError:
                    print("Invalid input for percentage.")
            if new_priority:
                try:
                    new_priority = int(new_priority)
                    project.update_priority(new_priority)
                except ValueError:
                    print("Invalid input for priority.")
            print("Project updated successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")


main()
