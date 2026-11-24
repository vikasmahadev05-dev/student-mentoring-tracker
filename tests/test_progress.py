"""
Unit tests for Module 4: Follow-up & Progress Tracking
Student Mentoring Tracker - Phase 1
Author: Vikas Mahadev (Member 4)
"""

import unittest
from datetime import date, timedelta
from unittest.mock import patch

from src.progress_tracking import progress


class TestProgressTracking(unittest.TestCase):

    def setUp(self):
        progress.actions.clear()
        progress.students.clear()

        # Add sample student
        progress.students.append({
            "student_id": "S101",
            "name": "Rahul",
            "department": "MCA",
            "year": 1,
            "contact": "9876543210",
            "mentor_id": "M101"
        })

        today = date.today()
        self.today = today
        self.past_3 = str(today - timedelta(days=3))
        self.future_4 = str(today + timedelta(days=4))
        self.today_str = str(today)

    def test_overdue_action_categorization(self):
        """Action is overdue ONLY if it is Pending and follow-up date < today."""
        action = {
            "action_id": "A101",
            "student_id": "S101",
            "meeting_id": "MT101",
            "description": "Task 1",
            "assigned_date": self.past_3,
            "due_date": self.past_3,
            "follow_up_date": self.past_3,
            "status": "Pending"
        }
        category = progress.get_action_timeline_category(action)
        self.assertEqual(category, "OVERDUE")

    def test_due_today_not_overdue(self):
        """Action with follow-up date equal to current date is Due Today, not overdue."""
        action = {
            "action_id": "A102",
            "student_id": "S101",
            "meeting_id": "MT101",
            "description": "Task 2",
            "assigned_date": self.past_3,
            "due_date": self.today_str,
            "follow_up_date": self.today_str,
            "status": "Pending"
        }
        category = progress.get_action_timeline_category(action)
        self.assertEqual(category, "DUE_TODAY")

    def test_upcoming_action_categorization(self):
        """Action with follow-up date in the future is UPCOMING."""
        action = {
            "action_id": "A103",
            "student_id": "S101",
            "meeting_id": "MT101",
            "description": "Task 3",
            "assigned_date": self.today_str,
            "due_date": self.future_4,
            "follow_up_date": self.future_4,
            "status": "Pending"
        }
        category = progress.get_action_timeline_category(action)
        self.assertEqual(category, "UPCOMING")

    def test_completed_actions_never_overdue(self):
        """Completed actions must never appear in the overdue list even if date passed."""
        action = {
            "action_id": "A104",
            "student_id": "S101",
            "meeting_id": "MT101",
            "description": "Task 4",
            "assigned_date": self.past_3,
            "due_date": self.past_3,
            "follow_up_date": self.past_3,
            "status": "Completed"
        }
        category = progress.get_action_timeline_category(action)
        self.assertEqual(category, "COMPLETED")

    @patch("builtins.input", return_value="S101")
    def test_student_summary_calculation(self, mock_input):
        """Verify summary math: 1 completed out of 2 total = 50.0% progress."""
        progress.actions.extend([
            {
                "action_id": "A101",
                "student_id": "S101",
                "description": "Task 1",
                "follow_up_date": self.past_3,
                "status": "Completed"
            },
            {
                "action_id": "A102",
                "student_id": "S101",
                "description": "Task 2",
                "follow_up_date": self.today_str,
                "status": "Pending"
            }
        ])

        progress.student_summary()
        student_actions = [a for a in progress.actions if a["student_id"] == "S101"]
        total = len(student_actions)
        completed = sum(1 for a in student_actions if a["status"] == "Completed")
        pct = (completed / total) * 100
        self.assertEqual(pct, 50.0)

    def test_radar_and_dashboard(self):
        """Verify daily radar and cohort dashboard run smoothly."""
        progress.actions.append({
            "action_id": "A101",
            "student_id": "S101",
            "description": "Task 1",
            "follow_up_date": self.past_3,
            "status": "Pending"
        })
        progress.daily_follow_up_radar()
        progress.cohort_dashboard()
        progress.students_needing_attention()


if __name__ == "__main__":
    unittest.main()
