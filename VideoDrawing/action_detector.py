import cv2
import mediapipe as mp

from VideoDrawing.Action import LeftHandAction, RightHandAction

hand_enum_reversed = {
    4: "thumb",
    7: "index",
    11: "middle",
    15: "ring",
    19: "pinky",
}

"""
This returns the motion that the user is currently doing.
Element 0 of tuple -> Left hand action
Element 1 of tuple -> Right hand action
"""

def action_detector(landmarks, hand_label):
    fingers_up = {
        "thumb": False,
        "index": False,
        "middle": False,
        "ring": False,
        "pinky": False,
    }

    action = None
    count = 0

    for landmark_id, finger_name in hand_enum_reversed.items():

        if finger_name == "thumb" :
            # goofy ah code such that for the thumnb it compares the tip vs the mcp instead of the ip vs the mcp
            if hand_label == "Right":
                if landmarks.landmark[landmark_id].x < landmarks.landmark[landmark_id - 2].x:
                    count = count + 1
                    fingers_up[finger_name] = True
            else:  # Right hand
                if landmarks.landmark[landmark_id].x > landmarks.landmark[landmark_id - 2].x:
                    count = count + 1
                    fingers_up[finger_name] = True
        else:
            if landmarks.landmark[landmark_id].y < landmarks.landmark[landmark_id - 1].y:

                count = count + 1
                fingers_up[finger_name] = True

    # Right hand with only index finger up = PAINT action
    if hand_label == "Right":
        if count == 1 and fingers_up["index"] == True:
            action = RightHandAction.PAINT

    return action



