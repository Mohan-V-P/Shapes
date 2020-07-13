import cv2
import numpy as np
from shapes import Myinit

class Triangle(Myinit):
    def __init__(self):
        super(Triangle, self).__init__()
        self.vertices = np.array([[100,50], [150,150], [50,150]],np.int32)
        self.vertices = self.vertices.reshape((-1, 1, 2))
        self.color=(255,0,255)

    def form_shape(self):
        self.img = cv2.polylines(self.img, [self.vertices], True, self.color)
        cv2.fillPoly(self.img, [self.vertices], self.color)

    def welcome(self):
        print('Printing Triangle...!')

    def sides(self):
        print("Triangle has 3 sides.")

    def draw_shape(self):
        self.welcome()
        self.form_shape()
        self.sides()
        cv2.imshow("Triangle", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
