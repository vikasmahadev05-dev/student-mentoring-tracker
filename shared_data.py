"""
Root-level re-export of shared data.
"""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent
src_dir = root_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from data.sample_data import students, mentors, meetings, actions

__all__ = ["students", "mentors", "meetings", "actions"]
