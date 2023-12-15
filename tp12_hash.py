class AdressePostale:
    def __init__(self, numero_rue:int, libelle_rue:str, code_postal:str, ville:str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville

    def __eq__(self, other):
        if not isinstance(other, AdressePostale):
            return False
        return self.numero_rue == other.numero_rue and self.libelle_rue == other.libelle_rue and self.code_postal == other.code_postal and self.ville == other.ville


    def __hash__(self):
        return hash((self.numero_rue, self.libelle_rue, self.code_postal, self.ville))


class Personne:
    def __init__(self, nom, prenom, adresse):
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self._nom==other._nom and self._prenom==other._prenom and self._adresse==other._adresse

    def __hash__(self):
        return hash((self._nom, self._prenom, self._adresse))

    def __str__(self):
        return f"{self._nom} {self._prenom}, {str(self._adresse)}"


adresse1 = AdressePostale(numero_rue=3, libelle_rue="Place Watteau", code_postal="30900", ville="Nîmes")

p1 = Personne(nom="berrabah", prenom="fatima", adresse=adresse1)
p2 = Personne(nom="berrabah", prenom="fatima", adresse=adresse1)

set_personne = {p1, p2}
for p in set_personne:
    print(p)
