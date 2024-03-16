class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self):
        self.length = ((self.start.x-self.end.x)**2+(self.start.y-self.end.y)**2)**(1/2)
        return (self.length)
    #The length is computed considering the distance between two points formula: ((x2-x1)^2+(y2-y1)^2)^0.5
    
    def compute_slope(self):
        vertical_change = (self.start.y-self.end.y)
        horizontal_change = (self.start.x-self.end.x)
        if (self.start.x-self.end.x)==0:
            return "The line is vertical, hence the slope is undefined."
        else:
            self.slope = vertical_change/horizontal_change
            return "The line's slope is: " + str(self.slope)
    #The slope is computed taking into account that it is found by dividing the vertical change (rise) by the horizontal change (run)
    
    def compute_vertical_cross(self):
        if (self.start.x-self.end.x)==0:
            return("The line is vertical, hence it has no y-intercept")
        else:
            self.intercept_y = self.start.y-(self.slope*self.start.x)
            #The method to calculate the intercept is based on the formula: y=mx+b, where b is the y-intercept
            if self.intercept_y>=self.start.y and self.intercept_y<= self.end.y or self.intercept_y<=self.start.y and self.intercept_y>=self.end.y:
                return "It exists the intersection with y-axis"
            #When the y-intercept is between the start point (y-coordinate) and the end point (y-coordinate) of the line, the intersection exists
            else:
                return "It doesn't exist the intersection with y-axis"
            
    def compute_horizontal_cross(self):
        if (self.start.x-self.end.x)==0:
            self.intercept_x = self.start.x
        #When the line is vertical, the x-intercept is the same as the x-coordinate of the points
        elif self.slope==0:
            return "It doesn't exist the intersection with x-axis"
        #When the line is horizontal, there is not intersection with x-axis
        else:
            self.intercept_x = -self.intercept_y/self.slope
        #The method to calculate the intercept is based on the formula: y=mx+b, where y=0 and b=y-intercept
        if self.intercept_x>=self.start.x and self.intercept_x<= self.end.x or self.intercept_x<=self.start.x and self.intercept_x>=self.end.x:
            return "It exists the intersection with x-axis"
            #When the x-intercept is between the start point (x-coordinate) and the end point (x-coordinate) of the line, the intersection exists
        else:
            return "It doesn't exist the intersection with x-axis"

class Rectangle:
    def __init__(self, method:int, *args):
        if method==1:#The rectangle is initialized with the bottom-left corner(Point), the width and the height
            self.bottom = Point(args[0], args[1])#args[0]=bottom left corner x-coordinate and args[1]=bottom left corner y-coordinate
            self.width = args[2]
            self.height = args[3]
        elif method==2:#The rectangle is initialized with the center(Point), the width and the height
            self.bottom = Point(args[0]-(args[2]/2), (args[1]-(args[3]/2)))#The center coordinates are turned into bottom left corner coordinates
            self.width = args[2]
            self.height = args[3]
        elif method==3:#The rectangle is initialized with two opposite corners(Points)
            if args[0]<args[2]:#When the x-coordinate of the first point is less than the one of the second point given by the user
                self.width = (args[2]-args[0])#width is the x-coordinate of the second point given minus the x-coordinate of the first point
                if args[1]<args[3]:#When the y-coordinate of the first point is less than the one of the second point given by the user
                    self.bottom = Point(args[0], args[1])#The bottom left corner has the same coordinates as the first point given 
                    self.height = (args[3]-args[1])#height is the y-coordinate of the second point given minus the y-coordinate of the first point
                else:
                    self.bottom = Point(args[0], args[3])#The bottom left corner has the x-coordinate of the first point and the y-coordinate of the second one
                    self.height = (args[1]-args[3])#height is the y-coordinate of the first point given minus the y-coordinate of the second point
            else:
                self.width = (args[0]-args[2])#width is the x-coordinate of the first point given minus the x-coordinate of the second point
                if args[1]<args[3]:#When the y-coordinate of the first point is less than the one of the second point given by the user 
                    self.bottom = Point(args[2], args[1])#The bottom left corner has the x-coordinate of the second point and the y-coordinate of the first point
                    self.height = (args[3]-args[1])#height is the y-coordinate of the second point given minus the y-coordinate of the first point
                else:#
                    self.bottom = Point(args[2], args[3])#The bottom left corner has the same coordinates as the second point given 
                    self.height = (args[1]-args[3])#height is the y-coordinate of the first point given minus the y-coordinate of the second point
        elif method==4:#The rectangle is initialized with four lines
            #There is a specific order to insert the lines; the 1st line is the bottom edge, the 2nd is the right edge, the 3rd the upper edge and the 4th the left edge.
            self.bottom = Point(args[0].start.x, args[0].start.y)#The bottom left corner is the same as the start point of the first line
            horizontal_line = args[0]#args[0]=line one=bottom edge
            vertical_line = args[1]#args[1]=line two=right edge
            self.width = (horizontal_line.compute_length())
            self.height = (vertical_line.compute_length())

    def compute_area(self):
        print("El área es " + str(self.width*self.height))
    
    def compute_perimeter(self):
        print("El perímetro es " + str(self.width*2+self.height*2))

    def compute_interference_point(self, Point):
        isInside = Point.x>=self.bottom.x and Point.x<=(self.width+self.bottom.x) and Point.y>=self.bottom.y and Point.y<=(self.height+self.bottom.y)
        print(isInside)

class Square(Rectangle):
    def __init__(self, method:int, *args):
        super().__init__(method, *args)

point = Point(-8,-2)
rectangle_one = Rectangle(1, -10, -4, 10, 6) #method, bottom-left.x, bottom-left.y, width, height
rectangle_two = Rectangle(2, -5,-2,10,8) #method, center.x, center.y, width, height
rectangle_three = Rectangle(3, 8,-2,-4,8)#method, opposite1.x, opposite1.y, opposite2.x, opposite2.y
rectangle_four = Rectangle(4, Line(Point(-2,-2), Point(2,-2)), Line(Point(2,-2), Point(2,1)), Line(Point(2,1), Point(-2, 1)), Line(Point(-2,1), Point(-2,-2)))#method, line 1(bottom edge), line 2(right edge), line 3(upper edge), line 4(left edge)
square = Square(3,-4,8,4,0)

rectangle_one.compute_area()
rectangle_one.compute_perimeter()
rectangle_one.compute_interference_point(point)

rectangle_two.compute_area()
rectangle_two.compute_perimeter()
rectangle_two.compute_interference_point(point)

rectangle_three.compute_area()
rectangle_three.compute_perimeter()
rectangle_three.compute_interference_point(point)

rectangle_four.compute_area()
rectangle_four.compute_perimeter()
rectangle_four.compute_interference_point(point)

square.compute_area()
square.compute_perimeter()
square.compute_interference_point(point)


line = Line(Point(-50,-20), Point(10,10))

print(line.compute_length())
print(line.compute_slope())
print(line.compute_vertical_cross())
print(line.compute_horizontal_cross())