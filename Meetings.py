"""
Meetings.py - Entry Point for Meeting Management Module
Student Mentoring Tracker (MCA Minor Project - Phase 1)
Member 2: Meetings Module
"""

import os
import sys

# Ensure repository root is on Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.meeting_management.meetings import (
    meeting_list,
    schedule_meeting,
    view_all_meetings,
    search_meetings,
    update_meeting,
    complete_meeting,
    cancel_meeting,
    delete_meeting,
    meetings_report,
    meeting_menu
)

if __name__ == "__main__":
    meeting_menu()
