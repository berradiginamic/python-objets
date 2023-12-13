class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return f"{self.nom} {self.prenom}, {self.age} ans"

    def __repr__(self):
        return f"Personne(nom={self.nom}, prenom={self.prenom}, age={self.age})"

personne1 = Personne(nom="Benmira", prenom="Ishak", age=3)

print("affichage utilisant __str__ :", personne1)

liste_personne = [
    Personne(nom="Benmira", prenom="Maria", age=1),
    Personne(nom="Berrabah", prenom="Fatima", age=41)
]
print("affichage utilisant __repr__ :", liste_personne)
