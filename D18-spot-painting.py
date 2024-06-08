import turtle as t
import random
import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('spot_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(243, 246, 250), (252, 245, 248), (219, 153, 108), (132, 172, 195), (221, 72, 88), (213, 132, 150), (26, 119, 151), (240, 208, 99), (122, 176, 148), (39, 119, 84), (20, 164, 203), (140, 86, 63), (219, 85, 78), (134, 81, 99), (174, 185, 216), (236, 161, 173), (25, 167, 123), (162, 209, 168), (171, 152, 76), (5, 95, 115), (237, 169, 154), (54, 60, 93), (155, 206, 218), (35, 59, 78), (34, 85, 56), (94, 129, 176), (235, 214, 14), (73, 77, 46)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()
