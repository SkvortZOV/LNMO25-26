import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
def tree(a):
  t.left(90)
  for i in range(a):
    size = 20 + i*15
    t.left(120)
    t.forward(size)
    t.forward(-size)
    t.right(240)
    t.forward(size)
    t.forward(-size)
    t.left(120)
    t.forward(-35)
    t.pendown()
   
tree(6)
t.done()
