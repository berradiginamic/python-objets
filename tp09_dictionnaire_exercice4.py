class Salarie:
    def __init__(self, nom, matricule, service):
        self.nom = nom
        self.matricule = matricule
        self.service = service

liste_salarie = [
    Salarie("Antoine Dupont", 127, "DSI/JAVA"),
    Salarie("Berthe Casa", 238, "DSI/PHP"),
    Salarie("Fatima Ouassa", 478, "DSI/JAVA"),
    Salarie("Cassian Andor", 156, "DSI/PYTHON"),
    Salarie("Lee Wu", 559, "DSI/PHP"),
    Salarie("Hassan Missen", 96, "DSI/PYTHON"),
    Salarie("Aurélien PIC", 889, "DSI/JAVA")
]
nbr_par_service = {}
for salarie in liste_salarie:
    if salarie.service in nbr_par_service:
        nbr_par_service[salarie.service] +=1
    else:
        nbr_par_service[salarie.service] = 1

print(nbr_par_service)
