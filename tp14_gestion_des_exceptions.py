class PersonneException(Exception):
    pass

class Personne:
    def __init__(self, nom, prenom, age,  adresse):
        self._nom = nom
        self._prenom = prenom
        self._age = age
        self._adresse = adresse


class PersonneService:
    @staticmethod
    def valider(personne):
        try:
            if not personne._nom or len(personne._nom.strip())<2:
                raise PersonneException("le nom doit contenir au moins 2 caractères.")
            if not personne._prenom or len(personne._prenom.strip())< 2:
                raise PersonneException("le prenom doit contenir au moins 2 caractères.")
            if not personne._adresse:
                raise PersonneException("vous devez renseigner l'adresse.")
        except PersonneException as e:
            print(f"erreur de validation pour {personne._nom} {personne._prenom}: {str(e)}")
        else:
            print(f"{personne._nom} {personne._prenom} a bien été validé")

p1 = Personne("berrabah", "fatima", 41, "3 place watteau 30900 Nîmes")
p2 = Personne("benmira", "I", 3, "3 place watteau 30900 Nîmes")
p3 = Personne("benmire", "maria", 1, "")

service = PersonneService()
service.valider(p1)
service.valider(p2)
service.valider(p3)
