import numpy

from VideoDrawing.Action import RightHandAction, LeftHandAction
import cv2

def handle_action(action: RightHandAction | LeftHandAction, hand_landmarks, hand_label, frame) -> numpy.ndarray:


    print("HandLabel: ", hand_label)
    # Again for some reason the handedness detection is flipped
    if hand_label == "Right":
        return handle_right_action(action, hand_landmarks, frame)

    elif hand_label == "Left":
        return handle_left_action(action, hand_landmarks, frame)
    return frame

def handle_right_action(action: RightHandAction, hand_landmarks, frame) -> numpy.ndarray:
    print(action)
    if action is None:
        print("No action")
        return frame

    if action == RightHandAction.PAINT:
        print("Paint action detected!")
        finger_tip = hand_landmarks.landmark[8]
        h, w, _ = frame.shape
        x, y = int(finger_tip.x * w), int(finger_tip.y * h)
        # Ensure coordinates are within bounds
        x = max(0, min(x, w - 1))
        y = max(0, min(y, h - 1))

        cv2.circle(frame, (x, y), radius=20, color=(0, 0, 0), thickness=-1)
        print(f"[PAINT] Drawing at ({x}, {y}) on canvas size {w}x{h}, finger_tip normalized: ({finger_tip.x:.3f}, {finger_tip.y:.3f})")

    return frame

def handle_left_action(action: LeftHandAction, hand_landmarks, frame) -> numpy.ndarray:
    if action is None:
        return frame
    return frame