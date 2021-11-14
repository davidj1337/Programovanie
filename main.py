import turtle
from Rectangle import Rectangle
from Triangle import Triangle
from Circle import Circle

t = turtle.Turtle()
t.speed(10)

rectangle = Rectangle(15,15,50,100)
rectangle.setColor("red")
rectangle.draw(t)

rectangle2 = Rectangle(-85,85,200,68)
rectangle2.setColor("blue")
rectangle2.draw(t)

triangle = Triangle(0,0,120)
triangle.setColor("green")
triangle.draw(t)

circle = Circle(0,0,120)
circle.setColor("orange")
circle.draw(t)

turtle.exitonclick()
