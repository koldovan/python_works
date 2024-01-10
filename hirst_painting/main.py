import turtle
import random


# import colorgram

# colors= colorgram.extract("pallete.jpg", 40)
#
# rgb_list = []
# for color in colors:
#     r,g, b = color.rgb
#     rgb_list.append((r,g, b))

color_list = [(249, 248, 244), (250, 246, 248), (240, 248, 245), (240, 245, 250), (239, 227, 1), (219, 1, 70),
              (204, 165, 3), (235, 224, 93), (10, 195, 118), (2, 194, 225), (220, 73, 5), (239, 46, 143),
              (228, 159, 96), (15, 109, 181), (15, 28, 181), (108, 179, 220), (11, 25, 69), (218, 132, 176),
              (237, 162, 198), (224, 3, 0), (226, 15, 166), (5, 50, 26), (57, 10, 24), (118, 193, 169), (19, 141, 64),
              (117, 223, 237), (139, 220, 205), (114, 85, 217), (72, 19, 5), (4, 101, 47), (254, 2, 52), (243, 69, 27),
              (166, 181, 234), (240, 169, 154), (2, 87, 106), (254, 3, 2), (25, 39, 244), (59, 104, 4), (1, 245, 241),
              (0, 244, 249)]

tyz = turtle.Turtle()
tyz.speed(0)
tyz.hideturtle()

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor((0,0,0))


def teleport(x_, y_):
    tyz.penup()  # Lift the pen to avoid drawing a line
    tyz.goto(x_, y_)  # Move the turtle to the desired coordinates
    tyz.pendown()  # Put the pen back down to resume drawing


x = -250
y = -250
teleport(x, y)

i = 0
number_of_dots = 100
for _ in range(number_of_dots):
    if i == 10:
        i = 0
        x -= 500
        y += 50
        teleport(x,y)
    tyz.dot(20, random.choice(color_list))
    x += 50
    i += 1
    teleport(x, y)


screen.exitonclick()
