import turtle as tur

def dibujar_flor():
    tur.fillcolor("yellow")
    tur.begin_fill()

    for _ in range(2):
        tur.circle(10, 180)
        tur.circle(25, 110)
    
    tur.end_fill()

def main():
    tur.speed(1)
    tur.hideturtle()

    for _ in range(3):
        tur.penup()
        dibujar_flor()
        tur.pendown()
        tur.forward(50)  # Espacio entre las flores

    tur.done()

if __name__ == "__main__":
    main()
