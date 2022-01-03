class Rectangle:

    def __init__(self, longueur=10, largeur=10):
        self.nom = "rectangle"
        self.largeur = largeur
        self.longueur = longueur

    def surface(self):
        return self.longueur * self.largeur

    def affichage(self):
        print(self.nom)
        print(self.longueur)
        print(self.largeur)

class carre(Rectangle):

    def __init__(self, longueur=20, largeur=20):
        super().__init__(longueur, largeur)
        self.nom = "carré"



r1 = Rectangle()
r1.affichage()
c1 = carre()
c1.affichage()
