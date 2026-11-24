"""
Shared Data Store & Demonstration Sample Records
Student Mentoring Tracker - Phase 1

This module maintains the in-memory shared data lists:
- students
- mentors
- meetings
- actions
All 4 modules import and manipulate these shared lists during program execution.
"""

from datetime import date, timedelta

today = date.today()
today_str = str(today)
past_date_3 = str(today - timedelta(days=3))
past_date_5 = str(today - timedelta(days=5))
past_date_8 = str(today - timedelta(days=8))
future_date_4 = str(today + timedelta(days=4))
future_date_7 = str(today + timedelta(days=7))

# -------------------------------------------------------------
# 1. Mentors
# -------------------------------------------------------------
mentors = [
    {
        "mentor_id": "M101",
        "name": "Dr. Kumar",
        "department": "MCA",
        "contact": "9876543211"
    },
    {
        "mentor_id": "M102",
        "name": "Prof. Anitha",
        "department": "MCA",
        "contact": "9876543212"
    }
]

# -------------------------------------------------------------
# 2. Students
# -------------------------------------------------------------
students = [
    {
        "student_id": "S101",
        "name": "Rahul",
        "department": "MCA",
        "year": 1,
        "contact": "9876543210",
        "mentor_id": "M101"
    },
    {
        "student_id": "S102",
        "name": "Priya",
        "department": "MCA",
        "year": 1,
        "contact": "9876543222",
        "mentor_id": "M102"
    },
    {
        "student_id": "S103",
        "name": "Arjun",
        "department": "MCA",
        "year": 2,
        "contact": "9876543233",
        "mentor_id": None
    }
]

# -------------------------------------------------------------
# 3. Meetings
# -------------------------------------------------------------
meetings = [
    {
        "meeting_id": "MT101",
        "student_id": "S101",
        "mentor_id": "M101",
        "date": past_date_5,
        "time": "10:30 AM",
        "description": "Initial academic mentoring and course discussion",
        "notes": "Discussed Python assignments and mini-project timeline",
        "status": "Completed"
    },
    {
        "meeting_id": "MT102",
        "student_id": "S102",
        "mentor_id": "M102",
        "date": future_date_4,
        "time": "02:00 PM",
        "description": "Semester progress review",
        "notes": "",
        "status": "Scheduled"
    }
]

# -------------------------------------------------------------
# 4. Action Items
# Demonstrates: Completed, Due Today, Overdue, and Upcoming
# -------------------------------------------------------------
actions = [
    {
        "action_id": "A101",
        "student_id": "S101",
        "meeting_id": "MT101",
        "description": "Complete Python basics assignment",
        "assigned_date": past_date_8,
        "due_date": past_date_5,
        "follow_up_date": past_date_5,
        "status": "Completed"
    },
    {
        "action_id": "A102",
        "student_id": "S101",
        "meeting_id": "MT101",
        "description": "Submit DBMS ER Diagram draft",
        "assigned_date": past_date_5,
        "due_date": today_str,
        "follow_up_date": today_str,
        "status": "Pending"   # Due Today
    },
    {
        "action_id": "A103",
        "student_id": "S101",
        "meeting_id": "MT101",
        "description": "Mini-project topic proposal submission",
        "assigned_date": past_date_8,
        "due_date": past_date_3,
        "follow_up_date": past_date_3,
        "status": "Pending"   # Overdue! (follow_up_date < today)
    },
    {
        "action_id": "A104",
        "student_id": "S101",
        "meeting_id": "MT101",
        "description": "Prepare seminar presentation slides",
        "assigned_date": past_date_5,
        "due_date": future_date_7,
        "follow_up_date": future_date_7,
        "status": "Pending"   # Upcoming
    },
    {
        "action_id": "A105",
        "student_id": "S102",
        "meeting_id": "MT102",
        "description": "Review research papers for seminar",
        "assigned_date": today_str,
        "due_date": future_date_4,
        "follow_up_date": future_date_4,
        "status": "Pending"   # Upcoming
    }
]

# Backwards compatibility aliases
SAMPLE_STUDENTS = students
SAMPLE_MENTORS = mentors
SAMPLE_MEETINGS = meetings
SAMPLE_ACTIONS = actions
