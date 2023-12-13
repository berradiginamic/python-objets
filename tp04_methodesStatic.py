class ChaineUtils:

    @staticmethod
    def est_anagramme(chaine1, chaine2):
        up_chaine1 = chaine1.upper()
        up_chaine2 = chaine2.upper()
        if not len(up_chaine1) == len(up_chaine2):
            return False
        return sorted(up_chaine1) == sorted(up_chaine2)

    @staticmethod
    def comptage_chaine(chaine, sous_chaine):
        return chaine.count(sous_chaine)


chaine1 = "listen"
chaine2 = "silent"
result_anagramme = ChaineUtils.est_anagramme(chaine1, chaine2)
print(f"est anagramme: {result_anagramme}")

chaine = "bobobobo"
sous_chaine = "bobo"
count_result = ChaineUtils.comptage_chaine(chaine, sous_chaine)
print(f"nombre d'accurences de '{sous_chaine}' dans '{chaine}' est {count_result}")

print(ChaineUtils.est_anagramme("chienne", "echine"))
print(ChaineUtils.comptage_chaine("le bateau est dans l'eau", "a"))
