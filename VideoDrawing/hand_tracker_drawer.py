from Base.hand_tracker import HandTracker
import matplotlib.pyplot as plt


class HandDrawer(HandTracker):
    def __init__(self):
        super.__init__()
        self.graph = plt.figure().add_subplot(projection='3d')


    def tracker(self):
        pass



if __name__ == "__main__":
    drawer = HandDrawer()

    drawer.tracker()