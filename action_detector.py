import cv2
import mediapipe as mp

hand_enum_reversed = {
    4: "thumb",
    7: "index",
    11: "middle",
    15: "ring",
    19: "pinky",
}


def action_detector(landmarks, hand_label):
    fingers_up = {
        "thumb": False,
        "index": False,
        "middle": False,
        "ring": False,
        "pinky": False,
    }

    count = 0
    for landmark_id, finger_name in hand_enum_reversed.items():

        if finger_name == "thumb" :
            # goofy ah code such that for the thumnb it compares the tip vs the mcp instead of the ip vs the mcp
            if hand_label == "left":
                if landmarks.landmark[landmark_id].x < landmarks.landmark[landmark_id - 2].x:
                    count = count + 1
                    fingers_up[finger_name] = True
            else:
                if landmarks.landmark[landmark_id].x > landmarks.landmark[landmark_id - 2].x:
                    count = count + 1
                    fingers_up[finger_name] = True
        else:
            if landmarks.landmark[landmark_id].y < landmarks.landmark[landmark_id - 1].y:

                count = count + 1
                fingers_up[finger_name] = True

    if count == 1 and fingers_up["index"] == True:
        pass





