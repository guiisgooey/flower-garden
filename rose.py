from flower import flower
import turtle as pen

class rose(flower):

  def get_turn_degrees(self, sides):
      """gets the amount of degrees needed for the next left turn to draw the spiral/reverse spiral"""
      interior_angle = ((180*(sides - 2))/sides)
      exterior_angle = (180-interior_angle)
      return exterior_angle

  def draw_stem(self):
    """draws a stem for the flower object"""
    global pen
    pen.seth(0)
    pen.up()
    pen.goto(self.x + self.length*1.5, self.y + self.length)
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
    """draws a spiral and reverse spiral resembling a rose"""
    global pen
    pen.seth(0)
    pen.speed(self.speed)
    pen.width(self.size)
    self.draw_stem()
    pen.up()
    pen.goto(self.x + self.length, self.y + self.length)
    inverted = self.invert(self.r, self.g, self.b)
    pen.pencolor(self.r, self.g, self.b)
    pen.fillcolor(inverted)
    pen.down()
    pen.begin_fill()
    for r in range(self.length*2):
        pen.forward(self.length)
        pen.left(self.get_turn_degrees(self.sides))
        self.length -=1
    pen.end_fill()
    pen.seth(0)
    return

