class ChaineUtils:

    @staticmethod
    def est_anagramme(chaine1, chaine2):
        chaine1_sorted = sorted(chaine1)
        chaine2_sorted = sorted(chaine2)
        return chaine1_sorted == chaine2_sorted

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
