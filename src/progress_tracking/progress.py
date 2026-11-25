"""
Module 4: Follow-up & Progress Tracking
Author: Vikas Mahadev (Member 4)
Description:
    The analytical and monitoring engine for the mentoring tracker.
    Uses Student, Mentor, Meeting, and Action Item records to:
    - Show daily overdue/due-today alerts
    - Plan follow-ups for the next 7 days
    - Track student scorecards and flag at-risk students
    - Measure mentor workload and department progress
    - Audit meetings to make sure follow-up tasks were created
"""

from datetime import date
from data.sample_data import actions, students, mentors, meetings


# -------------------------------------------------------------
# Basic Helper Functions
# -------------------------------------------------------------

def get_student(student_id):
    """Find and return a student dictionary by ID, or None."""
    return next((s for s in students if s["student_id"] == student_id), None)


def get_student_name(student_id):
    """Return student name if found, otherwise fall back to student_id."""
    student = get_student(student_id)
    return student["name"] if student else student_id


def get_mentor_name(mentor_id):
    """Return mentor name if found, otherwise 'Not Assigned' or mentor_id."""
    if not mentor_id:
        return "Not Assigned"
    mentor = next((m for m in mentors if m["mentor_id"] == mentor_id), None)
    return mentor["name"] if mentor else mentor_id


def get_action_timeline_category(action):
    """
    Categorize an action item based on its status and follow-up date.
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
    if follow_up == today:
        return "DUE_TODAY"
    return "UPCOMING"


def summarize_actions(action_items):
    """Count total, completed, pending, overdue, and due-today tasks."""
    total = len(action_items)
    completed = sum(1 for a in action_items if get_action_timeline_category(a) == "COMPLETED")
    overdue = sum(1 for a in action_items if get_action_timeline_category(a) == "OVERDUE")
    due_today = sum(1 for a in action_items if get_action_timeline_category(a) == "DUE_TODAY")
    pending = total - completed
    percentage = (completed / total) * 100 if total > 0 else 0.0

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
        "due_today": due_today,
        "percentage": percentage,
    }


def get_performance_rating(overdue, percentage):
    """Return a readable performance label for a student."""
    if overdue > 0:
        return "Needs Attention (Has Overdue Tasks)"
    if percentage >= 75.0:
        return "Excellent (On Track)"
    if percentage >= 50.0:
        return "Satisfactory (Making Progress)"
    return "Pending Progress (< 50% Completed)"


def build_progress_bar(percentage, width=10):
    """Build a text progress bar like [#####-----] 50.0% (drives UI bars in Phase 4)."""
    filled = max(0, min(width, int((percentage / 100) * width)))
    bar = ("#" * filled) + ("-" * (width - filled))
    return f"[{bar}] {percentage:.1f}%"


# -------------------------------------------------------------
# 1. Daily Follow-up Radar (Due Today & Overdue Items)
# -------------------------------------------------------------

def daily_follow_up_radar():
    """Show overdue and due-today actions needing immediate attention."""
    today = date.today()
    print("\n" + "=" * 50)
    print("           DAILY FOLLOW-UP RADAR")
    print(f"           Today's Date: {today}")
    print("=" * 50)

    overdue_items = [a for a in actions if get_action_timeline_category(a) == "OVERDUE"]
    due_today_items = [a for a in actions if get_action_timeline_category(a) == "DUE_TODAY"]

    print("\n[!] OVERDUE ACTIONS (IMMEDIATE ATTENTION NEEDED):")
    print("-" * 50)
    if not overdue_items:
        print("  [✔] None! All actions are on schedule.")
    else:
        for idx, action in enumerate(overdue_items, start=1):
            s_name = get_student_name(action["student_id"])
            days_late = (today - date.fromisoformat(action["follow_up_date"])).days
            print(f"  {idx}. [{action['action_id']}] {s_name} ({action['student_id']})")
            print(f"     Task      : {action['description']}")
            print(f"     Follow-up : {action['follow_up_date']} ({days_late} day(s) overdue!)")

    print("\n[★] ACTIONS DUE FOR FOLLOW-UP TODAY:")
    print("-" * 50)
    if not due_today_items:
        print("  [i] No actions scheduled for follow-up today.")
    else:
        for idx, action in enumerate(due_today_items, start=1):
            s_name = get_student_name(action["student_id"])
            print(f"  {idx}. [{action['action_id']}] {s_name} ({action['student_id']})")
            print(f"     Task      : {action['description']}")
            print(f"     Due Date  : {action['due_date']}")
    print("=" * 50)


# -------------------------------------------------------------
# 2. View Pending Actions by Timeline
# -------------------------------------------------------------

def view_pending_timeline():
    """Display all pending actions with urgency status and day countdown."""
    print("\n" + "=" * 50)
    print("       PENDING ACTIONS TIMELINE & DEADLINES")
    print("=" * 50)

    pending_actions = [a for a in actions if a["status"] == "Pending"]
    if not pending_actions:
        print("[!] No pending actions found in the system.")
        return

    today = date.today()
    for idx, action in enumerate(pending_actions, start=1):
        s_name = get_student_name(action["student_id"])
        category = get_action_timeline_category(action)

        try:
            diff = (date.fromisoformat(action["follow_up_date"]) - today).days
            if diff < 0:
                timeline_str = f"{abs(diff)} days OVERDUE"
            elif diff == 0:
                timeline_str = "DUE TODAY"
            else:
                timeline_str = f"Due in {diff} day(s)"
        except ValueError:
            timeline_str = "Date unavailable"

        print(f"\nTask #{idx} - [{category}]")
        print(f"  Action ID      : {action['action_id']}")
        print(f"  Student        : {s_name} ({action['student_id']})")
        print(f"  Description    : {action['description']}")
        print(f"  Follow-up Date : {action['follow_up_date']} ({timeline_str})")
        print("-" * 50)


# -------------------------------------------------------------
# 3. View Completed Actions & Achievements
# -------------------------------------------------------------

def view_completed():
    """Display all completed action items."""
    print("\n" + "=" * 50)
    print("         COMPLETED ACTIONS (ARCHIVE)")
    print("=" * 50)

    completed_actions = [a for a in actions if a["status"] == "Completed"]
    if not completed_actions:
        print("[!] No completed actions recorded yet.")
        return

    for idx, action in enumerate(completed_actions, start=1):
        s_name = get_student_name(action["student_id"])
        print(f"\nCompleted #{idx} [{action['action_id']}]")
        print(f"  Student     : {s_name} ({action['student_id']})")
        print(f"  Task        : {action['description']}")
        print("  Completed   : [✔] Successfully finished")
        print("-" * 50)


# -------------------------------------------------------------
# 4. Student-wise Progress Summary & Scorecard
# -------------------------------------------------------------

def student_summary():
    """Generate an individual student's mentoring progress scorecard."""
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

    stats = summarize_actions(student_actions)
    performance_rating = get_performance_rating(stats["overdue"], stats["percentage"])

    print("\n" + "=" * 50)
    print(f"         MENTORING SCORECARD: {student['name'].upper()}")
    print("=" * 50)
    print(f"Student ID         : {student['student_id']}")
    print(f"Department & Year  : {student['department']} (Year {student['year']})")
    print(f"Assigned Mentor    : {student.get('mentor_id') or 'Not Assigned'}")
    print("-" * 50)
    print(f"Total Assigned     : {stats['total']}")
    print(f"Completed Tasks    : {stats['completed']}")
    print(f"Pending Tasks      : {stats['pending']}")
    print(f"  - Overdue Tasks  : {stats['overdue']}")
    print(f"  - Due Today      : {stats['due_today']}")
    print(f"Overall Progress   : {build_progress_bar(stats['percentage'])}")
    print(f"Performance Status : {performance_rating}")
    print("-" * 50)
    print("Assigned Actions Breakdown:")
    for action in student_actions:
        cat = get_action_timeline_category(action)
        print(f"  [{cat:<9}] {action['action_id']} - {action['description'][:30]}")
    print("=" * 50)


# -------------------------------------------------------------
# 5. Students Requiring Urgent Attention (At-Risk Alert)
# -------------------------------------------------------------

def students_needing_attention():
    """Flag students who have overdue tasks or low completion (< 50%)."""
    print("\n" + "=" * 50)
    print("     STUDENTS REQUIRING MENTOR ATTENTION")
    print("=" * 50)

    flagged_students = []
    for student in students:
        s_actions = [a for a in actions if a["student_id"] == student["student_id"]]
        if not s_actions:
            continue

        stats = summarize_actions(s_actions)
        if stats["overdue"] > 0 or (stats["percentage"] < 50.0 and stats["total"] > 1):
            flagged_students.append({"student": student, **stats})

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
    """Display an executive summary across the entire cohort."""
    print("\n" + "=" * 50)
    print("       OVERALL COHORT MENTORING DASHBOARD")
    print("=" * 50)

    stats = summarize_actions(actions)

    print(f"Total Registered Students : {len(students)}")
    print(f"Total Registered Mentors  : {len(mentors)}")
    print(f"Total Meetings Tracked    : {len(meetings)}")
    print(f"Total Action Items Tracked: {stats['total']}")
    print("-" * 50)
    print(f"Completed Actions         : {stats['completed']}")
    print(f"Pending Actions           : {stats['pending']}")
    print(f"  • Overdue Actions       : {stats['overdue']} (Needs Follow-up)")
    print(f"  • Due Today             : {stats['due_today']}")
    print("-" * 50)
    print(f"Overall Cohort Completion : {build_progress_bar(stats['percentage'])}")
    print("=" * 50)


# -------------------------------------------------------------
# 7. Weekly Follow-up Planner (Next 7 Days Forecast)
# -------------------------------------------------------------

def weekly_follow_up_planner():
    """Group all pending tasks into Overdue, Today, Next 7 Days, and Later."""
    today = date.today()
    print("\n" + "=" * 50)
    print("       WEEKLY FOLLOW-UP PLANNER (7 DAYS)")
    print(f"       Planning From: {today}")
    print("=" * 50)

    buckets = {
        "OVERDUE (ACTION NEEDED)": [],
        "DUE TODAY": [],
        "DUE IN NEXT 7 DAYS": [],
        "UPCOMING LATER (> 7 DAYS)": [],
    }

    for action in actions:
        if action["status"] != "Pending":
            continue
        try:
            days_left = (date.fromisoformat(action["follow_up_date"]) - today).days
        except (ValueError, KeyError):
            continue

        if days_left < 0:
            buckets["OVERDUE (ACTION NEEDED)"].append(action)
        elif days_left == 0:
            buckets["DUE TODAY"].append(action)
        elif days_left <= 7:
            buckets["DUE IN NEXT 7 DAYS"].append(action)
        else:
            buckets["UPCOMING LATER (> 7 DAYS)"].append(action)

    for title, item_list in buckets.items():
        print(f"\n[{title}] - {len(item_list)} item(s)")
        print("-" * 50)
        if not item_list:
            print("  No tasks in this bucket.")
        else:
            for action in item_list:
                s_name = get_student_name(action["student_id"])
                print(f"  • [{action['action_id']}] {s_name} ({action['student_id']})")
                print(f"    {action['description']} (Follow-up: {action['follow_up_date']})")
    print("=" * 50)


# -------------------------------------------------------------
# 8. Mentor Workload & Performance Report
# -------------------------------------------------------------

def mentor_performance_report():
    """Show each mentor's mentees, meetings, and action completion rate."""
    print("\n" + "=" * 50)
    print("       MENTOR WORKLOAD & PERFORMANCE REPORT")
    print("=" * 50)

    if not mentors:
        print("[!] No mentors registered yet.")
        return

    for mentor in mentors:
        m_id = mentor["mentor_id"]
        mentees = [s for s in students if s.get("mentor_id") == m_id]
        mentee_ids = {s["student_id"] for s in mentees}
        mentee_text = ", ".join(s["name"] for s in mentees) if mentees else "None"

        mentor_meetings = [m for m in meetings if m.get("mentor_id") == m_id]
        completed_meetings = sum(1 for m in mentor_meetings if m["status"] == "Completed")
        scheduled_meetings = len(mentor_meetings) - completed_meetings

        mentor_actions = [a for a in actions if a["student_id"] in mentee_ids]
        stats = summarize_actions(mentor_actions)

        print(f"\nMentor: {mentor['name']} ({m_id}) - Dept: {mentor['department']}")
        print(f"  Assigned Mentees   : {len(mentees)} ({mentee_text})")
        print(f"  Meetings           : {completed_meetings} Completed, {scheduled_meetings} Scheduled")
        print(f"  Mentee Action Items: {stats['total']} Total | {stats['completed']} Done | {stats['overdue']} Overdue")
        print(f"  Completion Rate    : {build_progress_bar(stats['percentage'])}")
        print("-" * 50)


# -------------------------------------------------------------
# 9. Department Breakdown & Student Leaderboard
# -------------------------------------------------------------

def department_and_leaderboard_report():
    """Show department-wise progress and rank students by completion rate."""
    print("\n" + "=" * 50)
    print("    DEPARTMENT STATS & STUDENT LEADERBOARD")
    print("=" * 50)

    departments = list(dict.fromkeys(s["department"] for s in students))

    print("\n[A] DEPARTMENT-WISE PROGRESS:")
    print("-" * 50)
    for dept in departments:
        dept_ids = {s["student_id"] for s in students if s["department"] == dept}
        dept_actions = [a for a in actions if a["student_id"] in dept_ids]
        stats = summarize_actions(dept_actions)
        print(f"  {dept} ({len(dept_ids)} student(s))")
        print(f"    Tasks: {stats['completed']}/{stats['total']} Completed | Overdue: {stats['overdue']}")
        print(f"    Rate : {build_progress_bar(stats['percentage'])}")

    leaderboard = []
    for student in students:
        s_actions = [a for a in actions if a["student_id"] == student["student_id"]]
        if s_actions:
            leaderboard.append({**student, **summarize_actions(s_actions)})

    leaderboard.sort(key=lambda entry: entry["percentage"], reverse=True)

    print("\n[B] STUDENT PROGRESS LEADERBOARD:")
    print("-" * 50)
    if not leaderboard:
        print("  No student action items available yet.")
    else:
        for rank, entry in enumerate(leaderboard, start=1):
            bar = build_progress_bar(entry["percentage"])
            status = get_performance_rating(entry["overdue"], entry["percentage"])
            print(f"  #{rank} {entry['name']} ({entry['student_id']} - {entry['department']})")
            print(f"     {bar} ({entry['completed']}/{entry['total']} tasks) - {status}")
    print("=" * 50)


# -------------------------------------------------------------
# 10. Meeting Follow-up Audit
# -------------------------------------------------------------

def meeting_follow_up_audit():
    """Check each meeting for linked action items and flag missing follow-ups."""
    print("\n" + "=" * 50)
    print("          MEETING FOLLOW-UP AUDIT")
    print("=" * 50)

    if not meetings:
        print("[!] No meetings recorded in the system.")
        return

    missing_follow_ups = 0

    for meeting in meetings:
        m_id = meeting["meeting_id"]
        s_name = get_student_name(meeting["student_id"])
        m_name = get_mentor_name(meeting.get("mentor_id"))
        linked_actions = [a for a in actions if a.get("meeting_id") == m_id]
        stats = summarize_actions(linked_actions)

        print(f"\nMeeting [{m_id}] - {meeting['date']} ({meeting['status']})")
        print(f"  Student & Mentor : {s_name} with {m_name}")
        print(f"  Topic            : {meeting.get('description', '')}")

        if stats["total"] == 0:
            if meeting["status"] == "Completed":
                print("  [!] ALERT: Completed meeting has NO follow-up action items!")
                missing_follow_ups += 1
            else:
                print("  [i] Scheduled meeting - no tasks assigned yet.")
        else:
            print(f"  Follow-up Tasks  : {stats['completed']}/{stats['total']} Completed | {stats['overdue']} Overdue")
        print("-" * 50)

    print(f"Audit Summary: {missing_follow_ups} completed meeting(s) missing follow-up tasks.")
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
        print("7. Weekly Follow-up Planner (Next 7 Days)")
        print("8. Mentor Workload & Performance Report")
        print("9. Department Stats & Student Leaderboard")
        print("10. Meeting Follow-up Audit")
        print("11. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice (1-11): ").strip()

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
            weekly_follow_up_planner()
        elif choice == "8":
            mentor_performance_report()
        elif choice == "9":
            department_and_leaderboard_report()
        elif choice == "10":
            meeting_follow_up_audit()
        elif choice == "11":
            print("\nReturning to Main Menu...")
            break
        else:
            print("[!] Invalid choice! Please select 1 to 11.")
