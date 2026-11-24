"""
Unit tests for Module 1: Student and Mentor Management
Student Mentoring Tracker - Phase 1
Author: Member 1
"""

import unittest
from unittest.mock import patch

from src.student_management import students


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        students.students.clear()
        students.mentors.clear()

        students.mentors.append({
            "mentor_id": "M101",
            "name": "Dr. Kumar",
            "department": "MCA",
            "contact": "9876543211"
        })

    @patch("builtins.input", side_effect=["S101", "Rahul", "MCA", "1", "9876543210", "y", "M101"])
    def test_add_student(self, mock_input):
        students.add_student()
        self.assertEqual(len(students.students), 1)
        self.assertEqual(students.students[0]["student_id"], "S101")
        self.assertEqual(students.students[0]["mentor_id"], "M101")

    @patch("builtins.input", side_effect=["M102", "Prof. Anitha", "MCA", "9876543212"])
    def test_add_mentor(self, mock_input):
        students.add_mentor()
        self.assertEqual(len(students.mentors), 2)
        self.assertEqual(students.mentors[1]["mentor_id"], "M102")

    @patch("builtins.input", side_effect=["S102", "M101"])
    def test_assign_mentor(self, mock_input):
        students.students.append({
            "student_id": "S102",
            "name": "Priya",
            "department": "MCA",
            "year": 1,
            "contact": "9876543222",
            "mentor_id": None
        })
        students.assign_mentor()
        self.assertEqual(students.students[0]["mentor_id"], "M101")


if __name__ == "__main__":
    unittest.main()
