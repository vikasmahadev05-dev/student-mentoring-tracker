meeting_list = [
    {
        "meeting_id": "M1",
        "student_id": "101",
        "mentor_name": "Dr. Ramesh",
        "date": "2026-11-20",
        "topic": "Academic Review",
        "status": "Completed"
    },
    {
        "meeting_id": "M2",
        "student_id": "102",
        "mentor_name": "Prof. Anitha",
        "date": "2026-11-28",
        "topic": "Minor Project Discussion",
        "status": "Scheduled"
    }
]


def schedule_meeting():
    print("\n--- Schedule Meeting ---")
    meeting_id = "M" + str(len(meeting_list) + 1)
    student_id = input("Enter Student ID: ")
    mentor_name = input("Enter Mentor Name: ")
    date = input("Enter Meeting Date (YYYY-MM-DD): ")
    topic = input("Enter Meeting Topic: ")

    meeting = {
        "meeting_id": meeting_id,
        "student_id": student_id,
        "mentor_name": mentor_name,
        "date": date,
        "topic": topic,
        "status": "Scheduled"
    }
    meeting_list.append(meeting)
    print("\nMeeting scheduled successfully! Meeting ID:", meeting_id)


def view_meetings():
    print("\n--- All Meetings ---")
    if len(meeting_list) == 0:
        print("No meetings found!")
        return

    for m in meeting_list:
        print("ID:", m["meeting_id"], "| Student:", m["student_id"], "| Mentor:", m["mentor_name"], "| Date:", m["date"], "| Topic:", m["topic"], "| Status:", m["status"])


def search_meetings():
    print("\n--- Search Meetings ---")
    student_id = input("Enter Student ID to search: ")
    found = False

    for m in meeting_list:
        if m["student_id"] == student_id:
            print("ID:", m["meeting_id"], "| Mentor:", m["mentor_name"], "| Date:", m["date"], "| Topic:", m["topic"], "| Status:", m["status"])
            found = True

    if not found:
        print("No meetings found for Student ID:", student_id)


def update_meeting():
    print("\n--- Update Meeting ---")
    meeting_id = input("Enter Meeting ID to update: ")

    for m in meeting_list:
        if m["meeting_id"] == meeting_id:
            print("1. Update Date")
            print("2. Update Topic")
            print("3. Mark as Completed")
            choice = input("Enter choice (1-3): ")

            match choice:
                case "1":
                    m["date"] = input("Enter new date (YYYY-MM-DD): ")
                    print("Meeting date updated successfully!")
                case "2":
                    m["topic"] = input("Enter new topic: ")
                    print("Meeting topic updated successfully!")
                case "3":
                    m["status"] = "Completed"
                    print("Meeting marked as Completed!")
                case _:
                    print("Invalid choice!")
            return

    print("Meeting not found!")


def delete_meeting():
    print("\n--- Delete Meeting ---")
    meeting_id = input("Enter Meeting ID to delete: ")

    for m in meeting_list:
        if m["meeting_id"] == meeting_id:
            meeting_list.remove(m)
            print("Meeting", meeting_id, "deleted successfully!")
            return

    print("Meeting not found!")


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

        choice = input("Enter your choice (1-6): ")

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


if __name__ == "__main__":
    meeting_menu()
