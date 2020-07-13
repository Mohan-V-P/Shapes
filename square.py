import cv2
from shapes import Myinit

class Square(Myinit):
    def __init__(self):
        super(Square, self).__init__()
        self.point1 = (50,50)
        self.point2 = (150,150)
        self.color = (0,255,0)
        self.thickness = -1

    def form_shape(self):
        self.img = cv2.rectangle(self.img, self.point1, self.point2, self.color, self.thickness)

    def welcome(self):
        print('Printing Square...!')

    def sides(self):
        print("Square has 4 sides.")

    def draw_shape(self):
        self.welcome()
        self.form_shape()
        self.sides()
        cv2.imshow("Square", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()