from random import randrange
import turtle

def stvorec():
    dlzka = randrange(20,300)
    t.pencolor("blue")
    for i in range(4):
        t.fd(dlzka)
        t.lt(90)

def trojuholnik():
    dlzka2 = randrange(20,300)
    t.pencolor("red")
    t.fd(dlzka2)
    t.lt(120)
    t.fd(dlzka2)
    t.lt(120)
    t.fd(dlzka2)
    t.lt(120)

def poloha():
    polohax = randrange(-100,300)
    polohay = randrange(-100,300)
    t.setpos(polohax,polohay)
t = turtle.Turtle()
for i in range(randrange(10,100)):
    t.penup()
    poloha()
    t.pendown()
    predmet = randrange(0,100)
    if (predmet >= 50):
        stvorec()
    else:
        trojuholnik()

turtle.exitonclick()
