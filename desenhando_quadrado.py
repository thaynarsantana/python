import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)   #anda em frente 100 px
        some_turtle.right(90)      #gira pra direita 90º

def draw_art():
    
    window = turtle.Screen()    #cria uma tela onde tudo será desenhado
    window.bgcolor("white")     #define a cor backgroud da tela 

    #Create the turtle Brad
    brad = turtle.Turtle()  #brad é o nome da tartaruguinha
    brad.shape("turtle")    #forma do cursor
    brad.color("purple")    #cor da linha
    brad.speed(3)           #velocidade do desenho

    for i in range(1,37):
        draw_square(brad)       #chama a função de desenhar quadrado
        brad.right(10)          #gira o brad 10º pra ele poder desenhar o circulo de quadrados45
    #Create the turtle Angie   
    #angie = turtle.Turtle() #angie é a moça q faz o circulo
    #angie.shape("arrow")
    #angie.color("red")
    #angie.circle(100)

    #danny = turtle.Turtle()
    #danny.shape("arrow")
    #danny.color("blue")

    #for i in range(1,4):
     #   danny.forward(100)
      #  danny.left(120)
    

   
    window.exitonclick()    #sai automaticamente quando clicado

draw_art()
