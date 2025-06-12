import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


directions = [0,90,100,278]
tim.pensize(15)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
