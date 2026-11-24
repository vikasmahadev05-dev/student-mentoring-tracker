"""
Student Mentoring Tracker - Main Application Entry Point
MAIN MENU (main.py)
MCA Minor Project - Phase 1: Procedural Programming

Submodules:
  1. Student & Mentor     (Member 1 - students.py)
  2. Meetings             (Member 2 - meetings.py)
  3. Action Items         (Member 3 - actions.py)
  4. Follow-up & Progress (Member 4 - progress.py)
"""

import sys
import os

# Add parent directory to path so imports work from anywhere
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import module 2: meetings
try:
    from src.meeting_management import meetings
except ImportError:
    meetings = None


def open_students_menu():
    """Member 1: Student & Mentor submenu."""
    try:
        from src.student_management import students
        if hasattr(students, "student_menu"):
            students.student_menu()
        else:
            print("\n[INFO] Member 1 (Student & Mentor) module is currently under development.")
    except (ImportError, AttributeError):
        print("\n[INFO] Member 1 (Student & Mentor) module is currently under development.")


def open_meetings_menu():
    """Member 2: Meetings submenu."""
    if meetings and hasattr(meetings, "meeting_menu"):
        meetings.meeting_menu()
    else:
        print("\n[!] Meetings module could not be loaded.")


def open_actions_menu():
    """Member 3: Action Items submenu."""
    try:
        from src.action_management import actions
        if hasattr(actions, "actions_menu"):
            actions.actions_menu()
        elif hasattr(actions, "view_actions"):
            # Provide menu wrapper if member 3 hasn't wrapped it yet
            while True:
                print("\n" + "=" * 50)
                print("            ACTION ITEMS MENU")
                print("=" * 50)
                print("1. Create Action Item")
                print("2. View All Action Items")
                print("3. Search Action Items by Student ID")
                print("4. Update Action Item")
                print("5. Mark Action Item Completed")
                print("6. View Pending Action Items")
                print("7. View Completed Action Items")
                print("8. View Overdue Action Items")
                print("9. Back to Main Menu")
                print("=" * 50)
                ch = input("Enter choice (1-9): ").strip()
                if ch == "1":
                    actions.create_action()
                elif ch == "2":
                    actions.view_actions()
                elif ch == "3":
                    actions.search_actions()
                elif ch == "4":
                    actions.update_action()
                elif ch == "5":
                    actions.complete_action()
                elif ch == "6":
                    actions.view_pending_actions()
                elif ch == "7":
                    actions.view_completed_actions()
                elif ch == "8":
                    actions.get_overdue_actions()
                elif ch == "9":
                    break
                else:
                    print("[!] Invalid choice.")
        else:
            print("\n[INFO] Member 3 (Action Items) module is currently under development.")
    except (ImportError, AttributeError):
        print("\n[INFO] Member 3 (Action Items) module is currently under development.")


def open_progress_menu():
    """Member 4: Follow-up & Progress submenu."""
    try:
        from src.progress_tracking import progress
        if hasattr(progress, "tracking_menu"):
            progress.tracking_menu()
        else:
            print("\n[INFO] Member 4 (Follow-up & Progress) module is currently under development.")
    except (ImportError, AttributeError):
        print("\n[INFO] Member 4 (Follow-up & Progress) module is currently under development.")


def main_menu():
    """
    Main Menu for the Student Mentoring Tracker application.
    Coordinates between the 4 team members' modules.
    """
    while True:
        print("\n" + "=" * 60)
        print("              STUDENT MENTORING TRACKER")
        print("               MAIN MENU - Phase 1")
        print("=" * 60)
        print("  1. Student & Mentor       (Member 1 - students.py)")
        print("  2. Meetings               (Member 2 - meetings.py)")
        print("  3. Action Items           (Member 3 - actions.py)")
        print("  4. Follow-up & Progress   (Member 4 - progress.py)")
        print("  5. Exit")
        print("=" * 60)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            open_students_menu()
        elif choice == "2":
            open_meetings_menu()
        elif choice == "3":
            open_actions_menu()
        elif choice == "4":
            open_progress_menu()
        elif choice == "5":
            print("\nExiting Student Mentoring Tracker. Goodbye!")
            break
        else:
            print("[!] Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()
