import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='vit2357rew',
         autocommit=True
         )
def f(ident):
    sql = "SELECT name, iso_region from airport"
    sql += " WHERE ident='" + ident+"'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Name - {row[0]}\nLocation - {row[1]} ")
    return
ident = input("Enter icao: ")
f(ident)
