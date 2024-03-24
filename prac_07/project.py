class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize the Project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return the string for the project"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def update_completion(self, new_completion_percentage):
        """Update the percentage for the project"""
        self.completion_percentage = new_completion_percentage

    def update_priority(self, new_priority):
        """Update the priority for the project."""
        self.priority = new_priority
