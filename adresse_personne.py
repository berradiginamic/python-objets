class AdressePostale:
    def __init__(self, numero_rue:int, libelle_rue:str, code_postal:str, ville:str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville


class Personne:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

#créer 2 instances d'adresse postale en renseignant les valeurs de tous les attributs

adresse1 = AdressePostale(numero_rue=3, libelle_rue="Place Watteau", code_postal="30900", ville="Nîmes")
adresse2 = AdressePostale(numero_rue=5, libelle_rue="Impasse Vivaldi", code_postal="30900", ville="Nîmes")


#créer 2 instances de personne en renseignant la valeur de tous les attributs

personne1 = Personne(nom="Berrabah", prenom="Fatima", adresse=adresse1)
personne2 = Personne(nom="Calvet", prenom="Souad", adresse=adresse2)

#afficher les instances avec la fonction print

print("Personne 1", personne1.nom, personne1.prenom, "Adresse", personne1.adresse.numero_rue, personne1.adresse.libelle_rue, personne1.adresse.code_postal, personne1.adresse.ville)
print("Personne 2", personne2.nom, personne2.prenom, "Adresse", personne2.adresse.numero_rue, personne2.adresse.libelle_rue, personne2.adresse.code_postal, personne2.adresse.ville)
