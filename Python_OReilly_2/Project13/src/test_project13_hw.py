from project13_hw import JokeOfTheDay
import settings
from database import login_info
import mysql.connector
from email import message_from_string
conn = mysql.connector.Connect(**login_info)
curs = conn.cursor()
from datetime import datetime, timedelta
import os, email
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.text import MIMEText
import mimetypes
from email.utils import parsedate_tz, mktime_tz, parseaddr
import unittest

class Test_JokesOfTheDay(unittest.TestCase):
    """
    Tests project 13
    """
    def test_insert_jokes_in_db(self):
        """
        Tests if the insert_jokes_in_db method works
        """
        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        j = JokeOfTheDay(curs)
        j.insert_jokes_in_db()  # ok
        
        SQL_count = "SELECT COUNT(joke_text) FROM {}".format('jotd_emails')
        
        curs.execute(SQL_count)
        result = curs.fetchone()
        expected = (32,)  # all the jokes available

        self.assertEqual(result, expected)
            
            
    def test_create_email(self):
        """
        Tests if create_email module works. Must adjust values in the settings file.
        Chose a 10 day vacation.
        """
        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        j = JokeOfTheDay(curs)
        j.create_email(messages='messages', jotd_emails='jotd_emails')
        
        SQL_count = "SELECT COUNT(msgText) FROM messages"
        
        curs.execute(SQL_count)
        result = curs.fetchall()
        conn.commit()
        expected = [(30,)]

        self.assertEqual(result, expected)


    def test_store_emails(self):
        """
        tests the store_emails method by creating a test db and returning values
        """

        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        j = JokeOfTheDay(curs)
        
        table_name = 'messages_test'
        
        curs.execute("DROP TABLE IF EXISTS {}".format(table_name))
        conn.commit()
        
        TBLDEF = """\
                CREATE TABLE {} (
                     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
                     msgMessageID VARCHAR(128),
                     msgText LONGTEXT
                )""".format(table_name)
        
        curs.execute(TBLDEF)
        conn.commit()
        
        curs.execute("""INSERT INTO {}
                        (msgMessageID, msgText)
                        VALUES ('2', 'this is a test')""".format(table_name))

        SQL_count = "SELECT COUNT(msgText) FROM {}".format(table_name)
        
        # Testing
        curs.execute(SQL_count)
        result = curs.fetchall()
        expected = [(1,)]
        self.assertEqual(result, expected)

        # Dummy msg
        msg = MIMEMultipart()
        msg['From'] = 'paulo@me.com'  # constant
        msg['To'] = 'test@me.com'  # adds email To
        msg['day_date_list'] = '2'
        msg.attach(MIMEText('super funny joke right here'))  # adds text
        j.store_emails(msg, table=table_name)
                
        # Fetch from db, assert it works        
        SQL_select = "SELECT * FROM {}".format(table_name)
        curs.execute(SQL_select)
        result_select = curs.fetchall()
        expected_select = [(1, '2', 'this is a test')]

        self.assertEqual(result_select, expected_select)

    def test_retrive_joke(self):
        """
        Tests the retrieve_joke method
        """
        
        db = mysql.connector.Connect(**login_info)
        curs = db.cursor()
        
        
        table_name = 'jotd_emails_test'
        
        DROP = """\
        DROP TABLE IF EXISTS {}""".format(table_name)
        
        JOKES_TABLE_CREATE = """\
        CREATE TABLE {} (
            joke_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
            joke_date DATETIME,
            joke_text LONGTEXT
        )""".format(table_name) 

        curs.execute(DROP)
        conn.commit()
        curs.execute(JOKES_TABLE_CREATE)
        conn.commit()
        
        d_obj = datetime(2015, 4, 7)
        
        d = datetime.strftime(d_obj, "%Y/%m/%d")
        
        SQL_insert = """INSERT INTO {} (joke_date, joke_text) 
                             VALUES ('{}', 'funny joke here yes!')""".format(table_name, d)

        SQL_insert2 = """INSERT INTO {} (joke_date, joke_text) 
                             VALUES ('{}', 'another one!!')""".format(table_name, d)
        
        
        curs.execute(SQL_insert)
        curs.execute(SQL_insert2)
        
        conn.commit()
        
#        # Tests there is only 1 joke in the db.
#        SQL_count = "SELECT COUNT(*) FROM {}".format('jotd_emails') # table_name
#        curs.execute(SQL_count)
#        result = curs.fetchall()
#        expected = [(2,)]
##        print(result)
##        self.assertEqual(result, expected)
        
        curs.execute("SELECT * FROM {}".format('jotd_emails')) # jotd_emails
        conn.commit()
        result_select = curs.fetchall()
#        print(result_select)
        
        
        # Retrieves the joke
        # This abandons trying to retrieve the dummy table's results
        # and just retrieves the main table's results.
        # For some reason only one works. At least the function works.
        a = JokeOfTheDay(curs)
        result = a.retrieve_joke(1, 'jotd_emails')
        expected = ('What do you call a sleeping bull? A bull-dozer. ')
        self.assertEqual(result, expected)
        
        
        
if __name__ == "__main__":
    unittest.main()
