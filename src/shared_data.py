"""
Shared Data access for Student Mentoring Tracker.
Provides unified in-memory storage referenced across all modules.
"""

import sys
from pathlib import Path

# Setup paths so data.sample_data can be imported regardless of execution working directory
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from data.sample_data import students, mentors, meetings, actions

__all__ = ["students", "mentors", "meetings", "actions"]
