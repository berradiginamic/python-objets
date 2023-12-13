class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._achetable = False

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, nouv_titre):
        self._titre = nouv_titre

    @property
    def auteur(self):
        return self._auteur
    @auteur.setter
    def auteur(self, nouv_auteur):
        self._auteur = nouv_auteur

    @property
    def achetable(self):
        return self._achetable
    @achetable.setter
    def achetable(self, valeur):
        self._achetable = valeur

livre1 = Livre(titre="La mafia des généraux", auteur="Hichem ABOUD")

livre1.titre = "La sale guerre"
livre1.auteur = "Habib SOUAIDIA"
livre1.achetable = True

print(f"Titre: {livre1.titre}, Auteur: {livre1.auteur}, Achetable: {livre1.achetable}")

