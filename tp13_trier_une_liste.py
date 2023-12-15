class AdressePostale:
    def __init__(self, numero_rue:int, libelle_rue:str, code_postal:str, ville:str):
        self._numero_rue = numero_rue
        self._libelle_rue = libelle_rue
        self._code_postal = code_postal
        self._ville = ville

    def __repr__(self):
        return f"{self._numero_rue} - {self._libelle_rue} - {self._code_postal} - {self._ville}"


class Personne:
    def __init__(self, nom, prenom, age,  adresse):
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._adresse = adresse

    def __repr__(self):
        return f"{self._nom} - {self._prenom} - {self._age} - {self._adresse}"

    def __lt__(self, other):
        return self._prenom < other._prenom

adresse1 = AdressePostale(numero_rue=3, libelle_rue="Place Watteau", code_postal="30900", ville="Nîmes")

p1 = Personne(nom="berrabah", prenom="fatima", age=41, adresse=adresse1)
p2 = Personne(nom="benmira", prenom="ishak", age=3, adresse=adresse1)

print(p1 < p2)

