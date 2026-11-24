"""
Unit Tests for Meetings Module (Simple Procedural Implementation)
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
                "student_id": "101",
                "mentor_name": "Dr. Ramesh",
                "date": "2026-11-20",
                "topic": "Academic Review",
                "status": "Completed"
            },
            {
                "meeting_id": "M002",
                "student_id": "102",
                "mentor_name": "Prof. Anitha",
                "date": "2026-11-28",
                "topic": "Minor Project Discussion",
                "status": "Scheduled"
            }
        ]

    # Test Core Operation 1: Schedule Meeting
    @patch("builtins.input", side_effect=[
        "103",                 # Student ID
        "Dr. Ramesh",          # Mentor Name
        "2026-12-05",          # Date
        "Career Guidance"      # Topic
    ])
    def test_schedule_meeting(self, mock_input):
        initial_count = len(meetings.meeting_list)
        meetings.schedule_meeting()

        self.assertEqual(len(meetings.meeting_list), initial_count + 1)
        new_m = meetings.meeting_list[-1]
        self.assertEqual(new_m["meeting_id"], "M003")
        self.assertEqual(new_m["student_id"], "103")
        self.assertEqual(new_m["mentor_name"], "Dr. Ramesh")
        self.assertEqual(new_m["status"], "Scheduled")

    # Test Core Operation 2: View All Meetings
    def test_view_meetings(self):
        meetings.view_meetings()

    # Test Core Operation 2: Search Meetings by Student ID
    @patch("builtins.input", return_value="101")
    def test_search_meetings(self, mock_input):
        meetings.search_meetings()

    # Test Core Operation 3: Update Meeting Date
    @patch("builtins.input", side_effect=["M002", "1", "2026-12-01"])
    def test_update_meeting_date(self, mock_input):
        meetings.update_meeting()
        self.assertEqual(meetings.meeting_list[1]["date"], "2026-12-01")

    # Test Core Operation 3: Update Meeting Status to Completed
    @patch("builtins.input", side_effect=["M002", "3"])
    def test_update_meeting_complete(self, mock_input):
        meetings.update_meeting()
        self.assertEqual(meetings.meeting_list[1]["status"], "Completed")

    # Test Delete Meeting
    @patch("builtins.input", return_value="M001")
    def test_delete_meeting(self, mock_input):
        initial_count = len(meetings.meeting_list)
        meetings.delete_meeting()
        self.assertEqual(len(meetings.meeting_list), initial_count - 1)
        self.assertFalse(any(m["meeting_id"] == "M001" for m in meetings.meeting_list))


if __name__ == "__main__":
    unittest.main()
