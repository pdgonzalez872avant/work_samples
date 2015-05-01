"""
Sample program to list subjects by date
"""
from database import login_info
import mysql.connector
from email import message_from_string
conn = mysql.connector.Connect(**login_info)
curs = conn.cursor()
TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgSenderName VARCHAR(128),
     msgSenderAddress VARCHAR(128),
     msgText LONGTEXT
)"""

JOKES_TABLE_CREATE = """\
CREATE TABLE jotd_emails(
    jokeID INTEGER AUTO_INCREMENT PRIMARY KEY,
    joke_text LONGTEXT
)""" 

#SELECTSTM = """\
#SELECT * FROM message
#"""

SELECTSTM = """\
SELECT * FROM jotd_emails
"""

#jokes = []
#with open('jokes.txt', 'r') as f:
#    lines = f.readlines()
#    for i in lines:
#        jokes.append(str(i).replace('\n', ''))

#for i in jokes:
#    print(i)
#    curs.execute("""INSERT INTO jotd_emails (joke_text) VALUES (%s);""", (i, ))

#print(lines)

#curs.execute(TBLDEF)
curs.execute(SELECTSTM)

print(curs.fetchall())
conn.commit()


#for text, in curs.fetchall():
#    msg = message_from_string(text)
#    print(msg['date'], msg['subject'])
print('Complete')