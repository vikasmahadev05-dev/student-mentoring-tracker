"""
Student Mentoring Tracker - Meeting Management Module (meetings.py)
Phase 1: Procedural Programming Implementation
Member 2: Meetings Module

This module provides a complete menu-driven interface to manage mentoring meetings.
It demonstrates the three core operations:
  1. Schedule a New Meeting (Create / Add)
  2. View and Search Meetings (Read / Query)
  3. Update Meeting Details, Record Minutes, and Update Status (Update / Complete)
plus Cancel, Delete, and Summary Reporting.
"""

from datetime import date, datetime


# ==============================================================================
# DATA STRUCTURE: In-Memory Storage for Meetings
# Each meeting is stored as a dictionary within the meeting_list list.
# ==============================================================================
meeting_list = [
    {
        "meeting_id": "M001",
        "student_id": "S001",
        "student_name": "Rahul Sharma",
        "mentor_id": "MTR01",
        "mentor_name": "Dr. Ramesh Kumar",
        "date": "2026-11-20",
        "time": "10:30",
        "mode": "In-Person",
        "agenda": "Semester 1 Academic Review & Attendance Check",
        "notes": "Student showed steady progress in Python. Advised to practice more data structures.",
        "status": "Completed"
    },
    {
        "meeting_id": "M002",
        "student_id": "S002",
        "student_name": "Priya Patel",
        "mentor_id": "MTR02",
        "mentor_name": "Prof. Anitha Rao",
        "date": "2026-11-28",
        "time": "14:00",
        "mode": "Online",
        "agenda": "Minor Project Topic Discussion & Scope Finalization",
        "notes": "Reviewed initial synopsis. Student to submit revised problem statement.",
        "status": "Scheduled"
    },
    {
        "meeting_id": "M003",
        "student_id": "S003",
        "student_name": "Arjun Verma",
        "mentor_id": "MTR01",
        "mentor_name": "Dr. Ramesh Kumar",
        "date": "2026-11-30",
        "time": "11:15",
        "mode": "In-Person",
        "agenda": "Career Guidance & Internship Preparation",
        "notes": "Discussed skill building for upcoming campus placements.",
        "status": "Scheduled"
    }
]


# ==============================================================================
# HELPER FUNCTIONS: Input Validation & Formatting
# ==============================================================================

def get_valid_input(message):
    """Prompt the user until non-empty input is received."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("[!] Input cannot be empty. Please try again.")


def get_valid_date(message):
    """Prompt the user for a valid date in YYYY-MM-DD format."""
    while True:
        date_str = input(message).strip()
        try:
            parsed_date = date.fromisoformat(date_str)
            return str(parsed_date)
        except ValueError:
            print("[!] Invalid date format! Please enter date in YYYY-MM-DD format (e.g., 2026-12-05).")


def get_valid_time(message):
    """Prompt the user for a valid time in HH:MM (24-hour) format."""
    while True:
        time_str = input(message).strip()
        try:
            parsed_time = datetime.strptime(time_str, "%H:%M")
            return parsed_time.strftime("%H:%M")
        except ValueError:
            print("[!] Invalid time format! Please enter time in 24-hour HH:MM format (e.g., 14:30).")


def generate_meeting_id():
    """Generate a unique meeting ID based on existing records."""
    max_num = 0
    for meeting in meeting_list:
        mid = meeting.get("meeting_id", "")
        if mid.startswith("M") and mid[1:].isdigit():
            num = int(mid[1:])
            if num > max_num:
                max_num = num
    return f"M{str(max_num + 1).zfill(3)}"


def display_meeting_card(meeting):
    """Display a single meeting's details in a clean structured format."""
    print("-" * 55)
    print(f"  Meeting ID   : {meeting['meeting_id']}")
    print(f"  Student      : {meeting['student_name']} (ID: {meeting['student_id']})")
    print(f"  Mentor       : {meeting['mentor_name']} (ID: {meeting['mentor_id']})")
    print(f"  Date & Time  : {meeting['date']} at {meeting['time']}")
    print(f"  Mode         : {meeting['mode']}")
    print(f"  Agenda       : {meeting['agenda']}")
    print(f"  Notes/Minutes: {meeting['notes']}")
    print(f"  Status       : {meeting['status']}")
    print("-" * 55)


# ==============================================================================
# CORE OPERATION 1: Schedule / Add a New Meeting
# ==============================================================================

def schedule_meeting():
    """
    Core Operation 1: Schedule a new mentoring meeting.
    Collects student, mentor, date, time, mode, agenda, and creates the record.
    """
    print("\n" + "=" * 55)
    print("            SCHEDULE A NEW MEETING")
    print("=" * 55)

    meeting_id = generate_meeting_id()
    print(f"Generated Meeting ID : {meeting_id}")

    student_id = get_valid_input("Enter Student ID (e.g., S001): ")
    student_name = get_valid_input("Enter Student Name: ")
    mentor_id = get_valid_input("Enter Mentor ID (e.g., MTR01): ")
    mentor_name = get_valid_input("Enter Mentor Name: ")
    meeting_date = get_valid_date("Enter Meeting Date (YYYY-MM-DD): ")
    meeting_time = get_valid_time("Enter Meeting Time (HH:MM in 24hr): ")

    print("\nSelect Meeting Mode:")
    print("1. In-Person")
    print("2. Online")
    mode_choice = input("Enter choice (1 or 2): ").strip()
    while mode_choice not in ["1", "2"]:
        print("[!] Invalid choice. Please enter 1 or 2.")
        mode_choice = input("Enter choice (1 or 2): ").strip()
    mode = "In-Person" if mode_choice == "1" else "Online"

    agenda = get_valid_input("Enter Meeting Agenda / Purpose: ")
    notes_input = input("Enter Initial Discussion Notes (Press Enter to leave blank): ").strip()
    notes = notes_input if notes_input else "Pending meeting discussion."

    meeting = {
        "meeting_id": meeting_id,
        "student_id": student_id,
        "student_name": student_name,
        "mentor_id": mentor_id,
        "mentor_name": mentor_name,
        "date": meeting_date,
        "time": meeting_time,
        "mode": mode,
        "agenda": agenda,
        "notes": notes,
        "status": "Scheduled"
    }

    meeting_list.append(meeting)
    print("\n[SUCCESS] Meeting scheduled successfully!")
    print(f"[INFO] Meeting ID: {meeting_id} | Date: {meeting_date} | Time: {meeting_time}")


# ==============================================================================
# CORE OPERATION 2: View and Search Meetings
# ==============================================================================

def view_all_meetings():
    """View all scheduled, completed, and cancelled meetings."""
    print("\n" + "=" * 55)
    print("              ALL MENTORING MEETINGS")
    print("=" * 55)

    if not meeting_list:
        print("[!] No meetings found in the records.")
        return

    print(f"Total Records: {len(meeting_list)}\n")
    for meeting in meeting_list:
        display_meeting_card(meeting)


def search_meetings():
    """
    Core Operation 2: Search and query meetings by criteria.
    Options: Student ID, Mentor ID, Meeting ID, or Status.
    """
    print("\n" + "=" * 55)
    print("                 SEARCH MEETINGS")
    print("=" * 55)

    if not meeting_list:
        print("[!] No meetings available to search.")
        return

    print("1. Search by Student ID")
    print("2. Search by Mentor ID")
    print("3. Search by Meeting ID")
    print("4. Filter by Status (Scheduled / Completed / Cancelled)")
    choice = input("Enter search option (1-4): ").strip()

    if choice == "1":
        sid = get_valid_input("Enter Student ID to search: ").upper()
        found = False
        print(f"\n--- Meetings for Student ID: {sid} ---")
        for m in meeting_list:
            if m["student_id"].upper() == sid:
                display_meeting_card(m)
                found = True
        if not found:
            print(f"[!] No meetings found for Student ID: {sid}")

    elif choice == "2":
        mid = get_valid_input("Enter Mentor ID to search: ").upper()
        found = False
        print(f"\n--- Meetings conducted by Mentor ID: {mid} ---")
        for m in meeting_list:
            if m["mentor_id"].upper() == mid:
                display_meeting_card(m)
                found = True
        if not found:
            print(f"[!] No meetings found for Mentor ID: {mid}")

    elif choice == "3":
        mid = get_valid_input("Enter Meeting ID to search (e.g., M001): ").upper()
        found = False
        for m in meeting_list:
            if m["meeting_id"].upper() == mid:
                display_meeting_card(m)
                found = True
                break
        if not found:
            print(f"[!] Meeting with ID {mid} was not found.")

    elif choice == "4":
        print("\nSelect Status:")
        print("1. Scheduled")
        print("2. Completed")
        print("3. Cancelled")
        st_choice = input("Enter choice (1-3): ").strip()
        status_map = {"1": "Scheduled", "2": "Completed", "3": "Cancelled"}
        selected_status = status_map.get(st_choice)

        if not selected_status:
            print("[!] Invalid status selection.")
            return

        found = False
        print(f"\n--- {selected_status.upper()} MEETINGS ---")
        for m in meeting_list:
            if m["status"] == selected_status:
                display_meeting_card(m)
                found = True
        if not found:
            print(f"[!] No {selected_status} meetings found.")

    else:
        print("[!] Invalid option selected.")


# ==============================================================================
# CORE OPERATION 3: Update Meeting Details, Record Minutes, and Status
# ==============================================================================

def update_meeting():
    """
    Core Operation 3 (Part A): Update existing meeting information.
    Allows rescheduling (date/time), changing agenda, or updating notes.
    """
    print("\n" + "=" * 55)
    print("             UPDATE / RESCHEDULE MEETING")
    print("=" * 55)

    if not meeting_list:
        print("[!] No meetings available to update.")
        return

    meeting_id = get_valid_input("Enter Meeting ID to update (e.g., M001): ").upper()

    target = None
    for m in meeting_list:
        if m["meeting_id"].upper() == meeting_id:
            target = m
            break

    if not target:
        print(f"[!] Meeting ID {meeting_id} not found.")
        return

    print("\nCurrent Meeting Details:")
    display_meeting_card(target)

    print("\nSelect field to update:")
    print("1. Reschedule (Date & Time)")
    print("2. Update Agenda / Purpose")
    print("3. Update Mode (In-Person / Online)")
    print("4. Add / Update Discussion Notes")
    print("5. Cancel updating")
    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        new_date = get_valid_date("Enter new Date (YYYY-MM-DD): ")
        new_time = get_valid_time("Enter new Time (HH:MM): ")
        target["date"] = new_date
        target["time"] = new_time
        print("\n[SUCCESS] Meeting rescheduled successfully!")

    elif choice == "2":
        new_agenda = get_valid_input("Enter new Agenda / Purpose: ")
        target["agenda"] = new_agenda
        print("\n[SUCCESS] Agenda updated successfully!")

    elif choice == "3":
        print("1. In-Person\n2. Online")
        m_ch = input("Enter choice (1 or 2): ").strip()
        if m_ch in ["1", "2"]:
            target["mode"] = "In-Person" if m_ch == "1" else "Online"
            print("\n[SUCCESS] Meeting mode updated successfully!")
        else:
            print("[!] Invalid choice. Mode was not changed.")

    elif choice == "4":
        print(f"Current Notes: {target['notes']}")
        print("1. Replace Notes")
        print("2. Append to Notes")
        n_ch = input("Enter choice (1 or 2): ").strip()
        if n_ch == "1":
            new_notes = get_valid_input("Enter new notes: ")
            target["notes"] = new_notes
            print("\n[SUCCESS] Notes updated successfully!")
        elif n_ch == "2":
            append_notes = get_valid_input("Enter notes to append: ")
            target["notes"] += " | " + append_notes
            print("\n[SUCCESS] Notes appended successfully!")
        else:
            print("[!] Invalid option. Notes unchanged.")

    elif choice == "5":
        print("\nUpdate cancelled.")
    else:
        print("[!] Invalid choice.")


def complete_meeting():
    """
    Core Operation 3 (Part B): Mark meeting as Completed and record minutes/outcomes.
    """
    print("\n" + "=" * 55)
    print("      RECORD MEETING OUTCOMES & MARK COMPLETED")
    print("=" * 55)

    if not meeting_list:
        print("[!] No meetings found.")
        return

    meeting_id = get_valid_input("Enter Meeting ID to complete (e.g., M001): ").upper()

    target = None
    for m in meeting_list:
        if m["meeting_id"].upper() == meeting_id:
            target = m
            break

    if not target:
        print(f"[!] Meeting ID {meeting_id} not found.")
        return

    if target["status"] == "Completed":
        print(f"[!] Meeting {meeting_id} is already marked as Completed.")
        return

    if target["status"] == "Cancelled":
        print(f"[!] Meeting {meeting_id} is Cancelled and cannot be marked completed directly.")
        reopen = input("Do you want to re-open this meeting? (y/n): ").strip().lower()
        if reopen != "y":
            return

    print("\nMeeting to be Completed:")
    display_meeting_card(target)

    outcomes = get_valid_input("Enter Meeting Minutes / Key Outcomes / Action Items agreed upon: ")
    if target["notes"] and target["notes"] != "Pending meeting discussion.":
        target["notes"] += f" | Concluded: {outcomes}"
    else:
        target["notes"] = outcomes

    target["status"] = "Completed"
    print(f"\n[SUCCESS] Meeting {meeting_id} marked as COMPLETED!")
    print(f"[INFO] Final notes recorded: {target['notes']}")


# ==============================================================================
# ADDITIONAL OPERATIONS: Cancel, Delete, and Summary Report
# ==============================================================================

def cancel_meeting():
    """Cancel a scheduled meeting with an optional reason."""
    print("\n" + "=" * 55)
    print("                 CANCEL MEETING")
    print("=" * 55)

    if not meeting_list:
        print("[!] No meetings found.")
        return

    meeting_id = get_valid_input("Enter Meeting ID to cancel: ").upper()

    target = None
    for m in meeting_list:
        if m["meeting_id"].upper() == meeting_id:
            target = m
            break

    if not target:
        print(f"[!] Meeting ID {meeting_id} not found.")
        return

    if target["status"] == "Cancelled":
        print(f"[!] Meeting {meeting_id} is already cancelled.")
        return

    reason = input("Enter reason for cancellation (Press Enter to skip): ").strip()
    if reason:
        target["notes"] += f" | Cancelled reason: {reason}"

    target["status"] = "Cancelled"
    print(f"\n[SUCCESS] Meeting {meeting_id} has been marked as CANCELLED.")


def delete_meeting():
    """Delete a meeting record from storage with confirmation."""
    print("\n" + "=" * 55)
    print("                 DELETE MEETING")
    print("=" * 55)

    if not meeting_list:
        print("[!] No meetings available to delete.")
        return

    meeting_id = get_valid_input("Enter Meeting ID to delete: ").upper()

    target_index = -1
    for index, m in enumerate(meeting_list):
        if m["meeting_id"].upper() == meeting_id:
            target_index = index
            break

    if target_index == -1:
        print(f"[!] Meeting ID {meeting_id} not found.")
        return

    display_meeting_card(meeting_list[target_index])
    confirm = input(f"Are you sure you want to permanently delete {meeting_id}? (y/n): ").strip().lower()
    if confirm == "y":
        deleted = meeting_list.pop(target_index)
        print(f"\n[SUCCESS] Meeting {deleted['meeting_id']} deleted successfully.")
    else:
        print("\nDeletion cancelled.")


def meetings_report():
    """
    Display a summary analytics report of all mentoring meetings.
    Calculates total meetings, breakdown by status, and completion rate.
    """
    print("\n" + "=" * 55)
    print("            MEETINGS SUMMARY REPORT")
    print("=" * 55)

    total = len(meeting_list)
    if total == 0:
        print("[!] No meeting records available to generate report.")
        return

    scheduled_count = 0
    completed_count = 0
    cancelled_count = 0

    students_set = set()
    mentors_set = set()

    for m in meeting_list:
        status = m.get("status", "")
        if status == "Scheduled":
            scheduled_count += 1
        elif status == "Completed":
            completed_count += 1
        elif status == "Cancelled":
            cancelled_count += 1

        students_set.add(m.get("student_id"))
        mentors_set.add(m.get("mentor_id"))

    completion_rate = (completed_count / total) * 100 if total > 0 else 0.0

    print(f"Total Meetings Tracked : {total}")
    print(f"  - Scheduled Meetings : {scheduled_count}")
    print(f"  - Completed Meetings : {completed_count}")
    print(f"  - Cancelled Meetings : {cancelled_count}")
    print("-" * 55)
    print(f"Unique Students Met    : {len(students_set)}")
    print(f"Unique Mentors Involved: {len(mentors_set)}")
    print(f"Overall Completion Rate: {completion_rate:.1f}%")
    print("=" * 55)


# ==============================================================================
# MENU-DRIVEN INTERFACE: meeting_menu()
# ==============================================================================

def meeting_menu():
    """
    Main menu loop for the Meetings Management submodule.
    Integrates all functions in a clear, interactive procedural menu.
    """
    while True:
        print("\n" + "=" * 55)
        print("       STUDENT MENTORING TRACKER - MEETINGS MENU")
        print("=" * 55)
        print("  1. Schedule a New Meeting        (Add / Create)")
        print("  2. View All Meetings             (Display All)")
        print("  3. Search Meetings               (Query / Filter)")
        print("  4. Update Meeting Details        (Reschedule / Edit)")
        print("  5. Record Outcomes & Complete    (Record Minutes)")
        print("  6. Cancel a Meeting              (Status Update)")
        print("  7. Delete a Meeting Record       (Remove)")
        print("  8. View Meetings Summary Report  (Analytics)")
        print("  9. Exit / Back to Main Menu")
        print("=" * 55)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            schedule_meeting()
        elif choice == "2":
            view_all_meetings()
        elif choice == "3":
            search_meetings()
        elif choice == "4":
            update_meeting()
        elif choice == "5":
            complete_meeting()
        elif choice == "6":
            cancel_meeting()
        elif choice == "7":
            delete_meeting()
        elif choice == "8":
            meetings_report()
        elif choice == "9":
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid option! Please enter a number between 1 and 9.")


# Direct execution entry point
if __name__ == "__main__":
    meeting_menu()
