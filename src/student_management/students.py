"""
Module 1: Student and Mentor Management
Author: Vikas S (Member 1)
Description:
    Maintains basic details required to identify students and mentors,
    and connects students with their appropriate assigned mentor.
"""

from data.sample_data import students, mentors


def get_mentor_by_id(mentor_id):
    """Helper: find mentor dictionary by mentor_id."""
    for mentor in mentors:
        if mentor["mentor_id"] == mentor_id:
            return mentor
    return None


def get_student_by_id(student_id):
    """Helper: find student dictionary by student_id."""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def format_mentor_info(mentor_id):
    """Helper: return readable mentor label or 'Not Assigned'."""
    if not mentor_id:
        return "Not Assigned"
    mentor = get_mentor_by_id(mentor_id)
    return f"{mentor_id} - {mentor['name']}" if mentor else mentor_id


def print_student_details(student, indent=""):
    """Helper: print a student's details with optional indentation."""
    mentor_info = format_mentor_info(student["mentor_id"])
    print(f"{indent}Student ID      : {student['student_id']}")
    print(f"{indent}Name            : {student['name']}")
    print(f"{indent}Department      : {student['department']}")
    print(f"{indent}Year of Study   : Year {student['year']}")
    print(f"{indent}Contact         : {student['contact']}")
    print(f"{indent}Assigned Mentor : {mentor_info}")
    print("-" * 40)


def print_available_mentors():
    """Helper: list all available mentors in short form."""
    print("\nAvailable Mentors:")
    for mentor in mentors:
        print(f"  {mentor['mentor_id']} - {mentor['name']} ({mentor['department']})")


# -------------------------------------------------------------
# Student Operations
# -------------------------------------------------------------

def add_student():
    """Add a new student record."""
    print("\n" + "=" * 40)
    print("           ADD STUDENT RECORD")
    print("=" * 40)

    student_id = input("Enter Student ID (e.g. S104): ").strip().upper()
    if not student_id:
        print("[!] Student ID cannot be empty.")
        return

    if get_student_by_id(student_id):
        print(f"[!] Student ID '{student_id}' already exists!")
        return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("[!] Student name cannot be empty.")
        return

    department = input("Enter Department (e.g. MCA, BCA): ").strip().upper()

    while True:
        year_input = input("Enter Year of Study (1-5): ").strip()
        if year_input.isdigit() and 1 <= int(year_input) <= 5:
            year = int(year_input)
            break
        print("[!] Invalid year. Enter a number between 1 and 5.")

    contact = input("Enter Contact Number: ").strip()

    mentor_id = None
    if mentors:
        print_available_mentors()
        if input("Assign a mentor now? (y/n): ").strip().lower() == "y":
            chosen_mentor = input("Enter Mentor ID: ").strip().upper()
            if get_mentor_by_id(chosen_mentor):
                mentor_id = chosen_mentor
                print(f"[✔] Assigned to Mentor {mentor_id}.")
            else:
                print("[!] Mentor ID not found. Student registered without mentor.")

    students.append({
        "student_id": student_id,
        "name": name,
        "department": department,
        "year": year,
        "contact": contact,
        "mentor_id": mentor_id,
    })
    print(f"\n[✔] Student '{name}' (ID: {student_id}) added successfully!")


def view_students():
    """Display the list of all students."""
    print("\n" + "=" * 40)
    print("           LIST OF ALL STUDENTS")
    print("=" * 40)

    if not students:
        print("[!] No students registered yet.")
        return

    for idx, student in enumerate(students, start=1):
        print(f"\nStudent #{idx}")
        print_student_details(student, indent="  ")


def search_student():
    """Search for a student using Student ID."""
    print("\n" + "=" * 40)
    print("             SEARCH STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID to search: ").strip().upper()
    student = get_student_by_id(student_id)

    if not student:
        print(f"[!] No student found with ID: {student_id}")
        return

    print("\n" + "-" * 40)
    print_student_details(student)


def update_student():
    """Update student details."""
    print("\n" + "=" * 40)
    print("         UPDATE STUDENT DETAILS")
    print("=" * 40)

    student_id = input("Enter Student ID to update: ").strip().upper()
    student = get_student_by_id(student_id)

    if not student:
        print(f"[!] No student found with ID: {student_id}")
        return

    print(f"\nUpdating details for {student['name']} ({student_id}).")
    print("Press Enter without typing to keep current value.")

    new_name = input(f"New Name [{student['name']}]: ").strip()
    if new_name:
        student["name"] = new_name

    new_dept = input(f"New Department [{student['department']}]: ").strip().upper()
    if new_dept:
        student["department"] = new_dept

    new_year = input(f"New Year (1-5) [{student['year']}]: ").strip()
    if new_year.isdigit() and 1 <= int(new_year) <= 5:
        student["year"] = int(new_year)

    new_contact = input(f"New Contact [{student['contact']}]: ").strip()
    if new_contact:
        student["contact"] = new_contact

    print("\n[✔] Student details updated successfully!")


def delete_student():
    """Delete a student record."""
    print("\n" + "=" * 40)
    print("            DELETE STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID to delete: ").strip().upper()
    student = get_student_by_id(student_id)

    if not student:
        print(f"[!] No student found with ID: {student_id}")
        return

    print(f"\nStudent Found: {student['name']} (ID: {student['student_id']})")
    confirm = input("Are you sure you want to delete this student? (y/n): ").strip().lower()

    if confirm == "y":
        students.remove(student)
        print(f"\n[✔] Student record '{student_id}' deleted successfully.")
    else:
        print("\nDeletion cancelled.")


# -------------------------------------------------------------
# Mentor Operations
# -------------------------------------------------------------

def add_mentor():
    """Add a new mentor record."""
    print("\n" + "=" * 40)
    print("            ADD MENTOR RECORD")
    print("=" * 40)

    mentor_id = input("Enter Mentor ID (e.g. M103): ").strip().upper()
    if not mentor_id:
        print("[!] Mentor ID cannot be empty.")
        return

    if get_mentor_by_id(mentor_id):
        print(f"[!] Mentor ID '{mentor_id}' already exists!")
        return

    name = input("Enter Mentor Name: ").strip()
    if not name:
        print("[!] Mentor name cannot be empty.")
        return

    department = input("Enter Department: ").strip().upper()
    contact = input("Enter Contact Number: ").strip()

    mentors.append({
        "mentor_id": mentor_id,
        "name": name,
        "department": department,
        "contact": contact,
    })
    print(f"\n[✔] Mentor '{name}' (ID: {mentor_id}) added successfully!")


def view_mentors():
    """Display all registered mentors."""
    print("\n" + "=" * 40)
    print("           LIST OF ALL MENTORS")
    print("=" * 40)

    if not mentors:
        print("[!] No mentors registered yet.")
        return

    for idx, mentor in enumerate(mentors, start=1):
        mentees = [s["name"] for s in students if s.get("mentor_id") == mentor["mentor_id"]]
        mentee_str = ", ".join(mentees) if mentees else "None assigned"

        print(f"\nMentor #{idx}")
        print(f"  Mentor ID   : {mentor['mentor_id']}")
        print(f"  Name        : {mentor['name']}")
        print(f"  Department  : {mentor['department']}")
        print(f"  Contact     : {mentor['contact']}")
        print(f"  Mentees     : {mentee_str}")
        print("-" * 40)


def assign_mentor():
    """Assign an existing mentor to an existing student."""
    print("\n" + "=" * 40)
    print("         ASSIGN MENTOR TO STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID: ").strip().upper()
    student = get_student_by_id(student_id)
    if not student:
        print(f"[!] Student ID '{student_id}' does not exist.")
        return

    print(f"Selected Student: {student['name']} (Current Mentor: {student.get('mentor_id') or 'None'})")
    print_available_mentors()

    mentor_id = input("Enter Mentor ID to assign: ").strip().upper()
    mentor = get_mentor_by_id(mentor_id)
    if not mentor:
        print(f"[!] Mentor ID '{mentor_id}' does not exist.")
        return

    student["mentor_id"] = mentor_id
    print(f"\n[✔] Mentor {mentor['name']} ({mentor_id}) successfully assigned to student {student['name']} ({student_id})!")


# -------------------------------------------------------------
# Module Submenu (called by main.py)
# -------------------------------------------------------------

def student_mentor_menu():
    """Menu loop for Student and Mentor Management."""
    while True:
        print("\n" + "=" * 40)
        print("     STUDENT & MENTOR MANAGEMENT")
        print("=" * 40)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Add Mentor")
        print("7. View All Mentors")
        print("8. Assign Mentor to Student")
        print("9. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            add_mentor()
        elif choice == "7":
            view_mentors()
        elif choice == "8":
            assign_mentor()
        elif choice == "9":
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid choice! Please select 1 to 9.")
