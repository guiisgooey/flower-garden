from polygon import polygon
from flower import flower
import turtle
from rose import rose

def time():
    """asks user for what time of day it is and sets the background accordingly along with the ground"""
    global turtle
    time_color = ""
    time = ""
    while True:
        try:
            time = input("Is it daytime or nighttime?")
            if time != "daytime" and time != "nighttime":
                raise ValueError
            else:
                break
        except ValueError:
            print("Please select daytime or nighttime")

    if time == "daytime":
        time_color = "sky blue"
    elif time == "nighttime":
        time_color = "midnight blue"
    turtle.speed(10)
    turtle.bgcolor(time_color)
    turtle.up()
    turtle.pencolor("forest green")
    turtle.fillcolor("forest green")
    turtle.setpos(-1000,0)
    turtle.down()
    turtle.begin_fill()
    for r in range(2): 
        turtle.forward(2000)
        turtle.right(90)
        turtle.forward(1000)
        turtle.right(90)
    turtle.end_fill()

s1 = turtle.Screen()
s1.title("🌸 Flower Garden 🌸")

print("Welcome to your garden!")
time()

turtle.colormode(255)
p1 = polygon(10, 0, 0, 255, 5, 100, 4, 250, -150)

f1 = flower(10, 0, 0, 255, 5, 100, 4, 250, -150)
f2 = flower(10, 255, 255, 0, 3, 100, 4, -300, -350)
f3 = flower(10, 255, 0, 0, 10, 100, 4, -40, 0)

r1 = rose(10, 255, 0, 255, 2, 100, 5, -40, -300)
r2 = rose(10, 255, 255, 255, 2, 100, 7, -200, -350)
r3 = rose(10, 255, 0, 0, 2, 50, 9, -400, -200)

assert p1.get_turn_degrees(3) == 120
assert f1.get_turn_degrees(4) == 140
assert r1.get_turn_degrees(5) == 72

f1.draw()
f2.draw()
f3.draw()
r1.draw()
r2.draw()
r3.draw()
turtle.done()


