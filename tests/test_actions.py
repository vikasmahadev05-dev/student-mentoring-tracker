
import unittest
from datetime import date
from unittest.mock import patch

from src.action_management import actions


class TestActionManagement(unittest.TestCase):

    def setUp(self):
        actions.action_list.clear()

    # Test creating an action item
    @patch("builtins.input", side_effect=[
        "S001", "M001", "Python Assignment",
        "2026-11-25", "2026-11-24"
    ])
    def test_create_action(self, mock_input):

        actions.create_action()

        self.assertEqual(len(actions.action_list), 1)
        self.assertEqual(actions.action_list[0]["student_id"], "S001")
        self.assertEqual(actions.action_list[0]["status"], "Pending")

    # Test viewing all actions
    def test_view_actions(self):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": "M001",
            "description": "Python Assignment",
            "assigned_date": str(date.today()),
            "due_date": "2026-11-25",
            "follow_up_date": "2026-11-24",
            "status": "Pending"
        })

        actions.view_actions()

    # Test searching actions
    @patch("builtins.input", return_value="S001")
    def test_search_actions(self, mock_input):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": None,
            "description": "Python Assignment",
            "assigned_date": str(date.today()),
            "due_date": "2026-11-25",
            "follow_up_date": "2026-11-24",
            "status": "Pending"
        })

        actions.search_actions()

    # Test updating an action description
    @patch("builtins.input", side_effect=["A001", "1", "Updated Assignment"])
    def test_update_action(self, mock_input):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": None,
            "description": "Python Assignment",
            "assigned_date": str(date.today()),
            "due_date": "2026-11-25",
            "follow_up_date": "2026-11-24",
            "status": "Pending"
        })

        actions.update_action()

        self.assertEqual(
            actions.action_list[0]["description"],
            "Updated Assignment"
        )

    # Test completing an action
    @patch("builtins.input", return_value="A001")
    def test_complete_action(self, mock_input):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": None,
            "description": "Python Assignment",
            "assigned_date": str(date.today()),
            "due_date": "2026-11-25",
            "follow_up_date": "2026-11-24",
            "status": "Pending"
        })

        actions.complete_action()

        self.assertEqual(actions.action_list[0]["status"], "Completed")

    # Test viewing pending actions
    def test_view_pending_actions(self):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": None,
            "description": "Python Assignment",
            "assigned_date": str(date.today()),
            "due_date": "2026-11-25",
            "follow_up_date": "2026-11-24",
            "status": "Pending"
        })

        actions.view_pending_actions()

    # Test viewing completed actions
    def test_view_completed_actions(self):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": None,
            "description": "Python Assignment",
            "assigned_date": str(date.today()),
            "due_date": "2026-11-25",
            "follow_up_date": "2026-11-24",
            "status": "Completed"
        })

        actions.view_completed_actions()

    # Test identifying overdue actions
    def test_get_overdue_actions(self):

        actions.action_list.append({
            "action_id": "A001",
            "student_id": "S001",
            "meeting_id": None,
            "description": "Python Assignment",
            "assigned_date": "2026-11-18",
            "due_date": "2026-11-18",
            "follow_up_date": "2026-11-19",
            "status": "Pending"
        })

        actions.get_overdue_actions()

    # Test that completed actions are not overdue
    def test_completed_action_not_overdue(self):

        actions.action_list.append({
            "action_id": "A002",
            "student_id": "S002",
            "meeting_id": None,
            "description": "MCA Project",
            "assigned_date": "2026-11-18",
            "due_date": "2026-11-18",
            "follow_up_date": "2026-11-19",
            "status": "Completed"
        })

        actions.get_overdue_actions()


if __name__ == "__main__":
    unittest.main()
