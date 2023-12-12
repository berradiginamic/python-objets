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

    def afficher_nom_majuscule(self):
        print(f"{self.nom.upper()} {self.prenom}")

    def nom_modifie(self, nouveau_nom):
        self.nom = nouveau_nom

    def prenom_modifie(self, nouveau_prenom):
        self.prenom = nouveau_prenom

    def adresse_modifiee(self, nouvelle_adresse):
        self.adresse = nouvelle_adresse

    def return_nom(self):
        return self.nom

    def return_prenom(self):
        return self.prenom

    def return_adresse(self):
        return self.adresse

    def afficher_divers_attributs(self):
        print(f"Nom: {self.nom}")
        print(f"Prenom : {self.prenom}")
        print(f"Adresse:")
        print(f"{self.adresse.numero_rue} {self.adresse.libelle_rue} {self.adresse.code_postal} {self.adresse.ville}")



#créer 2 instances d'adresse postale en renseignant les valeurs de tous les attributs

adresse1 = AdressePostale(numero_rue=3, libelle_rue="Place Watteau", code_postal="30900", ville="Nîmes")



#créer 2 instances de personne en renseignant la valeur de tous les attributs

personne1 = Personne(nom="berrabah", prenom="fatima", adresse=adresse1)


#afficher les instances avec la fonction print

print("Personne 1", personne1.nom, personne1.prenom, "Adresse", personne1.adresse.numero_rue, personne1.adresse.libelle_rue, personne1.adresse.code_postal, personne1.adresse.ville)

personne1.afficher_nom_majuscule()
personne1.nom_modifie("Benmira")
personne1.prenom_modifie("Maria")

nouvelle_adresse = AdressePostale(numero_rue=5, libelle_rue="Impasse Vivaldi", code_postal="30900", ville="Nîmes")
personne1.adresse_modifiee(nouvelle_adresse)

print(personne1.afficher_divers_attributs())

