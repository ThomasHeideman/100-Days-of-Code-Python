from random import choice
from turtle import Turtle, Screen, colormode, speed, dot, goto
import colorgram

# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_color = (r, g, b)
#     color_list.append(rgb_color)
#
screen = Screen()
screen.colormode(255)
color_palette = [ (198, 65, 14), (18, 28, 59), (21, 94, 60), (81, 25, 17), (54, 93, 163), (236, 74, 32), (170, 55, 118), (253, 219, 17), (30, 118, 21), (74, 161, 210), (128, 26, 8), (82, 196, 117), (21, 50, 116), (63, 26, 29), (146, 133, 41), (46, 139, 217), (201, 146, 126), (15, 66, 34), (252, 223, 1), (193, 141, 160), (134, 32, 59), (183, 86, 127), (82, 164, 108), (235, 172, 160), (160, 210, 172), (16, 100, 103)]

def random_color():
   return choice(color_palette)
pen = Turtle()



screen_width =screen.window_width()
print(screen_width)
dot_size = 20
gap_size = 50 #(screen_width - dot_size) / 9

total_distance = 9 * gap_size

pos_x = -225 # -(total_distance / 2) - gap_size
pos_y = -220 # -(total_distance / 2) - gap_size

pen.penup()

for row in range(10):
    current_y = pos_y + (row * gap_size)
    pen.goto(pos_x, current_y)
    for dot in range(10):
        pen.dot(dot_size, random_color())
        if dot < 9:
            pen.forward(gap_size)
pen.hideturtle()

screen.exitonclick()