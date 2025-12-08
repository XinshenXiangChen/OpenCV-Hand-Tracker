import sys
from BaseHandTracker.hand_tracker import HandTracker
from VideoDrawing.action_tracker import HandDrawer

options = {
    "fuck67": HandTracker(),
    "base": HandTracker(),
    "drawer": HandDrawer()
}

def print_instructions():
    print("""
    This is a hand detection program with different options. 
    To choose the option run the program with:
    python main.py option

     - 6 7 destroyer:
    python main.py fuck67

     - base hand tracker
     python main.py base
    """)

def get_option(option: str) -> HandTracker:
    return options[option]

if __name__ == '__main__':
    print_instructions()

    if sys.argv.__len__() == 2:
        tracker_type = get_option(sys.argv[1])
        tracker = tracker_type.track()



