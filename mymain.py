from line import Line
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle
from ellipse import Ellipse
from pentagon import Pentagon

if __name__ == "__main__":
    line_obj = Line()
    rectangle_obj = Rectangle()
    square_obj = Square()
    circle_obj = Circle()
    triangle_obj = Triangle()
    ellipse_obj = Ellipse()
    
    while True:
        print()
        print("Shapes Available to draw:","1. Line", "2. Rectangle", "3. Square", "4. Circle", "5. Triangle", "6. Ellipse","7. Pentagon","8. Exit", sep='\n',end='\n')
        try:
            num = int(input("Enter your choice: "))
        except:
            print()
            print("Give correct input.")
            continue
        print()
        if num < 1 or num > 7:
            print("Incorrect choice, Choose from 1 to 7:")
            continue
        if num == 1:
            line_obj.draw_shape()
        elif num == 2:
            rectangle_obj.draw_shape()
        elif num == 3:
            square_obj.draw_shape()
        elif num == 4:
            circle_obj.draw_shape()
        elif num == 5:
            triangle_obj.draw_shape()
        elif num == 6:
            ellipse_obj.draw_shape()
        else:
            print("Thank you...!")
            break
