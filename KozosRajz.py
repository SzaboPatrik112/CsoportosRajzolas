import turtle as t
t.speed(0)
t.color("green")
t.width(3)

i=0
t.left(90)
while i<4:
    t.forward(100)
    t.left(90)
    i+=1
t.forward(100)
i=0
while i<4:
    t.forward(100)
    t.left(90)
    i+=1

t.forward(100)
t.setheading(136)
t.forward(70)
t.setheading(-136)
t.forward(70)
t.penup()
t.setheading(270)
t.forward(100)
t.left(180)
t.forward(30)
t.right(90)
t.forward(30)
i=0
t.pendown()
while i<4:
    t.forward(40)
    t.left(90)
    i+=1
t.forward(20)
t.left(90)
t.forward(40)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(40)
t.penup()
t.left(180)
t.forward(70)
t.left(90)
t.forward(150)

t.done()