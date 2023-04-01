#QUESTION1
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)

print(my_point)



#QUESTION2
class rectangle :
    def __init__(self, longueur, largeur):
        self.longueur= longueur
        self.largeur= largeur
    def surface(self):
        return self.longueur*self.largeur
    def perimetre(self):
        return (self.longueur+self.largeur)*2
rectangle1= rectangle(3,4)

print("surface= "+ str(rectangle1.surface()))
print("perimetre= " + str(rectangle1.perimetre()))


#QUESTION3
class cercle:
    def __init__(self,rayon,o):
        self.centre= o

        self.rayon= rayon

    def perimetre(self):
        return 2*3.14*self.rayon

    def surface(self):
        return self.rayon**2*3.14
    #problem pour continuer


#QUESTION4
class bank:
    def __init__(self):
        self.solde = 0


    def depot(self):
        montant = float(input("entre le montant à mettre en bank: "))
        self.solde += montant
        print("\n le montant de depot est :", montant)

    def retrait(self):
        montant = float(input("entrer le montant à retirer : "))
        if self.solde >= montant:
            self.solde -= montant
            print("\n vous avez retirer :", montant)
        else:
            print("\n solde insuffisant  ")

    def afficher (self):
        print("\n argent disponible =", self.solde)

mon_compte= bank()

