import turtle

def draw_flower(some_flower):
    for i in range(1,3):
        some_flower.forward(100)
        some_flower.right(45)
        some_flower.forward(100)
        some_flower.right(135)


def draw_art():
    window = turtle.Screen()   
    window.bgcolor("black") 
    
    fleur = turtle.Turtle()
    fleur.shape("turtle")
    fleur.color("pink")
    fleur.speed(8)

    for i in range(1,37):
        draw_flower(fleur)
        fleur.right(10)

    fleur.right(90)    
    fleur.forward(350)
    
draw_art()
