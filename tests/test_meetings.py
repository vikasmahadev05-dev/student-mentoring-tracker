"""
Unit Tests for Meeting Management Module (src/meeting_management/meetings.py)
Phase 1: Procedural Programming Verification
"""

import unittest
from unittest.mock import patch

from src.meeting_management import meetings


class TestMeetingManagement(unittest.TestCase):

    def setUp(self):
        """Reset meeting_list to a known state before each test."""
        meetings.meeting_list = [
            {
                "meeting_id": "M001",
                "student_id": "S001",
                "student_name": "Rahul Sharma",
                "mentor_id": "MTR01",
                "mentor_name": "Dr. Ramesh Kumar",
                "date": "2026-11-20",
                "time": "10:30",
                "mode": "In-Person",
                "agenda": "Academic Review",
                "notes": "Good progress in coursework.",
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
                "agenda": "Minor Project Discussion",
                "notes": "Reviewed initial synopsis.",
                "status": "Scheduled"
            }
        ]

    # --------------------------------------------------------------------------
    # Core Operation 1 Tests: Schedule Meeting
    # --------------------------------------------------------------------------
    @patch("builtins.input", side_effect=[
        "S003",                    # Student ID
        "Arjun Verma",             # Student Name
        "MTR01",                   # Mentor ID
        "Dr. Ramesh Kumar",        # Mentor Name
        "2026-12-01",              # Date
        "11:00",                   # Time
        "1",                       # Mode (In-Person)
        "Internship Counseling",   # Agenda
        "Discussed upcoming drives"# Initial Notes
    ])
    def test_schedule_meeting(self, mock_input):
        initial_count = len(meetings.meeting_list)
        meetings.schedule_meeting()

        self.assertEqual(len(meetings.meeting_list), initial_count + 1)
        new_meeting = meetings.meeting_list[-1]
        self.assertEqual(new_meeting["meeting_id"], "M003")
        self.assertEqual(new_meeting["student_id"], "S003")
        self.assertEqual(new_meeting["student_name"], "Arjun Verma")
        self.assertEqual(new_meeting["mentor_id"], "MTR01")
        self.assertEqual(new_meeting["date"], "2026-12-01")
        self.assertEqual(new_meeting["time"], "11:00")
        self.assertEqual(new_meeting["mode"], "In-Person")
        self.assertEqual(new_meeting["status"], "Scheduled")

    # --------------------------------------------------------------------------
    # Core Operation 2 Tests: View & Search Meetings
    # --------------------------------------------------------------------------
    def test_view_all_meetings(self):
        """Verify view_all_meetings executes without raising an exception."""
        meetings.view_all_meetings()

    @patch("builtins.input", side_effect=["1", "S001"])
    def test_search_by_student_id(self, mock_input):
        """Verify search by student ID works."""
        meetings.search_meetings()

    @patch("builtins.input", side_effect=["2", "MTR02"])
    def test_search_by_mentor_id(self, mock_input):
        """Verify search by mentor ID works."""
        meetings.search_meetings()

    @patch("builtins.input", side_effect=["3", "M002"])
    def test_search_by_meeting_id(self, mock_input):
        """Verify search by meeting ID works."""
        meetings.search_meetings()

    @patch("builtins.input", side_effect=["4", "1"])
    def test_search_by_status_scheduled(self, mock_input):
        """Verify filtering by Scheduled status works."""
        meetings.search_meetings()

    # --------------------------------------------------------------------------
    # Core Operation 3 Tests: Update, Reschedule & Complete Meetings
    # --------------------------------------------------------------------------
    @patch("builtins.input", side_effect=["M002", "1", "2026-12-05", "16:30"])
    def test_update_meeting_reschedule(self, mock_input):
        """Verify rescheduling updates date and time."""
        meetings.update_meeting()
        target = next(m for m in meetings.meeting_list if m["meeting_id"] == "M002")
        self.assertEqual(target["date"], "2026-12-05")
        self.assertEqual(target["time"], "16:30")

    @patch("builtins.input", side_effect=["M002", "2", "Updated Project Scope"])
    def test_update_meeting_agenda(self, mock_input):
        """Verify updating agenda."""
        meetings.update_meeting()
        target = next(m for m in meetings.meeting_list if m["meeting_id"] == "M002")
        self.assertEqual(target["agenda"], "Updated Project Scope")

    @patch("builtins.input", side_effect=["M002", "Project architecture approved by mentor."])
    def test_complete_meeting(self, mock_input):
        """Verify completing a meeting and recording outcomes."""
        meetings.complete_meeting()
        target = next(m for m in meetings.meeting_list if m["meeting_id"] == "M002")
        self.assertEqual(target["status"], "Completed")
        self.assertIn("Project architecture approved by mentor.", target["notes"])

    # --------------------------------------------------------------------------
    # Additional Operations Tests: Cancel, Delete, Report
    # --------------------------------------------------------------------------
    @patch("builtins.input", side_effect=["M002", "Student had an exam conflict"])
    def test_cancel_meeting(self, mock_input):
        """Verify cancelling a meeting."""
        meetings.cancel_meeting()
        target = next(m for m in meetings.meeting_list if m["meeting_id"] == "M002")
        self.assertEqual(target["status"], "Cancelled")
        self.assertIn("Cancelled reason", target["notes"])

    @patch("builtins.input", side_effect=["M001", "y"])
    def test_delete_meeting_confirmed(self, mock_input):
        """Verify deleting a meeting with confirmation."""
        initial_len = len(meetings.meeting_list)
        meetings.delete_meeting()
        self.assertEqual(len(meetings.meeting_list), initial_len - 1)
        self.assertFalse(any(m["meeting_id"] == "M001" for m in meetings.meeting_list))

    @patch("builtins.input", side_effect=["M001", "n"])
    def test_delete_meeting_cancelled(self, mock_input):
        """Verify refusing confirmation cancels deletion."""
        initial_len = len(meetings.meeting_list)
        meetings.delete_meeting()
        self.assertEqual(len(meetings.meeting_list), initial_len)

    def test_meetings_report(self):
        """Verify analytics report calculation."""
        meetings.meetings_report()

    # --------------------------------------------------------------------------
    # Helper & Validation Function Tests
    # --------------------------------------------------------------------------
    def test_generate_meeting_id(self):
        """Verify meeting ID auto-generation correctly formats next ID."""
        new_id = meetings.generate_meeting_id()
        self.assertEqual(new_id, "M003")

    @patch("builtins.input", side_effect=["   ", "Valid Input"])
    def test_get_valid_input_trims_and_rejects_empty(self, mock_input):
        result = meetings.get_valid_input("Enter: ")
        self.assertEqual(result, "Valid Input")

    @patch("builtins.input", side_effect=["not-a-date", "2026-12-15"])
    def test_get_valid_date(self, mock_input):
        result = meetings.get_valid_date("Enter date: ")
        self.assertEqual(result, "2026-12-15")

    @patch("builtins.input", side_effect=["99:99", "15:45"])
    def test_get_valid_time(self, mock_input):
        result = meetings.get_valid_time("Enter time: ")
        self.assertEqual(result, "15:45")


if __name__ == "__main__":
    unittest.main()
