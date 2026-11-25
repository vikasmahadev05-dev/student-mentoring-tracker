"""
Student Mentoring Tracker - Main Application Entry Point
MCA Minor Project - Phase 1: Procedural Programming

Run this file to start the app:
    python main.py
"""

from src.student_management.students import student_mentor_menu
from src.meeting_management.meetings import meeting_menu
from src.action_management.actions import action_menu
from src.progress_tracking.progress import progress_menu


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
