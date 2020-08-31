from polygon import polygon
import turtle as pen

class flower(polygon):
    """instantiates a flower object with the given values, inheriting from polygon"""
    def __init__(self, speed, r, g, b, size, length, sides, x, y):
        super().__init__(speed, r, g, b, size, length, sides, x, y)

    def get_turn_degrees(self, sides):
        """gets the amount of degrees needed for the next left turn to draw the star polygon"""
        interior_angle = ((180*(sides/2))/sides)
        exterior_angle = (180-interior_angle) + 50
        return exterior_angle
    
    def invert(self, r, g, b):
        """inverts the given r, g, and b values"""
        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        return(new_r, new_g, new_b)

    def draw_interior(self):
        """draws a smaller version of the star polygon inside the original, resembling a flower center"""
        global pen
        pen.seth(0)
        pen.up()
        pen.goto((self.x + self.length/4), (self.y + self.length/10))
        inverted = self.invert(self.r, self.g, self.b)
        pen.pencolor(inverted)
        pen.fillcolor(inverted)
        pen.down()
        pen.begin_fill()
        for r in range(self.sides*5):
            pen.forward(self.length/2)
            pen.left(self.get_turn_degrees(self.sides))
        pen.end_fill()
        pen.seth(0)
        return
    
    def draw_leaf(self):
        """draws a leaf for the stem of the flower object"""
        global pen
        pen.seth(0)
        pen.fillcolor(self.r, self.g, self.b)
        pen.begin_fill()
        pen.left(30)
        pen.forward(self.length/5)
        pen.right(60)
        pen.forward(self.length/5)
        pen.right(120)
        pen.forward(self.length/5)
        pen.right(60)
        pen.forward(self.length/5)
        pen.end_fill()
        pen.seth(0)
        return

    def draw_stem(self):
        """draws a stem for the flower object"""
        global pen
        pen.seth(0)
        pen.up()
        pen.goto(self.x + self.length /2, self.y)
        inverted = self.invert(self.r, self.g, self.b)
        pen.pencolor(inverted)
        pen.down()
        pen.right(90)
        pen.forward(self.length/2)
        self.draw_leaf()
        pen.pencolor(inverted)
        pen.right(90)
        pen.forward(self.length/2)
        pen.seth(0)
        return

    def draw(self):
        """draws a star polygon resembling a flower"""
        global pen
        pen.seth(0)
        pen.speed(self.speed)
        pen.width(self.size)
        self.draw_stem()
        pen.up()
        pen.goto(self.x, self.y)
        pen.pencolor(self.r, self.g, self.b)
        pen.fillcolor(self.r, self.g, self.b)
        pen.down()
        pen.begin_fill()
        for r in range(self.sides*5):
            pen.forward(self.length)
            pen.left(self.get_turn_degrees(self.sides))
        pen.end_fill()
        self.draw_interior()
        pen.seth(0)
        return


