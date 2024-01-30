import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "LaPlateforme",
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")

results = cursor.fetchone()
print(f"La capacité de toutes les salles est de: {results[0]}")

cursor.close()
mydb.close()
