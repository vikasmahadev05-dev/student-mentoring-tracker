"""
Student Mentoring Tracker - Main Application Entry Point
MAIN MENU (main.py)
MCA Minor Project - Phase 1: Procedural Programming

Submodules:
  1. Student & Mentor Management (Member 1 - students.py)
  2. Meeting Management          (Member 2 - meetings.py)
  3. Action Item Management      (Member 3 - actions.py)
  4. Follow-up & Progress        (Member 4 - progress.py)
"""

import sys
from pathlib import Path

# Add project root and src directory to sys.path
src_dir = Path(__file__).resolve().parent
root_dir = src_dir.parent
for p in [str(root_dir), str(src_dir)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from student_management.students import student_mentor_menu
from action_management.actions import action_menu
from progress_tracking.progress import progress_menu

# Meeting Management (Member 2)
try:
    from meeting_management.meetings import meeting_menu
except (ImportError, AttributeError):
    try:
        from src.meeting_management.meetings import meeting_menu
    except (ImportError, AttributeError):
        def meeting_menu():
            print("\n" + "=" * 40)
            print("          MEETING MANAGEMENT")
            print("=" * 40)
            print("[!] This module is currently being developed by Member 2.")
            print("Returning to Main Menu...")


def main_menu():
    """Main Menu loop calling each module's submenu."""
    while True:
        print("\n" + "=" * 40)
        print("     STUDENT MENTORING TRACKER")
        print("       (Phase 1 Application)")
        print("=" * 40)
        print("1. Student & Mentor Management")
        print("2. Meeting Management")
        print("3. Action Item Management")
        print("4. Follow-up & Progress Tracking")
        print("5. Exit Application")
        print("=" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            student_mentor_menu()
        elif choice == "2":
            meeting_menu()
        elif choice == "3":
            action_menu()
        elif choice == "4":
            progress_menu()
        elif choice == "5":
            print("\nThank you for using Student Mentoring Tracker!")
            print("Session ended.")
            break
        else:
            print("[!] Invalid choice! Please select a number from 1 to 5.")


if __name__ == "__main__":
    main_menu()
