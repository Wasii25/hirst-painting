import colorgram
import turtle as t
import random
rgb_colors = []
colors = colorgram.extract('OIP.jpeg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(215, 171, 128), (131, 74, 56), (53, 102, 152), (156, 180, 190), (117, 82, 93), (178, 149, 158),
              (159, 105, 149), (43, 48, 66), (130, 173, 120), (64, 11, 29), (84, 96, 183), (83, 131, 107),
              (223, 190, 149), (190, 92, 76), (52, 63, 78), (113, 45, 58), (66, 55, 45), (207, 182, 192),
              (97, 143, 119), (213, 182, 176), (71, 66, 53), (177, 186, 214), (181, 201, 182), (77, 58, 54),
              (172, 198, 203), (42, 69, 84)]

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
tim.pendown()
for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()
screen = t.Screen()
screen.exitonclick()