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
t.setheading(135)
t.forward(70)
t.setheading(-135)
t.forward(70)
t.done()