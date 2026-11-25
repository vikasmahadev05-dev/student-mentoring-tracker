"""
Module 2: Meeting Management
Author: Member 2
Description:
    Schedules, views, searches, updates, and deletes mentoring meetings
    using the shared in-memory data store.
"""

from data.sample_data import meetings, students, mentors


def find_meeting(meeting_id):
    """Find and return a meeting dictionary by its ID, or None."""
    for meeting in meetings:
        if meeting["meeting_id"] == meeting_id:
            return meeting
    return None


def find_student(student_id):
    """Find and return a student dictionary by ID, or None."""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def find_mentor(mentor_id):
    """Find and return a mentor dictionary by ID, or None."""
    for mentor in mentors:
        if mentor["mentor_id"] == mentor_id:
            return mentor
    return None


def generate_meeting_id():
    """Generate a unique Meeting ID like MT101, MT102, etc."""
    num = len(meetings) + 101
    while find_meeting(f"MT{num}"):
        num += 1
    return f"MT{num}"


def print_meeting(meeting):
    """Display one meeting record in a readable format."""
    student = find_student(meeting["student_id"])
    student_label = f"{student['name']} ({meeting['student_id']})" if student else meeting["student_id"]

    mentor_id = meeting.get("mentor_id")
    if mentor_id:
        mentor = find_mentor(mentor_id)
        mentor_label = f"{mentor['name']} ({mentor_id})" if mentor else mentor_id
    else:
        mentor_label = meeting.get("mentor_name", "Not Assigned")

    topic = meeting.get("description") or meeting.get("topic", "")
    print("Meeting ID :", meeting["meeting_id"])
    print("Student    :", student_label)
    print("Mentor     :", mentor_label)
    print("Date       :", meeting["date"])
    if meeting.get("time"):
        print("Time       :", meeting["time"])
    print("Topic      :", topic)
    if meeting.get("notes"):
        print("Notes      :", meeting["notes"])
    print("Status     :", meeting["status"])
    print("-" * 25)


def schedule_meeting():
    """Schedule a new mentoring meeting and save it to shared meetings."""
    print("\n--- Schedule Meeting ---")
    student_id = input("Enter Student ID: ").strip().upper()
    if not student_id:
        print("Student ID cannot be empty!")
        return

    student = find_student(student_id)
    if student:
        print(f"Student: {student['name']} ({student_id})")

    # Suggest assigned mentor if student already has one
    default_mentor = student.get("mentor_id") if student else None
    prompt = f"Enter Mentor ID [{default_mentor}]: " if default_mentor else "Enter Mentor ID: "
    mentor_id = input(prompt).strip().upper() or default_mentor

    date_str = input("Enter Meeting Date (YYYY-MM-DD): ").strip()
    time_str = input("Enter Meeting Time (e.g. 10:30 AM): ").strip()
    description = input("Enter Meeting Topic / Description: ").strip()
    notes = input("Enter Notes (optional): ").strip()

    meeting_id = generate_meeting_id()
    meetings.append({
        "meeting_id": meeting_id,
        "student_id": student_id,
        "mentor_id": mentor_id,
        "date": date_str,
        "time": time_str,
        "description": description,
        "notes": notes,
        "status": "Scheduled",
    })
    print("Meeting scheduled successfully!")
    print("Meeting ID:", meeting_id)


def view_meetings():
    """Display all scheduled and completed meetings."""
    print("\n--- All Meetings ---")
    if not meetings:
        print("No meetings found!")
        return

    for meeting in meetings:
        print_meeting(meeting)


def search_meetings():
    """Search and display meetings for a given Student ID."""
    print("\n--- Search Meetings ---")
    student_id = input("Enter Student ID to search: ").strip().upper()
    matches = [m for m in meetings if m["student_id"] == student_id]

    if not matches:
        print("No meetings found for this Student ID.")
        return

    for meeting in matches:
        print_meeting(meeting)


def update_meeting():
    """Update meeting date, topic, notes, or mark it as completed."""
    print("\n--- Update Meeting ---")
    meeting_id = input("Enter Meeting ID to update: ").strip().upper()
    meeting = find_meeting(meeting_id)

    if not meeting:
        print("Meeting not found!")
        return

    print("1. Update Date")
    print("2. Update Topic / Description")
    print("3. Update Notes")
    print("4. Mark as Completed")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        meeting["date"] = input("Enter new date (YYYY-MM-DD): ").strip()
        print("Date updated successfully!")
    elif choice == "2":
        meeting["description"] = input("Enter new topic / description: ").strip()
        print("Topic updated successfully!")
    elif choice == "3":
        meeting["notes"] = input("Enter meeting notes: ").strip()
        print("Notes updated successfully!")
    elif choice == "4":
        meeting["status"] = "Completed"
        print("Meeting marked as Completed!")
    else:
        print("Invalid choice!")


def delete_meeting():
    """Delete a meeting record by Meeting ID."""
    print("\n--- Delete Meeting ---")
    meeting_id = input("Enter Meeting ID to delete: ").strip().upper()
    meeting = find_meeting(meeting_id)

    if not meeting:
        print("Meeting not found!")
        return

    meetings.remove(meeting)
    print("Meeting deleted successfully!")


def meeting_menu():
    """Submenu loop for Meeting Management."""
    while True:
        print("\n--- Meeting Menu ---")
        print("1. Schedule Meeting")
        print("2. View All Meetings")
        print("3. Search Meetings by Student ID")
        print("4. Update Meeting")
        print("5. Delete Meeting")
        print("6. Back to Main Menu")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            schedule_meeting()
        elif choice == "2":
            view_meetings()
        elif choice == "3":
            search_meetings()
        elif choice == "4":
            update_meeting()
        elif choice == "5":
            delete_meeting()
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice, please try again.")
