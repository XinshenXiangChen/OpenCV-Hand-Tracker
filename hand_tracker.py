import cv2
import mediapipe as mp
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS


class HandTracker():
    def __init__(self):
        self.cap = (
            cv2.VideoCapture(0)
        )
        self.width = 600
        self.height = 600

        self.hand_drawer = mp.solutions.drawing_utils


        self.hand_tracker = mp.solutions.hands.Hands()

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)


    def track(self):
        # cap read always returns a boolean and a image frame as anumpy ndarray
        while True:
            success, frame = self.cap.read()
            if success:
                rec_hands = self.hand_tracker.process(frame)
                """
                Returns: (etracted from the hand tracker interface)
                  A NamedTuple object with the following fields:
                    1) a "multi_hand_landmarks" field that contains the hand landmarks on
                       each detected hand.
                    2) a "multi_hand_world_landmarks" field that contains the hand landmarks
                       on each detected hand in real-world 3D coordinates that are in meters
                       with the origin at the hand's approximate geometric center.
                    3) a "multi_handedness" field that contains the handedness (left v.s.
                       right hand) of the detected hand.
                """
                if rec_hands.multi_hand_landmarks:
                    for hand_landmarks in rec_hands.multi_hand_landmarks:
                        self.hand_drawer.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                cv2.imshow("hand_tracker", frame)
                if cv2.waitKey(1) == ord('q'):
                    break



if __name__ == "__main__":
    tracker = HandTracker()
    tracker.track()
