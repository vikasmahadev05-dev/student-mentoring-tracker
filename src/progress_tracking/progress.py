"""
Module 4: Follow-up & Progress Tracking
Author: Vikas Mahadev (Member 4)
Description:
    Tracks overdue tasks, due-today follow-ups, student progress scorecards,
    at-risk students, and the overall cohort summary.
"""

from datetime import date
from data.sample_data import actions, students


# -------------------------------------------------------------
# Helper Functions
# -------------------------------------------------------------

def get_student(student_id):
    """Find and return a student dictionary by ID, or None if not found."""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def get_student_name(student_id):
    """Return the student's name if found, otherwise return their ID."""
    student = get_student(student_id)
    if student is not None:
        return student["name"]
    else:
        return student_id


def get_action_timeline_category(action):
    """
    Classify an action by its status and follow-up date.
    Returns: 'COMPLETED', 'OVERDUE', 'DUE_TODAY', 'UPCOMING', or 'PENDING'
    """
    if action["status"] == "Completed":
        return "COMPLETED"

    today = date.today()
    try:
        follow_up = date.fromisoformat(action["follow_up_date"])
    except (ValueError, KeyError):
        return "PENDING"

    if follow_up < today:
        return "OVERDUE"
    elif follow_up == today:
        return "DUE_TODAY"
    else:
        return "UPCOMING"


def summarize_actions(action_items):
    """Count total, completed, pending, overdue, due-today tasks and %."""
    total = len(action_items)
    completed = 0
    pending = 0
    overdue = 0
    due_today = 0

    for action in action_items:
        category = get_action_timeline_category(action)
        if category == "COMPLETED":
            completed = completed + 1
        else:
            pending = pending + 1
            if category == "OVERDUE":
                overdue = overdue + 1
            elif category == "DUE_TODAY":
                due_today = due_today + 1

    if total > 0:
        percentage = (completed / total) * 100
    else:
        percentage = 0.0

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
        "due_today": due_today,
        "percentage": percentage,
    }


# -------------------------------------------------------------
# 1. Daily Follow-up Radar (Due Today & Overdue)
# -------------------------------------------------------------

def daily_follow_up_radar():
    """Show overdue tasks and tasks due for follow-up today."""
    today = date.today()
    print("\n" + "=" * 50)
    print("           DAILY FOLLOW-UP RADAR")
    print(f"           Today's Date: {today}")
    print("=" * 50)

    overdue_items = []
    due_today_items = []

    for action in actions:
        category = get_action_timeline_category(action)
        if category == "OVERDUE":
            overdue_items.append(action)
        elif category == "DUE_TODAY":
            due_today_items.append(action)

    # Section 1: Overdue tasks
    print("\n[!] OVERDUE ACTIONS (IMMEDIATE ATTENTION NEEDED):")
    print("-" * 50)
    if len(overdue_items) == 0:
        print("  [✔] None! All actions are on schedule.")
    else:
        number = 1
        for action in overdue_items:
            s_name = get_student_name(action["student_id"])
            follow_up = date.fromisoformat(action["follow_up_date"])
            days_late = (today - follow_up).days
            print(f"  {number}. [{action['action_id']}] {s_name} ({action['student_id']})")
            print(f"     Task      : {action['description']}")
            print(f"     Follow-up : {action['follow_up_date']} ({days_late} day(s) overdue!)")
            number = number + 1

    # Section 2: Tasks due today
    print("\n[★] ACTIONS DUE FOR FOLLOW-UP TODAY:")
    print("-" * 50)
    if len(due_today_items) == 0:
        print("  [i] No actions scheduled for follow-up today.")
    else:
        number = 1
        for action in due_today_items:
            s_name = get_student_name(action["student_id"])
            print(f"  {number}. [{action['action_id']}] {s_name} ({action['student_id']})")
            print(f"     Task      : {action['description']}")
            print(f"     Due Date  : {action['due_date']}")
            number = number + 1
    print("=" * 50)


# -------------------------------------------------------------
# 2. View Pending Actions by Timeline
# -------------------------------------------------------------

def view_pending_timeline():
    """Show all pending actions with days overdue or days remaining."""
    print("\n" + "=" * 50)
    print("       PENDING ACTIONS TIMELINE & DEADLINES")
    print("=" * 50)

    pending_actions = []
    for action in actions:
        if action["status"] == "Pending":
            pending_actions.append(action)

    if len(pending_actions) == 0:
        print("[!] No pending actions found in the system.")
        return

    today = date.today()
    number = 1
    for action in pending_actions:
        s_name = get_student_name(action["student_id"])
        category = get_action_timeline_category(action)

        try:
            follow_up = date.fromisoformat(action["follow_up_date"])
            diff = (follow_up - today).days
            if diff < 0:
                timeline_str = f"{abs(diff)} days OVERDUE"
            elif diff == 0:
                timeline_str = "DUE TODAY"
            else:
                timeline_str = f"Due in {diff} day(s)"
        except ValueError:
            timeline_str = "Date unavailable"

        print(f"\nTask #{number} - [{category}]")
        print(f"  Action ID      : {action['action_id']}")
        print(f"  Student        : {s_name} ({action['student_id']})")
        print(f"  Description    : {action['description']}")
        print(f"  Follow-up Date : {action['follow_up_date']} ({timeline_str})")
        print("-" * 50)
        number = number + 1


# -------------------------------------------------------------
# 3. View Completed Actions (Archive)
# -------------------------------------------------------------

def view_completed():
    """Show all completed action items."""
    print("\n" + "=" * 50)
    print("         COMPLETED ACTIONS (ARCHIVE)")
    print("=" * 50)

    completed_actions = []
    for action in actions:
        if action["status"] == "Completed":
            completed_actions.append(action)

    if len(completed_actions) == 0:
        print("[!] No completed actions recorded yet.")
        return

    number = 1
    for action in completed_actions:
        s_name = get_student_name(action["student_id"])
        print(f"\nCompleted #{number} [{action['action_id']}]")
        print(f"  Student     : {s_name} ({action['student_id']})")
        print(f"  Task        : {action['description']}")
        print("  Completed   : [✔] Successfully finished")
        print("-" * 50)
        number = number + 1


# -------------------------------------------------------------
# 4. Student-wise Progress Scorecard
# -------------------------------------------------------------

def student_summary():
    """Show one student's completion percentage and performance status."""
    print("\n" + "=" * 50)
    print("      STUDENT-WISE PROGRESS SCORECARD")
    print("=" * 50)

    student_id = input("Enter Student ID (e.g. S101): ").strip().upper()
    student = get_student(student_id)

    if student is None:
        print(f"[!] Student ID '{student_id}' does not exist.")
        return

    student_actions = []
    for action in actions:
        if action["student_id"] == student_id:
            student_actions.append(action)

    if len(student_actions) == 0:
        print(f"\nNo action items have been assigned yet to {student['name']} ({student_id}).")
        return

    stats = summarize_actions(student_actions)

    if stats["overdue"] > 0:
        performance_rating = "Needs Attention (Has Overdue Tasks)"
    elif stats["percentage"] >= 75.0:
        performance_rating = "Excellent (On Track)"
    elif stats["percentage"] >= 50.0:
        performance_rating = "Satisfactory (Making Progress)"
    else:
        performance_rating = "Pending Progress (< 50% Completed)"

    if student.get("mentor_id"):
        mentor_text = student["mentor_id"]
    else:
        mentor_text = "Not Assigned"

    print("\n" + "=" * 50)
    print(f"         MENTORING SCORECARD: {student['name'].upper()}")
    print("=" * 50)
    print(f"Student ID         : {student['student_id']}")
    print(f"Department & Year  : {student['department']} (Year {student['year']})")
    print(f"Assigned Mentor    : {mentor_text}")
    print("-" * 50)
    print(f"Total Assigned     : {stats['total']}")
    print(f"Completed Tasks    : {stats['completed']}")
    print(f"Pending Tasks      : {stats['pending']}")
    print(f"  - Overdue Tasks  : {stats['overdue']}")
    print(f"  - Due Today      : {stats['due_today']}")
    print(f"Overall Progress   : {stats['percentage']:.1f}%")
    print(f"Performance Status : {performance_rating}")
    print("-" * 50)
    print("Assigned Actions Breakdown:")
    for action in student_actions:
        cat = get_action_timeline_category(action)
        print(f"  [{cat:<9}] {action['action_id']} - {action['description'][:30]}")
    print("=" * 50)


# -------------------------------------------------------------
# 5. Flag Students Requiring Attention (At-Risk)
# -------------------------------------------------------------

def students_needing_attention():
    """Find students who have overdue tasks or < 50% completion."""
    print("\n" + "=" * 50)
    print("     STUDENTS REQUIRING MENTOR ATTENTION")
    print("=" * 50)

    flagged_students = []
    for student in students:
        s_actions = []
        for action in actions:
            if action["student_id"] == student["student_id"]:
                s_actions.append(action)

        if len(s_actions) == 0:
            continue

        stats = summarize_actions(s_actions)
        has_overdue = stats["overdue"] > 0
        has_low_progress = stats["percentage"] < 50.0 and stats["total"] > 1

        if has_overdue or has_low_progress:
            flagged_students.append({
                "student": student,
                "overdue": stats["overdue"],
                "total": stats["total"],
                "completed": stats["completed"],
                "percentage": stats["percentage"],
            })

    if len(flagged_students) == 0:
        print("[✔] Excellent! No students currently require urgent intervention.")
        return

    print(f"Found {len(flagged_students)} student(s) requiring mentor follow-up:\n")
    number = 1
    for item in flagged_students:
        st = item["student"]
        print(f"{number}. {st['name']} ({st['student_id']}) - Dept: {st['department']}")
        print(f"   • Overdue Tasks   : {item['overdue']}")
        print(f"   • Progress Rate   : {item['percentage']:.1f}% ({item['completed']}/{item['total']} completed)")
        print(f"   • Recommended     : Contact student via {st['contact']} to arrange review")
        print("-" * 50)
        number = number + 1


# -------------------------------------------------------------
# 6. Overall Cohort Mentoring Dashboard
# -------------------------------------------------------------

def cohort_dashboard():
    """Show total students, tasks, and overall completion percentage."""
    print("\n" + "=" * 50)
    print("       OVERALL COHORT MENTORING DASHBOARD")
    print("=" * 50)

    stats = summarize_actions(actions)

    print(f"Total Registered Students : {len(students)}")
    print(f"Total Action Items Tracked: {stats['total']}")
    print("-" * 50)
    print(f"Completed Actions         : {stats['completed']}")
    print(f"Pending Actions           : {stats['pending']}")
    print(f"  • Overdue Actions       : {stats['overdue']} (Needs Follow-up)")
    print(f"  • Due Today             : {stats['due_today']}")
    print("-" * 50)
    print(f"Overall Cohort Completion : {stats['percentage']:.1f}%")
    print("=" * 50)


# -------------------------------------------------------------
# 7. Student Progress Leaderboard
# -------------------------------------------------------------

def student_leaderboard():
    """Rank students from highest completion percentage to lowest."""
    print("\n" + "=" * 50)
    print("          STUDENT PROGRESS LEADERBOARD")
    print("=" * 50)

    leaderboard = []
    for student in students:
        s_actions = []
        for action in actions:
            if action["student_id"] == student["student_id"]:
                s_actions.append(action)

        if len(s_actions) == 0:
            continue

        stats = summarize_actions(s_actions)
        if stats["overdue"] > 0:
            status = "Needs Attention"
        elif stats["percentage"] >= 75.0:
            status = "Excellent"
        elif stats["percentage"] >= 50.0:
            status = "Satisfactory"
        else:
            status = "In Progress"

        leaderboard.append({
            "student_id": student["student_id"],
            "name": student["name"],
            "department": student["department"],
            "completed": stats["completed"],
            "total": stats["total"],
            "percentage": stats["percentage"],
            "status": status,
        })

    if len(leaderboard) == 0:
        print("[!] No student action items available yet.")
        return

    # Sort from highest percentage to lowest
    count = len(leaderboard)
    for i in range(count):
        for j in range(i + 1, count):
            if leaderboard[j]["percentage"] > leaderboard[i]["percentage"]:
                temp = leaderboard[i]
                leaderboard[i] = leaderboard[j]
                leaderboard[j] = temp

    rank = 1
    for entry in leaderboard:
        print(f"  #{rank} {entry['name']} ({entry['student_id']} - {entry['department']})")
        print(f"     Progress: {entry['percentage']:.1f}% ({entry['completed']}/{entry['total']} tasks) - {entry['status']}")
        rank = rank + 1
    print("=" * 50)


# -------------------------------------------------------------
# Module Submenu (called by main.py)
# -------------------------------------------------------------

def progress_menu():
    """Submenu loop for Follow-up & Progress Tracking."""
    while True:
        print("\n" + "=" * 50)
        print("       FOLLOW-UP & PROGRESS TRACKING")
        print("=" * 50)
        print("1. Daily Follow-up Radar (Due Today & Overdue)")
        print("2. View All Pending Actions by Timeline")
        print("3. View Completed Actions (Archive)")
        print("4. Student-wise Progress Scorecard")
        print("5. Flag Students Requiring Attention (At-Risk)")
        print("6. Overall Cohort Mentoring Dashboard")
        print("7. Student Progress Leaderboard")
        print("8. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            daily_follow_up_radar()
        elif choice == "2":
            view_pending_timeline()
        elif choice == "3":
            view_completed()
        elif choice == "4":
            student_summary()
        elif choice == "5":
            students_needing_attention()
        elif choice == "6":
            cohort_dashboard()
        elif choice == "7":
            student_leaderboard()
        elif choice == "8":
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid choice! Please select 1 to 8.")
