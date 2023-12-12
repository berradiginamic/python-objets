class Zoo:

    liste_animaux = []
    nombre_total_animaux = 0

    @classmethod

    def ajouter_animaux(cls, espece, nombre):
        for animal in cls.liste_animaux:
            if animal["espece"] == espece:
                animal["nombre"] += nombre
                cls.nombre_total_animaux += nombre
                break
        else:
            cls.liste_animaux.append({"espece": espece, "nombre": nombre})
            cls.nombre_total_animaux += nombre

    @classmethod

    def afficher_animaux(cls):
        print("animaux dans le Zoo:")
        for animal in cls.liste_animaux:
            print(f"{animal['espece']} : {animal['nombre']}")
        print(f"nombre total d'animaux dans le Zoo: {cls.nombre_total_animaux} ")

Zoo.ajouter_animaux("Lion", 5)
Zoo.ajouter_animaux("Elephant", 2)
Zoo.ajouter_animaux("Girafe", 3)
Zoo.ajouter_animaux("Elephant", 1)

Zoo.afficher_animaux()
