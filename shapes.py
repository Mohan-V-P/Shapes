import numpy as np

class Myinit:
    def __init__(self):
        self.img = np.zeros([300,300,3], np.uint8)
        self.color = (0,0,0)
        self.thickness=0

    def form_shape(self):
        pass

    def draw_shape(self):
        pass

    def welcome(self):
        print("Print shape:")

    def sides(self):
        print("Print sides:")
