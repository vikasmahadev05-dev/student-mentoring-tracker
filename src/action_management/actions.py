from datetime import date
# List to store all action items
action_list = []
# Function to get non-empty input
def get_valid_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty! Please try again.")
# Function to get a valid date
def get_valid_date(message, minimum_date=None):
    while True:
        date_input = input(message).strip()
        try:
            valid_date = date.fromisoformat(date_input)
            if minimum_date and valid_date < minimum_date:
                print("Date cannot be earlier than assigned date!")
                continue
            return valid_date
        except ValueError:
            print("Invalid date! Enter date in YYYY-MM-DD format.")
# Function to create an action item
def create_action():
    action_id = "A" + str(len(action_list) + 1).zfill(3)
    student_id = get_valid_input("Enter Student ID: ")
    meeting_id = input("Enter Meeting ID (press Enter if none): ").strip()
    description = get_valid_input("Enter Action Description: ")
    assigned_date = date.today()
    due_date = get_valid_date(
        "Enter Due Date (YYYY-MM-DD): ", assigned_date
    )
    follow_up_date = get_valid_date(
        "Enter Follow-up Date (YYYY-MM-DD): ", assigned_date
    )
    action = {
        "action_id": action_id,
        "student_id": student_id,
        "meeting_id": meeting_id if meeting_id else None,
        "description": description,
        "assigned_date": str(assigned_date),
        "due_date": str(due_date),
        "follow_up_date": str(follow_up_date),
        "status": "Pending"
    }
    action_list.append(action)
    print("\nAction Item Added Successfully!")
    print("Action ID:", action_id)
# Function to view all action items
def view_actions():
    if len(action_list) == 0:
        print("\nNo Action Items Found!")
        return
    print("\n========== ALL ACTION ITEMS ==========")
    for action in action_list:
        print("\nAction ID:", action["action_id"])
        print("Student ID:", action["student_id"])
        print("Meeting ID:", action["meeting_id"])
        print("Description:", action["description"])
        print("Assigned Date:", action["assigned_date"])
        print("Due Date:", action["due_date"])
        print("Follow-up Date:", action["follow_up_date"])
        print("Status:", action["status"])
    print("\n======================================")
# Function to search action items by Student ID
def search_actions():
    student_id = get_valid_input("\nEnter Student ID to search: ")
    found = False
    for action in action_list:
        if action["student_id"] == student_id:
            if not found:
                print("\nAction Items for Student:", student_id)
                print("--------------------------------------")
            print("\nAction ID:", action["action_id"])
            print("Description:", action["description"])
            print("Due Date:", action["due_date"])
            print("Follow-up Date:", action["follow_up_date"])
            print("Status:", action["status"])
            found = True
    if not found:
        print("\nNo Action Items Found for Student:", student_id)
# Function to update an action item
def update_action():
    action_id = get_valid_input("\nEnter Action ID to update: ")
    for action in action_list:
        if action["action_id"] == action_id:
            print("\n1. Update Description")
            print("2. Update Due Date")
            print("3. Update Follow-up Date")
            choice = input("Enter your choice: ")
            assigned_date = date.fromisoformat(action["assigned_date"])
            if choice == "1":
                action["description"] = get_valid_input(
                    "Enter new description: "
                )
            elif choice == "2":
                new_date = get_valid_date(
                    "Enter new due date (YYYY-MM-DD): ",
                    assigned_date
                )
                action["due_date"] = str(new_date)
            elif choice == "3":
                new_date = get_valid_date(
                    "Enter new follow-up date (YYYY-MM-DD): ",
                    assigned_date
                )
                action["follow_up_date"] = str(new_date)
            else:
                print("\nInvalid Choice!")
                return
            print("\nAction Item Updated Successfully!")
            return
    print("\nAction Item Not Found!")
# Function to mark an action item as completed
def complete_action():
    action_id = get_valid_input("\nEnter Action ID to complete: ")
    for action in action_list:
        if action["action_id"] == action_id:
            if action["status"] == "Completed":
                print("\nAction Item is Already Completed!")
                return
            action["status"] = "Completed"
            print("\nAction Item Marked as Completed Successfully!")
            return
    print("\nAction Item Not Found!")
# Function to view pending action items
def view_pending_actions():
    found = False
    print("\n========== PENDING ACTION ITEMS ==========")
    for action in action_list:
        if action["status"] == "Pending":
            print("\nAction ID:", action["action_id"])
            print("Student ID:", action["student_id"])
            print("Description:", action["description"])
            print("Due Date:", action["due_date"])
            found = True
    if not found:
        print("\nNo Pending Action Items Found!")
# Function to view completed action items
def view_completed_actions():
    found = False
    print("\n========== COMPLETED ACTION ITEMS ==========")
    for action in action_list:
        if action["status"] == "Completed":
            print("\nAction ID:", action["action_id"])
            print("Student ID:", action["student_id"])
            print("Description:", action["description"])
            print("Due Date:", action["due_date"])
            found = True
    if not found:
        print("\nNo Completed Action Items Found!")
# Function to identify overdue action items
def get_overdue_actions():
    today = date.today()
    found = False
    print("\n========== OVERDUE ACTION ITEMS ==========")
    for action in action_list:
        follow_up_date = date.fromisoformat(action["follow_up_date"])
        if action["status"] == "Pending" and follow_up_date < today:
            print("\nAction ID:", action["action_id"])
            print("Student ID:", action["student_id"])
            print("Description:", action["description"])
            print("Follow-up Date:", action["follow_up_date"])
            print("Status:", action["status"])
            found = True
    if not found:
        print("\nNo Overdue Action Items Found!")
