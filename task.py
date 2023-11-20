class Bug:
    def __init__(self, description, severity, deadline, status, assignee):
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self.status = status
        self.assignee = assignee

    def __str__(self):
        return f"Description: {self.description}\nSeverity: {self.severity}\nDeadline: {self.deadline}\nStatus: {self.status}\nAssignee: {self.assignee}\n"

class Backlog:
    def __init__(self):
        self.bugs = []

    def add_bug(self, bug):
        self.bugs.append(bug)

    def get_resolved_bugs_for_assignee(self, assignee):
        resolved_bugs = [bug for bug in self.bugs if bug.status == "RESOLVED" and bug.assignee == assignee]
        return resolved_bugs

    def sort_by_severity(self):
        self.bugs.sort(key=lambda bug: bug.severity)

    def __str__(self):
        backlog_str = ""
        for bug in self.bugs:
            backlog_str += str(bug) + "\n"
        return backlog_str

# Демонстрація роботи класів
if __name__ == "__main__":
    bug1 = Bug("Crash on startup", "Critical", "2023-11-01", "RESOLVED", "Developer A")
    bug2 = Bug("UI glitch", "Minor", "2023-10-30", "OPEN", "Developer B")
    bug3 = Bug("Database connection issue", "Major", "2023-11-05", "RESOLVED", "Developer A")

    backlog = Backlog()
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    backlog.add_bug(bug3)

    print("All Bugs in Backlog:")
    print(backlog)

    backlog.sort_by_severity()
    print("Backlog Sorted by Severity:")
    print(backlog)

    assignee = "Developer A"
    resolved_bugs = backlog.get_resolved_bugs_for_assignee(assignee)
    print(f"Resolved Bugs for {assignee}:")
    for bug in resolved_bugs:
        print(bug)
