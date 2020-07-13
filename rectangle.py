import cv2
from shapes import Myinit

class Rectangle(Myinit):
    def __init__(self):
        super(Rectangle, self).__init__()
        self.point1 = (50, 50)
        self.point2 = (150,100)
        self.color = (255, 0, 0)
        self.thickness = -1

    def form_shape(self):
        self.img = cv2.rectangle(self.img, self.point1, self.point2, self.color, self.thickness)

    def welcome(self):
        print("Printing Rectangle...!")

    def sides(self):
        print("Rectangle has 4 sides.")

    def draw_shape(self):
        self.welcome()
        self.form_shape()
        self.sides()
        cv2.imshow("Rectangle", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()