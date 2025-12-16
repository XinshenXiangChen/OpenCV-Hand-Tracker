import numpy

from VideoDrawing.Action import RightHandAction, LeftHandAction
import cv2

brush_size = 15
brush_size_step = 2

brush_color = (0, 0, 0)
erase_color = (255, 255, 255)


def handle_action(action: RightHandAction | LeftHandAction, hand_landmarks, hand_label, frame) -> numpy.ndarray:


    if hand_label == "Right":
        return handle_right_action(action, hand_landmarks, frame)
    elif hand_label == "Left":
        return handle_left_action(action, hand_landmarks, frame)
    return frame

def handle_right_action(action: RightHandAction, hand_landmarks, frame) -> numpy.ndarray:
    global brush_size
    global brush_size_step

    global brush_color
    global erase_color

    if action is None:
        return frame

    if action == RightHandAction.PAINT:
        finger_tip = hand_landmarks.landmark[8]
        h, w, _ = frame.shape
        x, y = int(finger_tip.x * w), int(finger_tip.y * h)
        # Ensure coordinates are within bounds
        x = max(0, min(x, w - 1))
        y = max(0, min(y, h - 1))

        cv2.circle(frame, (x, y), radius=brush_size, color=brush_color, thickness=-1)

    elif action == RightHandAction.ERASE:
        finger_tip = hand_landmarks.landmark[12]
        h, w, _ = frame.shape
        x, y = int(finger_tip.x * w), int(finger_tip.y * h)
        # Ensure coordinates are within bounds
        x = max(0, min(x, w - 1))
        y = max(0, min(y, h - 1))

        cv2.circle(frame, (x, y), radius=brush_size, color=erase_color, thickness=-1)


    return frame

def handle_left_action(action: LeftHandAction, hand_landmarks, frame) -> numpy.ndarray:
    global brush_size
    global brush_size_step

    global brush_color
    global erase_color

    if action is None:
        return frame
    return frame