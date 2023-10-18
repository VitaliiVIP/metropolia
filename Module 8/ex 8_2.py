import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='vit2357rew',
         autocommit=True
         )
def f(iso_country):
    sql = "SELECT type from airport"
    sql += " WHERE iso_country='" + iso_country+"'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    s = 0
    h = 0
    c = 0
    m = 0
    l = 0
    if cursor.rowcount >0 :
        for row in result:
            print(f"Name - {row[0]}\n ")
            if row[0] == "closed":
                c += 1
            if row[0] == "small_airport":
                s += 1
            if row[0] == "medium_airport":
                m += 1
            if row[0] == "heliport":
                h += 1
            if row[0] == "large_airport":
                l += 1

    print("Closed -", c, "\nSmall airport -", s, "\nMedium airport -", m, "\nLarge airport -", l, "\nHeliport -", h,)
    return
iso_country = input()
f(iso_country)

