def occurrence_cle_liste(liste_cle):
    occurrence = {}
    for cle in liste_cle:
        if cle in occurrence:
            occurrence[cle] +=1
        else:
            occurrence[cle] =1
    return occurrence

liste_cle = ["Ananas", "Banane", "Orange", "Ananas", "Banane"]
print(occurrence_cle_liste(liste_cle))
