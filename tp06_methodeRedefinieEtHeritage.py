class Livre:
    def __init__(self, titre, auteur, achetable=False):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable

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

    def affiche_info(self):
        print(f"Titre: {self._titre}, Auteur: {self._auteur}, Achetable: {self._achetable}")

class LivrePapier(Livre):

    def __init__(self, titre, auteur, achetable, etat):
        super().__init__(titre, auteur, achetable)
        self._etat = etat

    def affiche_info(self):
        super().affiche_info()
        print(f"etat: {self._etat}")

class LivreNumerique(Livre):

    def __init__(self, titre, auteur, achetable, format):
        super().__init__(titre, auteur, achetable)
        self._format = format

    def affiche_info(self):
        super().affiche_info()
        print(f"format: {self._format}")


livres =[
    LivrePapier(titre="La mafia des généraux", auteur="Hichem ABOUD", achetable=False, etat="neuf"),
    LivrePapier(titre="La sale guerre", auteur="Habib SOUAIDIA", achetable=True, etat="moyen"),
    LivreNumerique(titre="Père riche père pauvre", auteur="Robert T.Kiyosaki", achetable=True, format="Kindle"),
    LivreNumerique(titre="Physique Chimie", auteur="Julien Calafell", achetable=False, format="PDF")
]
for livre in livres:
    livre.affiche_info()
    print()



