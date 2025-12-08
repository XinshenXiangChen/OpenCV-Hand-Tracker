

from BaseHandTracker.hand_tracker import HandTracker
import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk

from action_detector import action_detector
from action_handler import *


class HandDrawer(HandTracker):
    def __init__(self):

        super().__init__()

        root = tk.Tk()
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.destroy()

        self.half_x_screen = int(self.screen_width / 2)
        self.half_y_screen = int(self.screen_height / 2)

        """
        Hand tracking window shows in the left
        """
        cv2.namedWindow("hand_tracker", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("hand_tracker", self.half_x_screen, self.half_y_screen)


        """
        Drawn canvas is shown in the right
        """
        cv2.namedWindow("canvas", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("canvas", self.half_x_screen, self.half_y_screen)
        cv2.moveWindow('canvas', int(self.screen_width/2), 0)

        self.canvas = np.ones((self.half_x_screen, self.half_y_screen, 3), dtype=np.uint8) * 255

    def tracker(self):
        while True:
            success, frame = self.cap.read()
            if success:
                # Flip frame horizontally to fix mirroring
                frame = cv2.flip(frame, 1)
                rec_hands = self.hand_tracker.process(frame)

                if rec_hands.multi_hand_landmarks:
                    for hand_landmarks, handedness in zip(
                            rec_hands.multi_hand_landmarks, rec_hands.multi_handedness):
                        # handedness.classification[0].label is "Left" or "Right"
                        hand_label = handedness.classification[0].label


                        self.plot_to_frame(hand_landmarks, hand_label)
                        self.hand_drawer.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)


                cv2.imshow("hand_tracker", frame)
                if cv2.waitKey(1) == ord('q'):
                    break

    def plot_to_frame(self, hand_landmarks, hand_label):

        action = action_detector(hand_landmarks, hand_label)
        frame = handle_action(action, hand_landmarks, hand_label, self.canvas)
        self.canvas = frame

        cv2.imshow("canvas", self.canvas)



if __name__ == "__main__":
    drawer = HandDrawer()

    drawer.tracker()