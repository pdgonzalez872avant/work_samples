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

class JokeOfTheDay:
    """
    Class to control the a database of jokes,
    create, store and and email recipients based on date inputs
    """
    def __init__(self, cursor):
        """
        Instantiates the class and passes values to the class.
        """        
        
        self.start_date = datetime.date(settings.STARTTIME)#, "%Y/%m/%d") # strptime for str
        self.day_count = settings.DAYCOUNT
        self.final_date = datetime.date(settings.STARTTIME) + timedelta(days=self.day_count)
        
        self.date_list = []
        for id, date in enumerate(range(0,self.day_count)):
            # the str() here is essential. Annoying to compare dates, easy to compare strings
            self.date_list.append((id + 1, str(datetime.date(settings.STARTTIME) + 
                                   timedelta(days=date))))
#        print(self.date_list) # ok

        
        self.recipient_list = [] # creates list
        for recep in settings.RECIPIENTS:
            self.recipient_list.append(recep[1])
        

    def insert_jokes_in_db(self):
        """
        Creates database of jokes
        """
        
        DROP = """\
        DROP TABLE IF EXISTS jotd_emails
        """
        
        JOKES_TABLE_CREATE = """\
        CREATE TABLE jotd_emails(
            joke_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
            joke_date DATETIME,
            joke_text LONGTEXT
        )""" 

        curs.execute(DROP)
        conn.commit()
        curs.execute(JOKES_TABLE_CREATE)
        conn.commit()
        
        with open('jokes.txt', 'r') as f:
            lines = f.readlines()
            for i in lines:
                d = datetime.strftime(self.start_date, "%Y/%m/%d")
                curs.execute("""INSERT INTO jotd_emails (joke_date, joke_text) 
                             VALUES (%s, %s);""",(d, str(i).replace('\n', ''), ))
#                self.start_date += 1
#                jokes.append(str(i).replace('\n', ''))
        conn.commit()
        
        SELECTSTM = """\
                    SELECT * FROM jotd_emails
                    """
        
        trigger_test =  """\
                        SELECT * FROM jotd_emails WHERE joke_ID = 10;
                        """ # this doesn't work
   
    def retrieve_joke(self, day, table):
        """
        This retrieves jokes from the joke db by the chosen day
        """

#        curs.execute("""SELECT * FROM {}""".format(table))#, (day, ))
#        conn.commit() # this causes all my tests to fail, so I must comment this out
        curs.execute("""SELECT * FROM {} WHERE joke_ID={}""".format(table, day))#, (day, ))

#        print(curs.fetchall())  # diagnostic
        joke_txt = curs.fetchone()[2]  # this is the text
        
        
        
        return joke_txt

    def store_emails(self, msg, table):
        """
        Stores an email message, if necessary, returning its primary key.
        """ 
        
        message_id = msg['day_date_list']
        
        curs.execute("""INSERT INTO """ +  table + """
                        (msgMessageID, msgText)
                        VALUES (%s, %s)""",
                        (message_id, msg.as_string()))
        
        conn.commit()

    def create_email(self, messages, jotd_emails):
        """
        This creates the messages table and creates emails attaching 
        the MIMEText(joke, txt)
        """

        curs.execute("DROP TABLE IF EXISTS messages")#.format('messages')
#        conn.commit()
        
        TBLDEF = """\
                CREATE TABLE {}(
                     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
                     msgMessageID VARCHAR(128),
                     msgText LONGTEXT
                )""".format('messages')
        
        curs.execute(TBLDEF)
        conn.commit()
        
        SELECTSTM = """\
                    SELECT * FROM messages
                    """
        
        ## diagnostic printing
#        diagnostic_test_list = []
               
        for itm in self.date_list:
#            print(day) # 10

            day_date_list, date_date_list = itm  # unpacking

            for recip in self.recipient_list: # 3
#                print(recip)

                msg = MIMEMultipart()
                msg['From'] = 'paulo@me.com'  # constant
                msg['To'] = str(recip)  # adds email To
                msg['day_date_list'] = str(day_date_list)
                # self.retrieve_joke
                msg.attach(MIMEText(self.retrieve_joke(day_date_list, table=jotd_emails)))  # adds text
#                msg.attach(MIMEText(self.retrieve_joke(day_date_list, table='jotd_emails')))  # adds text
                #self.store_emails
                self.store_emails(msg, table=messages)
#                self.store_emails(msg, table='messages')
#                diagnostic_test_list.append(msg)
        
#        print(len(diagnostic_test_list))

    
    def send_email(self):
        """
        This used smtplib to send the email if today's date == date on the email. 
        This is the trigger. Uses self.date_list to query today's day ID/date and
        if True, emails emails people by accessing the db and emailing what is returned. 
        """
        
        todays_date = datetime.now().strftime("%Y-%m-%d")
        trigger = 0
        for itm in self.date_list:
            day_date_list, date_date_list = itm
#            print(date_date_list, todays_date, day_date_list)
            if str(date_date_list) == str(todays_date):
#                print('woooo', day_date_list)
                curs.execute("SELECT * FROM messages WHERE msgMessageID=%s", (day_date_list, ))
                # the above only returns one record. I want it to return 3.
                for i in curs.fetchall():
                    print(i)
            else:
                pass
#                print("didn't find anything")
            
            
#            if date_date_list == todays_date:
#                print(date_date_list, todays_date)
#            else:
#                print('nope')
#                print(date_date_list, todays_date)
        
        
        # smtp send email.
        
        # loop to send to every person in the email list if the trigger is true.
        
        
    
    def __str__(self):
        """
        __str__ method
        """
        return "This is the JokeOfTheDay Class!"
        
#db = mysql.connector.Connect(**login_info)
#curs = db.cursor()
#j = JokeOfTheDay(curs)
#j.insert_jokes_in_db()  # ok
#print(j.retrieve_joke(1)) 
#j.create_email() # This also includes store_email method.
#j.send_email()

#print('This runs') # great!