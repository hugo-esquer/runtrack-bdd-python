import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "LaPlateforme",
)

cursor = mydb.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

results = cursor.fetchone()
print(f"La superficie de La Plateforme est de {results[0]} m2")

cursor.close()
mydb.close()
