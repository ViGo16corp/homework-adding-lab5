class Bug:
    STATUS_LIST = ["OPEN", "IN_PROGRESS", "RESOLVED", "CLOSED"]
    
    def __init__(self, description, severity, deadline, status, assignee):
        self._description = description
        self._severity = severity
        self._deadline = deadline
        self._status = status
        self._assignee = assignee

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_severity(self):
        return self._severity

    def set_severity(self, severity):
        self._severity = severity

    def get_deadline(self):
        return self._deadline

    def set_deadline(self, deadline):
        self._deadline = deadline

    def get_status(self):
        return self._status

    def set_status(self, status):
        if status in self.STATUS_LIST:
            self._status = status
        else:
            print(f"Invalid status: {status}")

    def get_assignee(self):
        return self._assignee

    def set_assignee(self, assignee):
        self._assignee = assignee

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
        return "\n".join(str(bug) for bug in self._bugs)


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



