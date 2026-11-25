"""
Shared Data Store & Demonstration Sample Records
Student Mentoring Tracker - Phase 1

This module maintains the in-memory shared data lists:
- mentors
- students
- meetings
- actions
All 4 modules import and update these lists during program execution.
"""

from datetime import date, timedelta

today = date.today()
today_str = str(today)
past_date_2 = str(today - timedelta(days=2))
past_date_3 = str(today - timedelta(days=3))
past_date_5 = str(today - timedelta(days=5))
past_date_8 = str(today - timedelta(days=8))
past_date_10 = str(today - timedelta(days=10))
future_date_2 = str(today + timedelta(days=2))
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
    },
    {
        "mentor_id": "M103",
        "name": "Dr. Suresh Nair",
        "department": "MCA",
        "contact": "9876543213"
    },
    {
        "mentor_id": "M104",
        "name": "Prof. Meera Krishnan",
        "department": "BCA",
        "contact": "9876543214"
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
    },
    {
        "student_id": "S104",
        "name": "Sneha",
        "department": "MCA",
        "year": 2,
        "contact": "9876543244",
        "mentor_id": "M103"
    },
    {
        "student_id": "S105",
        "name": "Karthik",
        "department": "BCA",
        "year": 3,
        "contact": "9876543255",
        "mentor_id": "M104"
    },
    {
        "student_id": "S106",
        "name": "Divya",
        "department": "MCA",
        "year": 1,
        "contact": "9876543266",
        "mentor_id": "M101"
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
    },
    {
        "meeting_id": "MT103",
        "student_id": "S104",
        "mentor_id": "M103",
        "date": past_date_3,
        "time": "11:15 AM",
        "description": "Final year project architecture review",
        "notes": "Approved ER model and database normalization plan",
        "status": "Completed"
    },
    {
        "meeting_id": "MT104",
        "student_id": "S105",
        "mentor_id": "M104",
        "date": past_date_2,
        "time": "03:30 PM",
        "description": "Attendance and lab performance check-in",
        "notes": "Student needs extra practice in SQL joins",
        "status": "Completed"
    },
    {
        "meeting_id": "MT105",
        "student_id": "S106",
        "mentor_id": "M101",
        "date": future_date_2,
        "time": "04:00 PM",
        "description": "Internship readiness and resume review",
        "notes": "Bring updated resume draft",
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
    },
    {
        "action_id": "A106",
        "student_id": "S104",
        "meeting_id": "MT103",
        "description": "Finalize project synopsis document",
        "assigned_date": past_date_10,
        "due_date": past_date_5,
        "follow_up_date": past_date_5,
        "status": "Completed"
    },
    {
        "action_id": "A107",
        "student_id": "S104",
        "meeting_id": "MT103",
        "description": "Push normalized SQL schema to repo",
        "assigned_date": past_date_5,
        "due_date": past_date_2,
        "follow_up_date": past_date_2,
        "status": "Completed"
    },
    {
        "action_id": "A108",
        "student_id": "S105",
        "meeting_id": "MT104",
        "description": "Complete SQL joins lab worksheet",
        "assigned_date": past_date_8,
        "due_date": past_date_2,
        "follow_up_date": past_date_2,
        "status": "Pending"   # Overdue!
    },
    {
        "action_id": "A109",
        "student_id": "S105",
        "meeting_id": "MT104",
        "description": "Attend remedial coding session",
        "assigned_date": past_date_3,
        "due_date": future_date_2,
        "follow_up_date": future_date_2,
        "status": "Pending"   # Upcoming
    },
    {
        "action_id": "A110",
        "student_id": "S106",
        "meeting_id": "MT105",
        "description": "Update technical resume for placement",
        "assigned_date": past_date_3,
        "due_date": today_str,
        "follow_up_date": today_str,
        "status": "Pending"   # Due Today
    }
]
