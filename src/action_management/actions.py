"""
Module 3: Action Item Management
Author: Member 3
Description:
    Records tasks agreed upon during mentoring meetings.
    Each action is linked to a student and optionally to the meeting.
"""

from datetime import date
from data.sample_data import actions, students


def get_valid_input(message):
    """Prompt until a non-empty string is entered."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty! Please try again.")


def get_valid_date(message, minimum_date=None):
    """Prompt until a valid YYYY-MM-DD date (>= minimum_date) is entered."""
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


def find_student(student_id):
    """Return the student dictionary matching student_id, or None."""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def find_action(action_id):
    """Return the action dictionary matching action_id, or None."""
    for action in actions:
        if action["action_id"] == action_id:
            return action
    return None


def generate_action_id():
    """Generate a unique Action ID like A101, A102, etc."""
    action_num = len(actions) + 101
    while find_action(f"A{action_num}"):
        action_num += 1
    return f"A{action_num}"


def create_action():
    """Create an action item linked to a student and optional meeting."""
    print("\n" + "=" * 40)
    print("           ADD ACTION ITEM")
    print("=" * 40)

    student_id = get_valid_input("Enter Student ID: ").upper()
    student = find_student(student_id)
    if student:
        print(f"Student: {student['name']} ({student_id})")
    else:
        print(f"Notice: Student ID '{student_id}' recorded.")

    meeting_id = input("Enter Meeting ID (press Enter if none): ").strip().upper() or None
    description = get_valid_input("Enter Action Description: ")

    assigned_date = date.today()
    print(f"Assigned Date (Today): {assigned_date}")

    due_date = get_valid_date("Enter Due Date (YYYY-MM-DD): ", assigned_date)
    follow_up_date = get_valid_date("Enter Follow-up Date (YYYY-MM-DD): ", assigned_date)

    action_id = generate_action_id()
    actions.append({
        "action_id": action_id,
        "student_id": student_id,
        "meeting_id": meeting_id,
        "description": description,
        "assigned_date": str(assigned_date),
        "due_date": str(due_date),
        "follow_up_date": str(follow_up_date),
        "status": "Pending",
    })

    student_name = student["name"] if student else student_id
    print("\n[✔] Action Item Added Successfully!")
    print(f"    Action ID      : {action_id}")
    print(f"    Student        : {student_name} ({student_id})")
    print(f"    Follow-up Date : {follow_up_date}")
    print(f"    Status         : Pending")


def view_actions():
    """Display all action items."""
    if not actions:
        print("\n[!] No Action Items Found!")
        return

    print("\n" + "=" * 40)
    print("          ALL ACTION ITEMS")
    print("=" * 40)
    for action in actions:
        meeting_str = action.get("meeting_id") or "None (Standalone)"
        print("\nAction ID      :", action["action_id"])
        print("Student ID     :", action["student_id"])
        print("Meeting ID     :", meeting_str)
        print("Description    :", action["description"])
        print("Assigned Date  :", action["assigned_date"])
        print("Due Date       :", action["due_date"])
        print("Follow-up Date :", action["follow_up_date"])
        print("Status         :", action["status"])
        print("-" * 40)


def search_actions():
    """Search and display action items by Student ID."""
    student_id = get_valid_input("\nEnter Student ID to search: ").upper()
    matches = [a for a in actions if a["student_id"] == student_id]

    if not matches:
        print(f"\n[!] No Action Items Found for Student: {student_id}")
        return

    print(f"\nAction Items for Student: {student_id}")
    print("-" * 40)
    for action in matches:
        print("Action ID      :", action["action_id"])
        print("Description    :", action["description"])
        print("Due Date       :", action["due_date"])
        print("Follow-up Date :", action["follow_up_date"])
        print("Status         :", action["status"])
        print("-" * 40)


def update_action():
    """Update an action item's description, due date, or follow-up date."""
    action_id = get_valid_input("\nEnter Action ID to update (e.g. A101): ").upper()
    action = find_action(action_id)

    if not action:
        print("\n[!] Action Item Not Found!")
        return

    print("\n1. Update Description")
    print("2. Update Due Date")
    print("3. Update Follow-up Date")
    choice = input("Enter your choice (1-3): ").strip()
    assigned_date = date.fromisoformat(action["assigned_date"])

    if choice == "1":
        action["description"] = get_valid_input("Enter new description: ")
    elif choice == "2":
        action["due_date"] = str(get_valid_date("Enter new due date (YYYY-MM-DD): ", assigned_date))
    elif choice == "3":
        action["follow_up_date"] = str(get_valid_date("Enter new follow-up date (YYYY-MM-DD): ", assigned_date))
    else:
        print("\n[!] Invalid Choice!")
        return

    print("\n[✔] Action Item Updated Successfully!")


def complete_action():
    """Mark an action item as completed."""
    action_id = get_valid_input("\nEnter Action ID to complete: ").upper()
    action = find_action(action_id)

    if not action:
        print("\n[!] Action Item Not Found!")
        return

    if action["status"] == "Completed":
        print("\n[!] Action Item is Already Completed!")
        return

    action["status"] = "Completed"
    print("\n[✔] Action Item Marked as Completed Successfully!")


def view_pending_actions():
    """Display all pending action items."""
    print("\n" + "=" * 40)
    print("        PENDING ACTION ITEMS")
    print("=" * 40)

    pending = [a for a in actions if a["status"] == "Pending"]
    if not pending:
        print("\nNo Pending Action Items Found!")
        return

    for action in pending:
        print("\nAction ID      :", action["action_id"])
        print("Student ID     :", action["student_id"])
        print("Description    :", action["description"])
        print("Due Date       :", action["due_date"])
        print("Follow-up Date :", action["follow_up_date"])
        print("-" * 40)


def view_completed_actions():
    """Display all completed action items."""
    print("\n" + "=" * 40)
    print("       COMPLETED ACTION ITEMS")
    print("=" * 40)

    completed = [a for a in actions if a["status"] == "Completed"]
    if not completed:
        print("\nNo Completed Action Items Found!")
        return

    for action in completed:
        print("\nAction ID   :", action["action_id"])
        print("Student ID  :", action["student_id"])
        print("Description :", action["description"])
        print("Due Date    :", action["due_date"])
        print("-" * 40)


def get_overdue_actions():
    """Identify and display overdue pending action items."""
    today = date.today()
    print("\n" + "=" * 40)
    print("        OVERDUE ACTION ITEMS")
    print("=" * 40)

    found = False
    for action in actions:
        follow_up_date = date.fromisoformat(action["follow_up_date"])
        if action["status"] == "Pending" and follow_up_date < today:
            print("\nAction ID      :", action["action_id"])
            print("Student ID     :", action["student_id"])
            print("Description    :", action["description"])
            print("Follow-up Date :", action["follow_up_date"])
            print("Status         : OVERDUE")
            print("-" * 40)
            found = True

    if not found:
        print("\nNo Overdue Action Items Found!")


# -------------------------------------------------------------
# Module Submenu (called by main.py)
# -------------------------------------------------------------

def action_menu():
    """Submenu loop for Action Item Management."""
    while True:
        print("\n" + "=" * 40)
        print("       ACTION ITEM MANAGEMENT")
        print("=" * 40)
        print("1. Add Action Item")
        print("2. View All Action Items")
        print("3. Search Actions by Student ID")
        print("4. Update Action Details")
        print("5. Mark Action as Completed")
        print("6. View Pending Actions")
        print("7. View Completed Actions")
        print("8. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            create_action()
        elif choice == "2":
            view_actions()
        elif choice == "3":
            search_actions()
        elif choice == "4":
            update_action()
        elif choice == "5":
            complete_action()
        elif choice == "6":
            view_pending_actions()
        elif choice == "7":
            view_completed_actions()
        elif choice == "8":
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid choice! Please select 1 to 8.")
