class Audit:
    def __init__(self, audit_id, location, auditor, date_time):
        self.audit_id = audit_id
        self.location = location
        self.auditor = auditor
        self.date_time = date_time
        self.audit_done = False

class SafetyIssue:
    def __init__(self, issue_id, audit_id, description, severity):
        self.issue_id = issue_id
        self.audit_id = audit_id
        self.description = description
        self.severity = severity

audits_db = {
    1: Audit(1, 'Intersection A', 'John Doe', '2023-04-25 09:00:00'),
    2: Audit(2, 'Highway B', 'Jane Smith', '2023-04-26 10:30:00'),
    3: Audit(3, 'Street C', 'David Johnson', '2023-04-27 11:45:00'),
    4: Audit(4, 'Roundabout D', 'Emily Brown', '2023-04-28 08:15:00'),
    5: Audit(5, 'Crosswalk E', 'Michael Davis', '2023-04-29 13:20:00'),
    6: Audit(6, 'Intersection F', 'Sophia Wilson', '2023-04-30 14:45:00'),
    7: Audit(7, 'Highway G', 'Daniel Martinez', '2023-05-01 10:00:00'),
    8: Audit(8, 'Street H', 'Olivia Anderson', '2023-05-02 12:30:00'),
    9: Audit(9, 'Roundabout I', 'James Taylor', '2023-05-03 09:45:00'),
    10: Audit(10, 'Crosswalk J', 'Emma Brown', '2023-05-04 08:00:00')
}

issues_db = {}

unsuccessful_db = {}

def create_audit():
    audit_id = int(input("Enter audit ID: ")) 
    audit = audits_db.get(audit_id)
    if audit:
        print("Already record exists with the same audit_id, please enter with a different ID")
        return
    
    location = input("Enter location: ")
    if not location:
        print("Location is required. Audit creation unsuccessful.")
        return
    
    auditor = input("Enter auditor: ")
    if not auditor:
        print("Auditor is required. Audit creation unsuccessful.")
        return
    
    date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    if not date_time:
        print("Date and time are required. Audit creation unsuccessful.")
        return
    
    audit = Audit(audit_id, location, auditor, date_time)
    audits_db[audit_id] = audit
    print("Audit created successfully.")

def read_audit(audit_id):
    audit = audits_db.get(audit_id)
    if audit:
        print(f"Audit ID: {audit.audit_id}, Location: {audit.location}, Auditor: {audit.auditor}, Date Time: {audit.date_time}")
    else:
        print("No audit record found.")

def update_audit(audit_id):
    audit = audits_db.get(audit_id)
    if audit:
        print("What would you like to update?")
        print("1. Location")
        print("2. Auditor")
        print("3. Date")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            new_location = input("Enter new location: ")
            audit.location = new_location
            print("Location updated successfully.")
        elif choice == 2:
            new_auditor = input("Enter new auditor: ")
            audit.auditor = new_auditor
            print("Auditor updated successfully.")
        elif choice == 3:
            new_date = input("Enter new date and time (YYYY-MM-DD HH:MM:SS): ")
            audit.date_time = new_date
            print("Date updated successfully.")
        else:
            print("Invalid choice.")
    else:
        print("No audit record found.")

def delete_audit(audit_id):
    if audit_id in audits_db:
        print("Are you sure to delete record ? (Enter yes or no)")
        result = input()
        if result == "YES" or result == "yes" :
            del audits_db[audit_id]
            print("Audit record deleted successfully.")
        else:
            print("No record deleted as per your choice")
    else:
        print("No audit record found.")

def report_safety_issue():
    audit_id = int(input("Enter related audit ID: "))
    if audit_id in audits_db:
        issue_id = int(input("Enter issue ID: "))
        if audit_id in unsuccessful_db:
            description = unsuccessful_db[audit_id]
            print("ISSUES are:", end = " ")
            print(*description)

            severity = input("Enter severity of the issue: ")
            issue = SafetyIssue(issue_id, audit_id, description, severity)
            issues_db[issue_id] = issue
            print("Safety issue reported successfully.")

        else:
            print("No issues with this audit_id")

    else:
        print("No audit record found")

def conduct_road_safety_audits(audit_id):
    audit = audits_db.get(audit_id)
    if audit:
        print(f"Conducting safety audit for Audit ID: {audit_id}, Location: {audit.location}, Auditor: {audit.auditor}, Date Time: {audit.date_time}")
        rc = check_road_conditions(audit)
        ts = check_traffic_signs(audit)
        crm = check_road_markings(audit)
        cv = check_visibility(audit)
        if rc > 2.5 and ts > 2.5 and crm > 2.5 and cv > 2.5:
            audit.audit_done = True
            print("Safety audit conducted successfully.")
        else:
            unsuccessful_db[audit_id] = []
            if rc < 2.5:
                unsuccessful_db[audit_id].append("ROAD CONDITIONS(road surface, potholes, cracks)")

            if ts < 2.5:
                unsuccessful_db[audit_id].append("TRAFFIC SIGNS(condition and visibility of traffic signs)")

            if crm < 2.5:
                unsuccessful_db[audit_id].append("ROAD MARKINGS(condition and visibility of road markings)")

            if cv < 2.5:
                unsuccessful_db[audit_id].append("VISIBILITY AT INTERSECTIONS AND PEDESTRIANS")
            
            
            print("Safety audit conducted unsuccessful")
            return False
    else:
        print("No audit record found.")

def check_road_conditions(audit):
    rc = float(input("ENTER THE REVIEWS OF ROAD CONDITIONS (road surface, potholes, cracks): "))
    return rc

def check_traffic_signs(audit):
    ts = float(input("ENTER THE REVIEWS OF TRAFFIC SIGNS (condition and visibility of traffic signs): "))
    return ts

def check_road_markings(audit):
    crm = float(input("ENTER THE REVIEWS OF ROAD MARKINGS (condition and visibility of road markings): "))
    return crm

def check_visibility(audit):
    cv = float(input("ENTER THE REVIEWS OF VISIBILITY CONDITIONS AT INTERSECTIONS AND PEDESTRIANS: "))
    return cv

while True:
    print("\nChoose an option:")
    print("1. Create audit")
    print("2. Read audit")
    print("3. Update audit")
    print("4. Delete audit")
    print("5. Conduct safety audit")
    print("6. Report safety issue")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_audit()
    elif choice == 2:
        audit_id = int(input("Enter audit ID to read: "))
        read_audit(audit_id)
    elif choice == 3:
        audit_id = int(input("Enter audit ID to update: "))
        update_audit(audit_id)
    elif choice == 4:
        audit_id = int(input("Enter audit ID to delete: "))
        delete_audit(audit_id)
    elif choice == 6:
        report_safety_issue()
    elif choice == 5:
        audit_id = int(input("Enter audit ID to conduct safety audit: "))
        conduct_road_safety_audits(audit_id)
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
