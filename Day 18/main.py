# import colorgram
# colors = colorgram.extract('image.jpg',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(239, 231, 214), (225, 158, 68), (235, 238, 245), (244, 233, 239), (50, 96, 57), (61, 121, 171), (240, 201, 60), (236, 244, 239), (221, 172, 199), (182, 52, 56), (174, 173, 40), (181, 64, 51), (211, 88, 56), (46, 46, 94), (209, 164, 188), (134, 160, 186), (39, 41, 80), (76, 131, 185), (148, 167, 149), (244, 199, 5), (37, 84, 46), (196, 74, 80), (228, 175, 165), (178, 188, 212), (112, 139, 114), (181, 199, 184), (32, 58, 41), (75, 143, 173), (57, 48, 38), (114, 43, 62)]

tim.setpos(10,-120)
tim.setheading(205)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()





