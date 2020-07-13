import cv2
from shapes import Myinit

class Line(Myinit):
    def __init__(self):
        super(Line, self).__init__()
        self.point1 = (50, 50)
        self.point2 = (150, 50)
        self.color = (255, 255, 255)
        self.thickness = 5

    def form_shape(self):
        self.img = cv2.rectangle(self.img, self.point1, self.point2, self.color, self.thickness)

    def welcome(self):
        print("Printing Line...!")

    def sides(self):
        print("Line has 2 points.")

    def draw_shape(self):
        self.welcome()
        self.form_shape()
        self.sides()
        cv2.imshow("Line", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()