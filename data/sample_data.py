"""
Sample Data for Student Mentoring Tracker
Phase 1 - Procedural Programming
"""

SAMPLE_STUDENTS = [
    {"student_id": "S001", "name": "Rahul Sharma", "semester": "MCA Sem 1", "email": "rahul.s@univ.edu"},
    {"student_id": "S002", "name": "Priya Patel", "semester": "MCA Sem 1", "email": "priya.p@univ.edu"},
    {"student_id": "S003", "name": "Arjun Verma", "semester": "MCA Sem 1", "email": "arjun.v@univ.edu"}
]

SAMPLE_MENTORS = [
    {"mentor_id": "MTR01", "name": "Dr. Ramesh Kumar", "department": "Computer Applications", "email": "ramesh.k@univ.edu"},
    {"mentor_id": "MTR02", "name": "Prof. Anitha Rao", "department": "Computer Applications", "email": "anitha.r@univ.edu"}
]

SAMPLE_MEETINGS = [
    {
        "meeting_id": "M001",
        "student_id": "S001",
        "student_name": "Rahul Sharma",
        "mentor_id": "MTR01",
        "mentor_name": "Dr. Ramesh Kumar",
        "date": "2026-11-20",
        "time": "10:30",
        "mode": "In-Person",
        "agenda": "Semester 1 Academic Review & Attendance Check",
        "notes": "Student showed steady progress in Python. Advised to practice more data structures.",
        "status": "Completed"
    },
    {
        "meeting_id": "M002",
        "student_id": "S002",
        "student_name": "Priya Patel",
        "mentor_id": "MTR02",
        "mentor_name": "Prof. Anitha Rao",
        "date": "2026-11-28",
        "time": "14:00",
        "mode": "Online",
        "agenda": "Minor Project Topic Discussion & Scope Finalization",
        "notes": "Reviewed initial synopsis. Student to submit revised problem statement.",
        "status": "Scheduled"
    },
    {
        "meeting_id": "M003",
        "student_id": "S003",
        "student_name": "Arjun Verma",
        "mentor_id": "MTR01",
        "mentor_name": "Dr. Ramesh Kumar",
        "date": "2026-11-30",
        "time": "11:15",
        "mode": "In-Person",
        "agenda": "Career Guidance & Internship Preparation",
        "notes": "Discussed skill building for upcoming campus placements.",
        "status": "Scheduled"
    }
]
