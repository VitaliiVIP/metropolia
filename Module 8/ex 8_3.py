import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='vit2357rew',
         autocommit=True
         )
ident = input("Enter icao: ")
sql = "SELECT latitude_deg, longitude_deg from airport"
sql += " WHERE ident='" + ident+"'"
print(sql)
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount >0 :
    for row in result:
        print(f"Latitude - {row[0]}\nLongitude - {row[1]} ")
        port1=(row[0], row[1])
ident2 = input("Enter icao: ")
sql = "SELECT latitude_deg, longitude_deg from airport"
sql += " WHERE ident='" + ident2+"'"
print(sql)
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount >0 :
    for row in result:
        print(f"Latitude - {row[0]}\nLongitude - {row[1]} ")
        port2 = (row[0], row[1])
print(geodesic(port1, port2).km)


