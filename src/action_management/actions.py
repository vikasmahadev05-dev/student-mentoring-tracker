"""
Module 3: Action Item Management
Author: Member 3
Description:
    Records tasks agreed upon during mentoring meetings.
    Each action is linked to a student and optionally to the meeting.
"""

from datetime import date
from shared_data import actions, students, meetings

# Synchronized reference to the shared actions list
action_list = actions


def get_valid_input(message):
    """Function to get non-empty input."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty! Please try again.")


def get_valid_date(message, minimum_date=None):
    """Function to get a valid date."""
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


def create_action():
    """Function to create an action item linked to student and optional meeting."""
    print("\n" + "=" * 40)
    print("           ADD ACTION ITEM")
    print("=" * 40)

    # Student ID input
    student_id = get_valid_input("Enter Student ID: ").upper()
    student = next((s for s in students if s["student_id"] == student_id), None)
    if student:
        print(f"Student: {student['name']} ({student_id})")
    else:
        print(f"Notice: Student ID '{student_id}' recorded.")

    # Optional Meeting Reference
    meeting_id = input("Enter Meeting ID (press Enter if none): ").strip().upper()
    if not meeting_id:
        meeting_id = None

    description = get_valid_input("Enter Action Description: ")
    assigned_date = date.today()
    print(f"Assigned Date (Today): {assigned_date}")

    due_date = get_valid_date("Enter Due Date (YYYY-MM-DD): ", assigned_date)
    follow_up_date = get_valid_date("Enter Follow-up Date (YYYY-MM-DD): ", assigned_date)

    # Generate unique Action ID
    action_num = len(action_list) + 101
    action_id = f"A{action_num}"
    while any(a["action_id"] == action_id for a in action_list):
        action_num += 1
        action_id = f"A{action_num}"

    action = {
        "action_id": action_id,
        "student_id": student_id,
        "meeting_id": meeting_id,
        "description": description,
        "assigned_date": str(assigned_date),
        "due_date": str(due_date),
        "follow_up_date": str(follow_up_date),
        "status": "Pending"
    }

    action_list.append(action)
    print("\n[✔] Action Item Added Successfully!")
    print(f"    Action ID      : {action_id}")
    student_name = student["name"] if student else student_id
    print(f"    Student        : {student_name} ({student_id})")
    print(f"    Follow-up Date : {follow_up_date}")
    print(f"    Status         : Pending")


def view_actions():
    """Function to view all action items."""
    if len(action_list) == 0:
        print("\n[!] No Action Items Found!")
        return

    print("\n" + "=" * 40)
    print("          ALL ACTION ITEMS")
    print("=" * 40)
    for action in action_list:
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
    """Function to search action items by Student ID."""
    student_id = get_valid_input("\nEnter Student ID to search: ").upper()
    found = False
    for action in action_list:
        if action["student_id"] == student_id:
            if not found:
                print(f"\nAction Items for Student: {student_id}")
                print("-" * 40)
            print("Action ID      :", action["action_id"])
            print("Description    :", action["description"])
            print("Due Date       :", action["due_date"])
            print("Follow-up Date :", action["follow_up_date"])
            print("Status         :", action["status"])
            print("-" * 40)
            found = True
    if not found:
        print(f"\n[!] No Action Items Found for Student: {student_id}")


def update_action():
    """Function to update an action item description or dates."""
    action_id = get_valid_input("\nEnter Action ID to update (e.g. A101): ").upper()
    for action in action_list:
        if action["action_id"] == action_id:
            print("\n1. Update Description")
            print("2. Update Due Date")
            print("3. Update Follow-up Date")
            choice = input("Enter your choice (1-3): ").strip()
            assigned_date = date.fromisoformat(action["assigned_date"])

            if choice == "1":
                action["description"] = get_valid_input("Enter new description: ")
            elif choice == "2":
                new_date = get_valid_date("Enter new due date (YYYY-MM-DD): ", assigned_date)
                action["due_date"] = str(new_date)
            elif choice == "3":
                new_date = get_valid_date("Enter new follow-up date (YYYY-MM-DD): ", assigned_date)
                action["follow_up_date"] = str(new_date)
            else:
                print("\n[!] Invalid Choice!")
                return

            print("\n[✔] Action Item Updated Successfully!")
            return

    print("\n[!] Action Item Not Found!")


def complete_action():
    """Function to mark an action item as completed."""
    action_id = get_valid_input("\nEnter Action ID to complete: ").upper()
    for action in action_list:
        if action["action_id"] == action_id:
            if action["status"] == "Completed":
                print("\n[!] Action Item is Already Completed!")
                return
            action["status"] = "Completed"
            print("\n[✔] Action Item Marked as Completed Successfully!")
            return
    print("\n[!] Action Item Not Found!")


def view_pending_actions():
    """Function to view pending action items."""
    found = False
    print("\n" + "=" * 40)
    print("        PENDING ACTION ITEMS")
    print("=" * 40)
    for action in action_list:
        if action["status"] == "Pending":
            print("\nAction ID      :", action["action_id"])
            print("Student ID     :", action["student_id"])
            print("Description    :", action["description"])
            print("Due Date       :", action["due_date"])
            print("Follow-up Date :", action["follow_up_date"])
            print("-" * 40)
            found = True
    if not found:
        print("\nNo Pending Action Items Found!")


def view_completed_actions():
    """Function to view completed action items."""
    found = False
    print("\n" + "=" * 40)
    print("       COMPLETED ACTION ITEMS")
    print("=" * 40)
    for action in action_list:
        if action["status"] == "Completed":
            print("\nAction ID   :", action["action_id"])
            print("Student ID  :", action["student_id"])
            print("Description :", action["description"])
            print("Due Date    :", action["due_date"])
            print("-" * 40)
            found = True
    if not found:
        print("\nNo Completed Action Items Found!")


def get_overdue_actions():
    """Helper: identify overdue action items."""
    today = date.today()
    found = False
    print("\n" + "=" * 40)
    print("        OVERDUE ACTION ITEMS")
    print("=" * 40)
    for action in action_list:
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
