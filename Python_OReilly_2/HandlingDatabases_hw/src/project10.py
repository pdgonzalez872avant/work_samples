"""
Project 10
Creates program that checks if every animal eats at least one food
"""

import mysql.connector
from database_hw import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

#cursor.execute("""INSERT INTO animal (id, name, family, weight)
#                    VALUES (%s, %s, %s, %s)""", (99, 'Sillyface', 'Sheep', 50))

cursor.execute("""
        SELECT * 
        FROM animal LEFT JOIN food ON animal.id=food.anid
        WHERE feed is NULL       
               """)

#cursor.execute("""
#               SELECT *
#               FROM animal
#               """)

#cursor.execute("""
#        SELECT * 
#        FROM animal JOIN food ON animal.id=food.anid
#        WHERE feed is NULL """)

# 
#cursor.execute("""
#        SELECT * 
#        FROM animal JOIN food ON animal.id=food.anid
#        WHERE feed is NOT NULL """)

data = cursor.fetchall() # this was the problem! This needs to be here.

db.commit()

if data != []:
    #print('All animals eat at least one food')
    for d in data:
        print('{}, the {}, has to eat something'.format(d[1], d[2]))
else:
    print('no data')