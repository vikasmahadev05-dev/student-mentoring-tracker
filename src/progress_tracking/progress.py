"""
Module 4: Follow-up & Progress Tracking
Author: Vikas Mahadev (Member 4)
Description:
    The analytical and monitoring engine for the mentoring tracker.
    Uses Student and Action Item records to track follow-up deadlines,
    detect overdue tasks, flag at-risk students, and calculate progress summaries.
"""

from datetime import date
from shared_data import actions, students


def get_student(student_id):
    """Helper: Find student dictionary by ID."""
    for s in students:
        if s["student_id"] == student_id:
            return s
    return None


def get_action_timeline_category(action):
    """
    Helper: Categorize an action based on its status and follow-up date.
    Returns: 'COMPLETED', 'OVERDUE', 'DUE_TODAY', or 'UPCOMING'
    
    Business Rules (SRS):
    - Completed actions are never marked overdue.
    - Pending actions with follow_up_date < today are OVERDUE.
    - Pending actions with follow_up_date == today are DUE_TODAY.
    - Pending actions with follow_up_date > today are UPCOMING.
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


# -------------------------------------------------------------
# 1. Daily Follow-up Radar (Due Today & Overdue Items)
# -------------------------------------------------------------

def daily_follow_up_radar():
    """
    Actionable daily briefing for mentors showing items requiring immediate attention.
    Combines Overdue actions and actions Due Today.
    """
    today = date.today()
    print("\n" + "=" * 50)
    print("           DAILY FOLLOW-UP RADAR")
    print(f"           Today's Date: {today}")
    print("=" * 50)

    overdue_items = []
    due_today_items = []

    for a in actions:
        cat = get_action_timeline_category(a)
        if cat == "OVERDUE":
            overdue_items.append(a)
        elif cat == "DUE_TODAY":
            due_today_items.append(a)

    # Section 1: Overdue Alerts
    print("\n[!] OVERDUE ACTIONS (IMMEDIATE ATTENTION NEEDED):")
    print("-" * 50)
    if not overdue_items:
        print("  [✔] None! All actions are on schedule.")
    else:
        for idx, a in enumerate(overdue_items, start=1):
            s = get_student(a["student_id"])
            s_name = s["name"] if s else a["student_id"]
            follow_up = date.fromisoformat(a["follow_up_date"])
            days_late = (today - follow_up).days
            print(f"  {idx}. [{a['action_id']}] {s_name} ({a['student_id']})")
            print(f"     Task      : {a['description']}")
            print(f"     Follow-up : {a['follow_up_date']} ({days_late} day(s) overdue!)")

    # Section 2: Due Today
    print("\n[★] ACTIONS DUE FOR FOLLOW-UP TODAY:")
    print("-" * 50)
    if not due_today_items:
        print("  [i] No actions scheduled for follow-up today.")
    else:
        for idx, a in enumerate(due_today_items, start=1):
            s = get_student(a["student_id"])
            s_name = s["name"] if s else a["student_id"]
            print(f"  {idx}. [{a['action_id']}] {s_name} ({a['student_id']})")
            print(f"     Task      : {a['description']}")
            print(f"     Due Date  : {a['due_date']}")
    print("=" * 50)


# -------------------------------------------------------------
# 2. View Pending Actions by Timeline
# -------------------------------------------------------------

def view_pending_timeline():
    """Displays all pending actions categorized by urgency with countdowns."""
    print("\n" + "=" * 50)
    print("       PENDING ACTIONS TIMELINE & DEADLINES")
    print("=" * 50)

    pending_actions = [a for a in actions if a["status"] == "Pending"]
    if not pending_actions:
        print("[!] No pending actions found in the system.")
        return

    today = date.today()
    for idx, a in enumerate(pending_actions, start=1):
        s = get_student(a["student_id"])
        s_name = s["name"] if s else a["student_id"]
        category = get_action_timeline_category(a)

        # Calculate days difference
        try:
            follow_up = date.fromisoformat(a["follow_up_date"])
            diff = (follow_up - today).days
            if diff < 0:
                timeline_str = f"{abs(diff)} days OVERDUE"
            elif diff == 0:
                timeline_str = "DUE TODAY"
            else:
                timeline_str = f"Due in {diff} day(s)"
        except ValueError:
            timeline_str = "Date unavailable"

        print(f"\nTask #{idx} - [{category}]")
        print(f"  Action ID      : {a['action_id']}")
        print(f"  Student        : {s_name} ({a['student_id']})")
        print(f"  Description    : {a['description']}")
        print(f"  Follow-up Date : {a['follow_up_date']} ({timeline_str})")
        print("-" * 50)


# -------------------------------------------------------------
# 3. View Completed Actions & Achievements
# -------------------------------------------------------------

def view_completed():
    """Displays all completed action items."""
    print("\n" + "=" * 50)
    print("         COMPLETED ACTIONS (ARCHIVE)")
    print("=" * 50)

    completed = [a for a in actions if a["status"] == "Completed"]
    if not completed:
        print("[!] No completed actions recorded yet.")
        return

    for idx, a in enumerate(completed, start=1):
        s = get_student(a["student_id"])
        s_name = s["name"] if s else a["student_id"]
        print(f"\nCompleted #{idx} [{a['action_id']}]")
        print(f"  Student     : {s_name} ({a['student_id']})")
        print(f"  Task        : {a['description']}")
        print(f"  Completed   : [✔] Successfully finished")
        print("-" * 50)


# -------------------------------------------------------------
# 4. Student-wise Progress Summary & Scorecard
# -------------------------------------------------------------

def student_summary():
    """
    Generates an individual student's mentoring progress scorecard.
    Calculates completion percentage, status breakdown, and performance rating.
    Formula: Progress = (Completed Actions / Total Actions) * 100
    """
    print("\n" + "=" * 50)
    print("      STUDENT-WISE PROGRESS SCORECARD")
    print("=" * 50)

    student_id = input("Enter Student ID (e.g. S101): ").strip().upper()
    student = get_student(student_id)

    if not student:
        print(f"[!] Student ID '{student_id}' does not exist.")
        return

    student_actions = [a for a in actions if a["student_id"] == student_id]

    if not student_actions:
        print(f"\nNo action items have been assigned yet to {student['name']} ({student_id}).")
        return

    total = len(student_actions)
    completed = 0
    pending = 0
    overdue = 0
    due_today = 0

    for a in student_actions:
        cat = get_action_timeline_category(a)
        if cat == "COMPLETED":
            completed += 1
        elif cat == "OVERDUE":
            overdue += 1
            pending += 1
        elif cat == "DUE_TODAY":
            due_today += 1
            pending += 1
        else:
            pending += 1

    percentage = (completed / total) * 100 if total > 0 else 0.0

    # Performance Rating based on percentage and overdue status
    if overdue > 0:
        performance_rating = "Needs Attention (Has Overdue Tasks)"
    elif percentage >= 75.0:
        performance_rating = "Excellent (On Track)"
    elif percentage >= 50.0:
        performance_rating = "Satisfactory (Making Progress)"
    else:
        performance_rating = "Pending Progress (< 50% Completed)"

    print("\n" + "=" * 50)
    print(f"         MENTORING SCORECARD: {student['name'].upper()}")
    print("=" * 50)
    print(f"Student ID         : {student['student_id']}")
    print(f"Department & Year  : {student['department']} (Year {student['year']})")
    print(f"Assigned Mentor    : {student.get('mentor_id') or 'Not Assigned'}")
    print("-" * 50)
    print(f"Total Assigned     : {total}")
    print(f"Completed Tasks    : {completed}")
    print(f"Pending Tasks      : {pending}")
    print(f"  - Overdue Tasks  : {overdue}")
    print(f"  - Due Today      : {due_today}")
    print(f"Overall Progress   : {percentage:.1f}%")
    print(f"Performance Status : {performance_rating}")
    print("-" * 50)
    print("Assigned Actions Breakdown:")
    for a in student_actions:
        cat = get_action_timeline_category(a)
        print(f"  [{cat:<9}] {a['action_id']} - {a['description'][:30]}")
    print("=" * 50)


# -------------------------------------------------------------
# 5. Students Requiring Urgent Attention (At-Risk Alert)
# -------------------------------------------------------------

def students_needing_attention():
    """
    Identifies students who have overdue tasks or low progress (< 50%).
    Helps mentors proactively intervene for struggling students.
    """
    print("\n" + "=" * 50)
    print("     STUDENTS REQUIRING MENTOR ATTENTION")
    print("=" * 50)

    flagged_students = []

    for s in students:
        s_id = s["student_id"]
        s_actions = [a for a in actions if a["student_id"] == s_id]

        if not s_actions:
            continue

        overdue_count = 0
        completed_count = 0
        for a in s_actions:
            cat = get_action_timeline_category(a)
            if cat == "OVERDUE":
                overdue_count += 1
            elif cat == "COMPLETED":
                completed_count += 1

        total = len(s_actions)
        pct = (completed_count / total) * 100

        # Flag if overdue tasks exist OR completion < 50%
        if overdue_count > 0 or (pct < 50.0 and total > 1):
            flagged_students.append({
                "student": s,
                "overdue": overdue_count,
                "total": total,
                "completed": completed_count,
                "percentage": pct
            })

    if not flagged_students:
        print("[✔] Excellent! No students currently require urgent intervention.")
        return

    print(f"Found {len(flagged_students)} student(s) requiring mentor follow-up:\n")
    for idx, item in enumerate(flagged_students, start=1):
        st = item["student"]
        print(f"{idx}. {st['name']} ({st['student_id']}) - Dept: {st['department']}")
        print(f"   • Overdue Tasks   : {item['overdue']}")
        print(f"   • Progress Rate   : {item['percentage']:.1f}% ({item['completed']}/{item['total']} completed)")
        print(f"   • Recommended     : Contact student via {st['contact']} to arrange review")
        print("-" * 50)


# -------------------------------------------------------------
# 6. Overall Cohort Mentoring Dashboard
# -------------------------------------------------------------

def cohort_dashboard():
    """
    Provides an executive summary of all mentoring activities
    across the entire department/cohort.
    """
    print("\n" + "=" * 50)
    print("       OVERALL COHORT MENTORING DASHBOARD")
    print("=" * 50)

    total_students = len(students)
    total_actions = len(actions)
    completed_actions = sum(1 for a in actions if a["status"] == "Completed")
    pending_actions = sum(1 for a in actions if a["status"] == "Pending")
    overdue_actions = sum(1 for a in actions if get_action_timeline_category(a) == "OVERDUE")
    due_today_actions = sum(1 for a in actions if get_action_timeline_category(a) == "DUE_TODAY")

    overall_pct = (completed_actions / total_actions) * 100 if total_actions > 0 else 0.0

    print(f"Total Registered Students : {total_students}")
    print(f"Total Action Items Tracked: {total_actions}")
    print("-" * 50)
    print(f"Completed Actions         : {completed_actions}")
    print(f"Pending Actions           : {pending_actions}")
    print(f"  • Overdue Actions       : {overdue_actions} (Needs Follow-up)")
    print(f"  • Due Today             : {due_today_actions}")
    print("-" * 50)
    print(f"Overall Cohort Completion : {overall_pct:.1f}%")
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
        print("7. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice (1-7): ").strip()

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
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid choice! Please select 1 to 7.")
