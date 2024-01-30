import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database

        )
        self.cursor = self.connection.cursor()

    def ajout_employe(self, nom, prenom, salaire, id_service):
        requete = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    def lire_employe(self, id):
        requete = "SELECT * FROM employe WHERE id = %s"
        self.cursor.execute(requete, (id,))
        employe = self.cursor.fetchone()
        return employe
    
    def maj_employe(self, id, nom, prenom, salaire, id_service):
        requete = """
        UPDATE employe
        SET nom = %s, prenom = %s, salaire = %s, id_service = %s
        WHERE id = %s"""
        valeurs = (nom, prenom, salaire, id_service, id)
        self.cursor.execute(requete, valeurs)
        self.connection.commit()

    def suppression_employe(self, id):
        requete = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(requete, (id,))
        self.connection.commit()

    def fermer(self):
        self.cursor.close()
        self.connection.close()

# Instance de la classe Employe
entreprise = Employe("localhost", "root", "root", "Entreprise")

# Ajout d'un nouvel employé
entreprise.ajout_employe("Doe", "Jhon", 6500, 1)

# Lecture des information d'un employé
print(entreprise.lire_employe(6))

# Modification des informations d'un employé
entreprise.maj_employe(6, "Doe", "Jhon", 3200, 1)

# Verification que la modification a été réalisé
print(entreprise.lire_employe(6))

# suppression d'un employe
entreprise.suppression_employe(6)

entreprise.fermer()


# Début du job07
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Entreprise",
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM employe WHERE salaire > 3000")

results = cursor.fetchall()
print(results)

cursor.execute("""SELECT employe.id, employe.nom, employe.prenom, service.nom FROM employe
               JOIN service
               ON employe.id_service = service.id""")

results = cursor.fetchall()
print (results)

cursor.close()
mydb.close()