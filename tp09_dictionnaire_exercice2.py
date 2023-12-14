def nombre_caracteres_cle(liste_cle):
    return {cle: len(cle) for cle in liste_cle}

liste_cle = ["coucou", "Hi", "bonjour"]
print(nombre_caracteres_cle(liste_cle))
