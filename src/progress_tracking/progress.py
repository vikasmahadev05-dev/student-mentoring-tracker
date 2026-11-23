# In-memory storage for progress records
# Each record is stored as a dictionary inside this list.
progress_records = [
    {
        "student_id": "101",
        "student_name": "Rahul",
        "task": "Python Assignment 1",
        "description": "Completed basic loops",
        "status": "Completed",
        "remarks": "Good performance"
    },
    {
        "student_id": "101",
        "student_name": "Rahul",
        "task": "Data Structures Basics",
        "description": "Lists and Dictionaries practice",
        "status": "In Progress",
        "remarks": "Working on exercises"
    },
    {
        "student_id": "102",
        "student_name": "Arjun",
        "task": "Database Assignment",
        "description": "ER diagram and SQL queries",
        "status": "Pending",
        "remarks": "Needs improvement"
    }
]


def add_progress():
    """
    Function 1: Add a new progress record.
    Collects student details and task status, then appends to progress_records.
    """
    print("\n" + "=" * 40)
    print("         ADD PROGRESS RECORD")
    print("=" * 40)

    # Validate Student ID (Cannot be empty)
    student_id = input("Enter Student ID: ").strip()
    while not student_id:
        print("[!] Student ID cannot be empty. Please enter a valid ID.")
        student_id = input("Enter Student ID: ").strip()

    student_name = input("Enter Student Name: ").strip()
    while not student_name:
        print("[!] Student Name cannot be empty.")
        student_name = input("Enter Student Name: ").strip()

    task = input("Enter Activity / Task Name: ").strip()
    while not task:
        print("[!] Task name cannot be empty.")
        task = input("Enter Activity / Task Name: ").strip()

    description = input("Enter Task Description: ").strip()

    # Status Selection with validation
    print("\nSelect Task Status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")

    status_choice = input("Enter choice (1-3): ").strip()
    while status_choice not in ["1", "2", "3"]:
        print("[!] Invalid choice. Please select 1, 2, or 3.")
        status_choice = input("Enter choice (1-3): ").strip()

    if status_choice == "1":
        status = "Pending"
    elif status_choice == "2":
        status = "In Progress"
    else:
        status = "Completed"

    remarks = input("Enter Remarks (e.g., Good performance): ").strip()

    # Create the record as a dictionary
    record = {
        "student_id": student_id,
        "student_name": student_name,
        "task": task,
        "description": description,
        "status": status,
        "remarks": remarks
    }

    # Append to the records list
    progress_records.append(record)
    print("\n[✔] Progress record added successfully!")


def view_progress():
    """
    Function 2: View progress records.
    Allows viewing all records or searching records by Student ID.
    """
    print("\n" + "=" * 40)
    print("        VIEW PROGRESS RECORDS")
    print("=" * 40)

    if not progress_records:
        print("[!] No progress records found.")
        return

    print("1. View All Records")
    print("2. Search Records by Student ID")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        print("\n" + "-" * 40)
        print("          ALL PROGRESS RECORDS")
        print("-" * 40)
        for index, record in enumerate(progress_records, start=1):
            print(f"Record #{index}")
            print(f"  Student ID   : {record['student_id']}")
            print(f"  Student Name : {record['student_name']}")
            print(f"  Task         : {record['task']}")
            print(f"  Description  : {record['description']}")
            print(f"  Status       : {record['status']}")
            print(f"  Remarks      : {record['remarks']}")
            print("-" * 40)

    elif choice == "2":
        search_id = input("\nEnter Student ID to search: ").strip()
        matched = []
        for record in progress_records:
            if record["student_id"] == search_id:
                matched.append(record)

        if not matched:
            print(f"[!] No records found for Student ID: {search_id}")
        else:
            print("\n" + "-" * 40)
            print(f"     RECORDS FOR STUDENT ID: {search_id}")
            print("-" * 40)
            for index, record in enumerate(matched, start=1):
                print(f"Task #{index}")
                print(f"  Student Name : {record['student_name']}")
                print(f"  Task         : {record['task']}")
                print(f"  Description  : {record['description']}")
                print(f"  Status       : {record['status']}")
                print(f"  Remarks      : {record['remarks']}")
                print("-" * 40)
    else:
        print("[!] Invalid option. Returning to menu.")


def update_progress():
    """
    Function 3: Update existing progress records.
    Locates record by Student ID and allows changing status and remarks.
    """
    print("\n" + "=" * 40)
    print("          UPDATE PROGRESS")
    print("=" * 40)

    if not progress_records:
        print("[!] No progress records found to update.")
        return

    student_id = input("Enter Student ID: ").strip()

    # Find all records for this student
    student_tasks = []
    for record in progress_records:
        if record["student_id"] == student_id:
            student_tasks.append(record)

    if not student_tasks:
        print(f"[!] No records found for Student ID: {student_id}")
        return

    # Display available tasks for this student
    print(f"\nTasks found for Student {student_tasks[0]['student_name']} (ID: {student_id}):")
    for idx, rec in enumerate(student_tasks, start=1):
        print(f"{idx}. Task: {rec['task']} | Current Status: {rec['status']}")

    task_choice = input(f"\nSelect task to update (1-{len(student_tasks)}): ").strip()
    if not task_choice.isdigit() or int(task_choice) < 1 or int(task_choice) > len(student_tasks):
        print("[!] Invalid task selection.")
        return

    selected_record = student_tasks[int(task_choice) - 1]

    # Select new status
    print("\nSelect New Status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")

    new_status_choice = input("Select new status (1-3): ").strip()
    while new_status_choice not in ["1", "2", "3"]:
        print("[!] Invalid choice. Please choose 1, 2, or 3.")
        new_status_choice = input("Select new status (1-3): ").strip()

    if new_status_choice == "1":
        selected_record["status"] = "Pending"
    elif new_status_choice == "2":
        selected_record["status"] = "In Progress"
    else:
        selected_record["status"] = "Completed"

    # Optional update for remarks
    update_rem = input("\nDo you want to update remarks? (y/n): ").strip().lower()
    if update_rem == "y":
        new_remarks = input("Enter new remarks: ").strip()
        selected_record["remarks"] = new_remarks

    print("\n[✔] Progress updated successfully!")


def delete_progress():
    """
    Function 4: Delete a progress record.
    Finds a record by Student ID and Task name, asks confirmation, then removes it.
    """
    print("\n" + "=" * 40)
    print("       DELETE PROGRESS RECORD")
    print("=" * 40)

    if not progress_records:
        print("[!] No records available to delete.")
        return

    student_id = input("Enter Student ID: ").strip()
    task_name = input("Enter Task Name: ").strip()

    record_to_delete = None
    for record in progress_records:
        if record["student_id"] == student_id and record["task"].lower() == task_name.lower():
            record_to_delete = record
            break

    if not record_to_delete:
        print(f"[!] No record found matching Student ID '{student_id}' and Task '{task_name}'.")
        return

    # Confirmation prompt
    print("\nRecord found:")
    print(f"  Student : {record_to_delete['student_name']} (ID: {record_to_delete['student_id']})")
    print(f"  Task    : {record_to_delete['task']}")
    print(f"  Status  : {record_to_delete['status']}")

    print("\nAre you sure you want to delete?")
    print("1. Yes")
    print("2. No")
    confirm = input("Enter choice (1 or 2): ").strip()

    if confirm == "1":
        progress_records.remove(record_to_delete)
        print("\n[✔] Record deleted successfully!")
    else:
        print("\nDeletion cancelled.")


def progress_report():
    """
    Function 5: View Progress Report.
    Calculates completed, in progress, pending tasks, and overall progress percentage.
    Formula: Progress = (Completed Tasks / Total Tasks) * 100
    """
    print("\n" + "=" * 40)
    print("       STUDENT PROGRESS REPORT")
    print("=" * 40)

    if not progress_records:
        print("[!] No records available to generate report.")
        return

    student_id = input("Enter Student ID: ").strip()

    # Filter records for the specified student
    student_records = []
    for record in progress_records:
        if record["student_id"] == student_id:
            student_records.append(record)

    if not student_records:
        print(f"[!] No tasks found for Student ID: {student_id}")
        return

    student_name = student_records[0]["student_name"]
    total_tasks = len(student_records)
    completed_tasks = 0
    in_progress_tasks = 0
    pending_tasks = 0

    # Count tasks by status using a loop and conditionals
    for record in student_records:
        if record["status"] == "Completed":
            completed_tasks += 1
        elif record["status"] == "In Progress":
            in_progress_tasks += 1
        elif record["status"] == "Pending":
            pending_tasks += 1

    # Calculate overall progress percentage
    if total_tasks > 0:
        progress_percentage = (completed_tasks / total_tasks) * 100
    else:
        progress_percentage = 0.0

    # Display the report
    print("\n" + "-" * 40)
    print("        STUDENT PROGRESS REPORT")
    print("-" * 40)
    print(f"Student ID        : {student_id}")
    print(f"Student Name      : {student_name}")
    print()
    print(f"Total Tasks       : {total_tasks}")
    print(f"Completed Tasks   : {completed_tasks}")
    print(f"In Progress Tasks : {in_progress_tasks}")
    print(f"Pending Tasks     : {pending_tasks}")
    print()
    print(f"Overall Progress  : {progress_percentage:.1f}%")
    print("-" * 40)


def tracking_menu():
    """
    Function 6: Main Tracking & Progress Menu.
    Provides a nested menu-driven interface to call all module functions.
    """
    while True:
        print("\n" + "=" * 40)
        print("       TRACKING & PROGRESS MENU")
        print("=" * 40)
        print("1. Add Progress Record")
        print("2. View Progress Records")
        print("3. Update Progress")
        print("4. Delete Progress Record")
        print("5. View Progress Report")
        print("6. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_progress()
        elif choice == "2":
            view_progress()
        elif choice == "3":
            update_progress()
        elif choice == "4":
            delete_progress()
        elif choice == "5":
            progress_report()
        elif choice == "6":
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 6.")


# Direct execution entry point
if __name__ == "__main__":
    tracking_menu()
