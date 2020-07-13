import cv2
from shapes import Myinit

class Circle(Myinit):
    def __init__(self):
        super(Circle, self).__init__()
        self.center = (100,100)
        self.radius = 50
        self.color = (0,0,255)
        self.thickness = -1

    def form_shape(self):
        self.img = cv2.circle(self.img, self.center, self.radius, self.color, -1)

    def welcome(self):
        print('Printing Circle...!')

    def sides(self):
        print("Circle has only arcs.")

    def draw_shape(self):
        self.welcome()
        self.form_shape()
        self.sides()
        cv2.imshow("Circle", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()