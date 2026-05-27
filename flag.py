import turtle
import random

turtle.setup(800, 500)
turtle.bgcolor("white")
t = turtle.Turtle()
t.speed(10)

points = 1
lives = 3

def Japan():
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    t.pensize(3)
    t.color("black")
    for i in range(2):
        t.forward(600)
        t.right(90)
        t.forward(400)
        t.right(90)

    t.penup()
    t.goto(0, -10)
    t.color("red")
    t.begin_fill()
    t.circle(80)
    t.end_fill()

def Armenia():
    t.color("yellow")
    t.penup()
    t.begin_fill()
    t.pd()
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.end_fill()

    t.color("blue")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.end_fill()

    t.color("red")
    t.begin_fill()
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.end_fill()

def Ukraine():
    t.color("yellow")
    t.penup()
    t.begin_fill()
    t.pd()
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.end_fill()

    t.color("blue")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.end_fill()

countries = [Japan, Armenia, Ukraine]
countries.reverse()


flag = random.choice(countries)

while lives > 0 and len(countries) > 0:

    t.reset()
    t.speed(10)
    flag()

    answer = input("give a flag ")


    if answer.lower() == flag.__name__.lower():
        print("Correct")
        points = points + 1


        countries.remove(flag)


        if len(countries) > 0:
            flag = random.choice(countries)
    else:
        print("Wrong")
        lives = lives - 1


    print("Points:", points)
    print("Lives:", lives)

if lives <= 0:
    print("try again")
else:
    print("Bravo! You finished all flags!")

turtle.done()
