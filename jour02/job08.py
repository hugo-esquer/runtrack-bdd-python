import mysql.connector

def ajouter_animal(nom, race, cage_id, naissance, pays):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""INSERT INTO animal (nom, race, cage_id, naissance, pays)
                    VALUES (%s, %s, %s, %s, %s)""", (nom, race, cage_id, naissance, pays))
    
    connexion.commit()
    connexion.close()

def supprimer_aniaml(nom):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""DELETE FROM animal WHERE nom = %s""", (nom,))

    connexion.commit()
    connexion.close()

def modifier_aniaml(id, nom, race, cage_id, naissance, pays):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""UPDATE animal
                    SET nom = %s, race = %s, cage_id = %s, naissance = %s, pays = %s
                    WHERE id = %s""", (nom, race, cage_id, naissance, pays, id))
    connexion.commit()
    connexion.close()

def ajouter_cage(superficie, capacite):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""INSERT INTO cage (superficie, capacite)
                    VALUES (%s, %s)""", (superficie, capacite))
    
    connexion.commit()
    connexion.close()

def suppression_cage(id):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""DELETE FROM cage WHERE id = %s""", (id,))

    connexion.commit()
    connexion.close()

def modifier_cage(id, superficie, capacite):
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""UPDATE animal
                    SET superficie = %s, capacite = %s
                    WHERE id = %s""", (superficie, capacite, id))
    connexion.commit()
    connexion.close()

def afficher_animaux():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM animal")
    animaux = curseur.fetchall()

    for animal in animaux:
        print(animal)

    connexion.close()

def afficher_animaux_cage():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("""SELECT cage.id, cage.superficie, cage.capacite, animal.*
                    FROM cage
                    LEFT JOIN animal ON cage.id = animal.cage_id""")
    animaux = curseur.fetchall()
    for animal in animaux:
        print(animal)

    connexion.close()

def superficie_totale():
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="zoo"
    )
    curseur = connexion.cursor()

    curseur.execute("SELECT SUM(superficie) FROM cage")
    superficie = curseur.fetchone()
    superficie = superficie[0]

    connexion.close()

    return superficie

while True:
    print("\nMenu:")
    print("1. Ajouter un animal")
    print("2. Ajouter une cage")
    print("3. Afficher la liste des animaux dans le zoo")
    print("4. Afficher la liste des animaux dans les cages")
    print("5. Calculer la superficie totale de toutes les cages")
    print("6. Modifier un animal")
    print("7. Supprimer un animal")
    print("8. Modifier une cage")
    print("9. Supprimer une cage")
    print("0. Quitter")

    choix = input("Entrez votre choix: ")

    if choix == "1":
        nom = input("Nom de l'animal: ")
        race = input("Race de l'animal: ")
        cage_id = int(input("ID de la cage: "))
        naissance = input("Date de naissance de l'animal: ")
        pays = input("Pays d'origine de l'animal: ")

        ajouter_animal(nom, race, cage_id, naissance, pays)

    elif choix == "2":
        superficie = int(input("Superficie de la cage: "))
        capacite = int(input("Capacite de la cage: "))

        ajouter_cage(superficie, capacite)

    elif choix == "3":
        afficher_animaux()

    elif choix == "4":
        afficher_animaux_cage()

    elif choix == "5":
        superficie = superficie_totale()
        print(f"La superficie totale des cages est de {superficie} m2")

    elif choix == "6":
        id = int(input("ID de l'animal a modifier: "))
        nom = input("Nouveau nom de l'animal: ")
        race = input("Nouvelle race de l'animal: ")
        cage_id = int(input("Nouvelle ID de la cage: "))
        naissance = input("Nouvelle date de naissance de l'animal: ")
        pays = input("Nouveau pays d'origine de l'animal: ")

        modifier_aniaml(id, nom, race, cage_id, naissance, pays)

    elif choix == "7":
        nom = input("Nom de l'animal a supprimer: ")

        supprimer_aniaml(nom)

    elif choix == 8:
        id = int(input("ID de la cage a modifier: "))
        superficie = int(input("Superficie de la cage: "))
        capacite = int(input("Capacite de la cage: "))

        modifier_cage(id, superficie, capacite)

    elif choix == "9":
        id = int(input("ID de la cage a supprimer: "))

        suppression_cage(id)

    elif choix == "0":
        break

    else:
        print("Choix invalide, entrer un choix valide.")