import unittest
from unittest.mock import patch

from src.meeting_management import meetings


class TestMeetingManagement(unittest.TestCase):

    def setUp(self):
        meetings.meeting_list = [
            {
                "meeting_id": "M1",
                "student_id": "101",
                "mentor_name": "Dr. Ramesh",
                "date": "2026-11-20",
                "topic": "Academic Review",
                "status": "Completed"
            },
            {
                "meeting_id": "M2",
                "student_id": "102",
                "mentor_name": "Prof. Anitha",
                "date": "2026-11-28",
                "topic": "Minor Project Discussion",
                "status": "Scheduled"
            }
        ]

    @patch("builtins.input", side_effect=[
        "103",
        "Dr. Ramesh",
        "2026-12-05",
        "Career Guidance"
    ])
    def test_schedule_meeting(self, mock_input):
        initial_count = len(meetings.meeting_list)
        meetings.schedule_meeting()

        self.assertEqual(len(meetings.meeting_list), initial_count + 1)
        new_m = meetings.meeting_list[-1]
        self.assertEqual(new_m["meeting_id"], "M3")
        self.assertEqual(new_m["student_id"], "103")
        self.assertEqual(new_m["mentor_name"], "Dr. Ramesh")
        self.assertEqual(new_m["status"], "Scheduled")

    def test_view_meetings(self):
        meetings.view_meetings()

    @patch("builtins.input", return_value="101")
    def test_search_meetings(self, mock_input):
        meetings.search_meetings()

    @patch("builtins.input", side_effect=["M2", "1", "2026-12-01"])
    def test_update_meeting_date(self, mock_input):
        meetings.update_meeting()
        self.assertEqual(meetings.meeting_list[1]["date"], "2026-12-01")

    @patch("builtins.input", side_effect=["M2", "3"])
    def test_update_meeting_complete(self, mock_input):
        meetings.update_meeting()
        self.assertEqual(meetings.meeting_list[1]["status"], "Completed")

    @patch("builtins.input", return_value="M1")
    def test_delete_meeting(self, mock_input):
        initial_count = len(meetings.meeting_list)
        meetings.delete_meeting()
        self.assertEqual(len(meetings.meeting_list), initial_count - 1)
        self.assertFalse(any(m["meeting_id"] == "M1" for m in meetings.meeting_list))


if __name__ == "__main__":
    unittest.main()
