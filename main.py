"""
Student Mentoring Tracker - Main Starting Point
Run this file to start the application:
    python main.py
"""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent
src_dir = root_dir / "src"
for p in [str(root_dir), str(src_dir)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from src.main import main_menu

if __name__ == "__main__":
    main_menu()
