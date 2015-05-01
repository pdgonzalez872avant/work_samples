"""
Demonstration of indexed access to data elements
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

fmt = "{0:10} {1:10} {2:6}"
print(fmt.format("Animal", "Weight", "Family"))
print("-" * 28)
cursor.execute("SELECT name, weight, family FROM animal")
#cursor.execute("SELECT * FROM animal")

for name, weight, family in cursor.fetchall():
    print(fmt.format(name,weight, family))

#for animal in cursor.fetchall():
#    print(fmt.format(animal[1], animal[3], animal[2]))
