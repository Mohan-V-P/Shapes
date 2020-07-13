import cv2
from shapes import Myinit

class Ellipse(Myinit):
    def __init__(self):
        super(Ellipse, self).__init__()
        self.center = (100,100)
        self.axis = (100, 50)
        self.color = (255,255,0)
        self.thickness = -1 
    
    def form_shape(self):
        self.img = cv2.ellipse(self.img, self.center, self.axis, 0, 0, 360, self.color,self.thickness)

    def welcome(self):
        print('Printing Ellipse...!')

    def sides(self):
        print("Ellipse have foci.")

    def draw_shape(self):
        self.welcome()
        self.form_shape()
        self.sides()
        cv2.imshow("Ellipse",self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
