import turtle


# def moveTurtle(px, nb):
#     for i in range(nb):
#         t.forward(px)
#         t.left(90)
#         t.forward(px)
#         t.right(90)
#         px -= 10
#     t.forward(px)

# moveTurtle(60, 5)


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    # taille = (i+1)*taille_depart
    for i in range(0, nb):
        taille = (i+1)*(i+1)*taille_depart
        carre(taille)


t = turtle.Turtle()

carres(10, 10)

turtle.done()
