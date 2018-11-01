import turtle

def draw_inicials():
    thay = turtle.Turtle()
    thay.shape("turtle")
    thay.color("red")
    thay.speed(1)

    thay.pu()
    thay.setpos(-200,0)
    thay.pd()
    thay.forward(100)
    thay.backward(50)
    thay.right(90)
    thay.forward(100)
    thay.right(90)

    thay.pu()
    thay.setpos(100,0)
    thay.pd()
    thay.forward(100)
    thay.left(90)
    thay.forward(50)
    thay.left(90)
    thay.forward(100)
    thay.right(90)
    thay.forward(50)
    thay.right(90)
    thay.forward(100)


    

draw_inicials()
