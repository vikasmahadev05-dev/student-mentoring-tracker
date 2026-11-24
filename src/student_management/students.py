
import json
from datetime import datetime, date

FILE_NAME = "mentoring_records.json"


# ---------------------------------
# LOAD AND SAVE RECORDS
# ---------------------------------

def load_records():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"meetings": [], "actions": []}
    except json.JSONDecodeError:
        print("Warning: Data file is damaged. Starting with empty records.")
        return {"meetings": [], "actions": []}


def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


# ---------------------------------
# DATE VALIDATION
# ---------------------------------

def get_valid_date(message):
    while True:
        date_input = input(message)

        try:
            return datetime.strptime(
                date_input, "%Y-%m-%d"
            ).date().isoformat()

        except ValueError:
            print("Invalid date! Enter date in YYYY-MM-DD format.")


# ---------------------------------
# 1. SCHEDULE MEETING AND RECORD ACTIONS
# ---------------------------------

def schedule_meeting(records):

    print("\n--- Schedule Mentoring Meeting ---")

    student_id = input("Enter Student ID: ").strip()
    student_name = input("Enter Student Name: ").strip()
    mentor_name = input("Enter Mentor Name: ").strip()

    if not student_id or not student_name or not mentor_name:
        print("Student ID, student name and mentor name are required.")
        return

    meeting_date = get_valid_date("Enter Meeting Date (YYYY-MM-DD): ")

    discussion = input("Enter Meeting Discussion/Notes: ").strip()

    meeting_id = "M" + str(len(records["meetings"]) + 1).zfill(3)

    meeting = {
        "meeting_id": meeting_id,
        "student_id": student_id,
        "student_name": student_name,
        "mentor_name": mentor_name,
        "meeting_date": meeting_date,
        "discussion": discussion
    }

    records["meetings"].append(meeting)

    print("\nMeeting scheduled successfully!")
    print("Meeting ID:", meeting_id)

    # Record agreed actions

    while True:
        try:
            count = int(input("\nHow many action items to record? "))

            if count < 0:
                print("Enter zero or a positive number.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    for i in range(count):

        print("\nAction Item", i + 1)

        description = input("Enter Action Description: ").strip()

        if not description:
            print("Action description cannot be empty. Try again.")
            continue

        due_date = get_valid_date("Enter Follow-up Date (YYYY-MM-DD): ")

        action_id = "A" + str(len(records["actions"]) + 1).zfill(3)

        action = {
            "action_id": action_id,
            "meeting_id": meeting_id,
            "student_id": student_id,
            "student_name": student_name,
            "mentor_name": mentor_name,
            "description": description,
            "due_date": due_date,
            "status": "Pending"
        }

        records["actions"].append(action)

        print("Action recorded successfully! Action ID:", action_id)

    save_records(records)
    print("\nMeeting and action records saved successfully!")


# ---------------------------------
# 2. UPDATE ACTION STATUS
# ---------------------------------

def update_action(records):

    print("\n--- Update Action Status ---")

    action_id = input("Enter Action ID: ").strip().upper()

    for action in records["actions"]:

        if action["action_id"] == action_id:

            print("\nAction Description:", action["description"])
            print("Student:", action["student_name"])
            print("Current Status:", action["status"])

            print("\n1. Mark as Completed")
            print("2. Mark as Pending")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                action["status"] = "Completed"

            elif choice == "2":
                action["status"] = "Pending"

            else:
                print("Invalid choice!")
                return

            save_records(records)

            print("\nAction status updated successfully!")
            return

    print("\nAction ID not found!")


# ---------------------------------
# 3. VIEW PENDING AND OVERDUE ACTIONS
# ---------------------------------

def view_pending_actions(records):

    print("\n--- Pending and Overdue Actions ---")

    today = date.today()

    found = False

    for action in records["actions"]:

        if action["status"] == "Pending":

            found = True

            due_date = datetime.strptime(
                action["due_date"], "%Y-%m-%d"
            ).date()

            if due_date < today:
                status = "OVERDUE"
            else:
                status = "PENDING"

            print("\n-----------------------------")
            print("Action ID:", action["action_id"])
            print("Student:", action["student_name"])
            print("Student ID:", action["student_id"])
            print("Mentor:", action["mentor_name"])
            print("Action:", action["description"])
            print("Follow-up Date:", action["due_date"])
            print("Status:", status)

    if not found:
        print("\nNo pending actions found.")


# ---------------------------------
# 4. VIEW ALL MEETING RECORDS
# ---------------------------------

def view_meetings(records):

    print("\n--- All Mentoring Meetings ---")

    if not records["meetings"]:
        print("No meeting records available.")
        return

    for meeting in records["meetings"]:

        print("\n-----------------------------")
        print("Meeting ID:", meeting["meeting_id"])
        print("Student ID:", meeting["student_id"])
        print("Student Name:", meeting["student_name"])
        print("Mentor:", meeting["mentor_name"])
        print("Meeting Date:", meeting["meeting_date"])
        print("Discussion:", meeting["discussion"])

        print("Associated Actions:")

        associated_actions = [
            action for action in records["actions"]
            if action["meeting_id"] == meeting["meeting_id"]
        ]

        if not associated_actions:
            print("No actions recorded.")
        else:
            for action in associated_actions:
                print(
                    action["action_id"],
                    "-",
                    action["description"],
                    "|",
                    action["status"],
                    "| Due:",
                    action["due_date"]
                )


# ---------------------------------
# MAIN MENU
# ---------------------------------

def main():

    records = load_records()

    while True:

        print("\n================================")
        print("     STUDENT MENTORING TRACKER")
        print("================================")

        print("1. Schedule Mentoring Meeting")
        print("2. Update Action Status")
        print("3. View Pending and Overdue Actions")
        print("4. View All Meeting Records")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            schedule_meeting(records)

        elif choice == "2":
            update_action(records)

        elif choice == "3":
            view_pending_actions(records)

        elif choice == "4":
            view_meetings(records)

        elif choice == "5":
            print("\nThank you for using Student Mentoring Tracker!")
            break

        else:
            print("\nInvalid choice! Please select 1 to 5.")


# ---------------------------------
# PROGRAM EXECUTION
# ---------------------------------

if __name__ == "__main__":
    main()
