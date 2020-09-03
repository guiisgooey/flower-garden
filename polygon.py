import turtle as pen

class polygon:

    def __init__(self, speed, r, g, b, size, length, sides, x, y):
        """initializes a polygon object with the given values"""
        self.speed = speed
        self.r = r
        self.g = g
        self.b = b
        self.size = size
        self.length = length
        self.sides = sides
        self.x = x
        self.y = y
    
    def get_turn_degrees(self, sides):
        """gets the amount of degrees needed for the next left turn to draw the polygon"""
        interior_angle = ((180*(sides - 2))/sides)
        exterior_angle = (180-interior_angle)
        return exterior_angle

    def draw(self):
        """draws a polygon using the given values"""
        global pen
        pen.seth(0)
        pen.up()
        pen.goto(self.x, self.y)
        pen.pencolor(self.r, self.g, self.b)
        pen.fillcolor(self.r, self.g, self.b)
        pen.speed(self.speed)
        pen.width(self.size)
        pen.down()
        pen.begin_fill()
        for r in range(self.sides):
            pen.forward(self.length)
            pen.left(self.get_turn_degrees(self.sides))
        pen.end_fill()
        pen.seth(0)
        return
