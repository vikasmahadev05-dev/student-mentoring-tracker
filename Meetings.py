# ==============================================================================
# Student Mentoring Tracker - Meetings Module (Phase 1)
# Procedural programming using functions, loops, match-case (switch case), and list of dicts.
# ==============================================================================

# In-memory data structure storing meetings as a list of dictionaries
meeting_list = [
    {
        "meeting_id": "M001",
        "student_id": "101",
        "mentor_name": "Dr. Ramesh",
        "date": "2026-11-20",
        "topic": "Academic Review",
        "status": "Completed"
    },
    {
        "meeting_id": "M002",
        "student_id": "102",
        "mentor_name": "Prof. Anitha",
        "date": "2026-11-28",
        "topic": "Minor Project Discussion",
        "status": "Scheduled"
    }
]


# Core Operation 1: Schedule a New Meeting
def schedule_meeting():
    print("\n--- Schedule Meeting ---")
    meeting_id = "M" + str(len(meeting_list) + 1).zfill(3)
    student_id = input("Enter Student ID: ").strip()
    mentor_name = input("Enter Mentor Name: ").strip()
    date = input("Enter Meeting Date (YYYY-MM-DD): ").strip()
    topic = input("Enter Meeting Topic: ").strip()

    meeting = {
        "meeting_id": meeting_id,
        "student_id": student_id,
        "mentor_name": mentor_name,
        "date": date,
        "topic": topic,
        "status": "Scheduled"
    }
    meeting_list.append(meeting)
    print(f"\n[+] Meeting scheduled successfully! Meeting ID: {meeting_id}")


# Core Operation 2: View All Meetings
def view_meetings():
    print("\n--- All Meetings ---")
    if len(meeting_list) == 0:
        print("No meetings found!")
        return

    for m in meeting_list:
        print(f"ID: {m['meeting_id']} | Student: {m['student_id']} | Mentor: {m['mentor_name']} | Date: {m['date']} | Topic: {m['topic']} | Status: {m['status']}")


# Core Operation 2 (Contd): Search Meetings by Student ID
def search_meetings():
    print("\n--- Search Meetings ---")
    student_id = input("Enter Student ID to search: ").strip()
    found = False

    for m in meeting_list:
        if m["student_id"] == student_id:
            print(f"ID: {m['meeting_id']} | Mentor: {m['mentor_name']} | Date: {m['date']} | Topic: {m['topic']} | Status: {m['status']}")
            found = True

    if not found:
        print(f"No meetings found for Student ID: {student_id}")


# Core Operation 3: Update Meeting Details or Mark as Completed
def update_meeting():
    print("\n--- Update Meeting ---")
    meeting_id = input("Enter Meeting ID to update: ").strip()

    for m in meeting_list:
        if m["meeting_id"] == meeting_id:
            print("1. Update Date")
            print("2. Update Topic")
            print("3. Mark as Completed")
            choice = input("Enter choice (1-3): ").strip()

            # Switch-case using Python's match-case
            match choice:
                case "1":
                    m["date"] = input("Enter new date (YYYY-MM-DD): ").strip()
                    print("Meeting date updated successfully!")
                case "2":
                    m["topic"] = input("Enter new topic: ").strip()
                    print("Meeting topic updated successfully!")
                case "3":
                    m["status"] = "Completed"
                    print("Meeting marked as Completed!")
                case _:
                    print("Invalid choice!")
            return

    print("Meeting not found!")


# Delete a meeting
def delete_meeting():
    print("\n--- Delete Meeting ---")
    meeting_id = input("Enter Meeting ID to delete: ").strip()

    for i in range(len(meeting_list)):
        if meeting_list[i]["meeting_id"] == meeting_id:
            del meeting_list[i]
            print(f"Meeting {meeting_id} deleted successfully!")
            return

    print("Meeting not found!")


# Menu-Driven Loop using Switch Case (match-case)
def meeting_menu():
    while True:
        print("\n" + "=" * 35)
        print("      MEETING MANAGEMENT MENU")
        print("=" * 35)
        print("1. Schedule Meeting")
        print("2. View All Meetings")
        print("3. Search Meetings by Student ID")
        print("4. Update / Complete Meeting")
        print("5. Delete Meeting")
        print("6. Exit")
        print("=" * 35)

        choice = input("Enter your choice (1-6): ").strip()

        # Switch-case implementation
        match choice:
            case "1":
                schedule_meeting()
            case "2":
                view_meetings()
            case "3":
                search_meetings()
            case "4":
                update_meeting()
            case "5":
                delete_meeting()
            case "6":
                print("Returning to Main Menu...")
                break
            case _:
                print("Invalid choice! Please enter a number between 1 and 6.")


# Direct execution entry point
if __name__ == "__main__":
    meeting_menu()
