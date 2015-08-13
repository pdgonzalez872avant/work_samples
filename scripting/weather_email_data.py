import os
import sys
import subprocess
import csv
import json
import urllib
from urllib.request import urlopen
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from config_email import attachments, gmail_password, sender
import config_email


class EmailForecast:
    """
    Fetches, charts using R and emails forecasted data
    """

    def __init__(self, city, day_count):
        """
        Uses variables from the config_email file.
        """
        self.city = city
        self.day_count = day_count
        self.weather_data_url = "http://api.openweathermap.org/data/2.5/" \
                                "forecast/daily?q=" + self.city + "&mode=" \
                                "json&units=imperial&cnt=" + self.day_count
        self.img = config_email.img
        self.attachments = config_email.attachments
        self.sender = config_email.sender
        self.gmail_password = config_email.gmail_password
        self.csv_file = config_email.csv_file
        self.RScript_path_Windows = config_email.RScript_path_Windows
        self.R_filepath_Windows = config_email.R_filepath_Windows
        self.RScript_path_Linux = config_email.RScript_path_Linux
        self.R_filepath_Linux = config_email.R_filepath_Linux

    def get_data(self):
        """
        get weather data from openweathermap
        """
        response = urlopen(self.weather_data_url)
        str_response = response.readall().decode('utf-8')
        obj = json.loads(str_response)

        # Could do list comps, for now this for readability.
        # Creates lists to zip later.
        list_date = []
        list_temp = []
        date_temp_list = []

        for itm in obj['list']:

            # This has a Unix format (1427475600)
            itm_date = datetime.datetime.fromtimestamp(itm['dt'])
            # This is formatted accordingly
            itm_date_formatted = itm_date.strftime("%m/%d/%y")  # interesting
            # itm_date_formatted = itm_date.strftime("%b-%d-%y")  # interesting

            itm_temp = itm['temp']['day']

            # list_date.append(itm_date)
            list_date.append(itm_date_formatted)
            list_temp.append(itm_temp)

        # Gives me leverage to iterate if necessary when charting this
        for d in zip(list_date, list_temp):
            date_temp_list.append(d)

        # Starts the csv process
        with open(self.csv_file, 'wt') as outcsv:

            #configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter='\t', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['Date', 'Values'])  # Headers

            # Uses the zipped list
            for item in date_temp_list:
                writer.writerow([item[0], item[1]])  #Write item to outcsv

        return list_date, list_temp

    def chart_R_Windows(self):
        """
        Uses an R script to plot the results above. Lightweight solution
        to import/file size problem. Super fast.
        """
        RScript_path_Windows = self.RScript_path_Windows
        R_filepath_Windows = self.R_filepath_Windows
        retcode = subprocess.call([RScript_path_Windows, R_filepath_Windows])

    def chart_R_Linux(self):
        """
        This is to run on the raspberry pi
        """

        RScript_path_Linux = self.RScript_path_Linux
        R_filepath_Linux = self.R_filepath_Linux
        retcode = subprocess.call(['/usr/lib/R/bin/Rscript',
                                   'R_weather_data_manipulation.R'])

    def chart_tuples_from_list(self, dates, values):
        """
        This uses matplotlib to chart the data. This is no longer used, we
        use R instead.
        """
        x = mdates.date2num(dates)
        y = values

        fig, ax = plt.subplots()
        # ax.plot(x, y)
        ax.plot(x, y, 'k--', label='Temperature')

        # legend = ax.legend(loc='upper right', shadow=True)  # didn't like this

        plt.xlabel('Date', fontsize=16)
        plt.ylabel('Temperature', fontsize=16)

        plt.scatter(x,y)
        plt.title('{} day Forecast for {}'.format(self.day_count, self.city), fontsize=22)
        # plt.xticks(1,2)

        # # attempt at datalabels
        # for y in y:                                                # <--
        #     ax.text(y, 1, 1)


        my_fmt = mdates.DateFormatter('%b-%d')
        ax.xaxis.set_major_formatter(my_fmt)

        fig.autofmt_xdate()

        fn = fig.savefig(self.img)

        return plt
        # return plt.show()

    def daily_email(self, recipient_list):
        """
        Source:
        http://robertwdempsey.com/python3-email-with-attachments-using-gmail/
        """
        sender = self.sender
        gmail_password = self.gmail_password

        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        fmt = datetime.datetime.now().strftime("%b-%d-%Y")
        outer['Subject'] = "Weather Forecast for {} - {}".format(self.city, fmt)
        outer['To'] = recipient_list
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        # Add the attachments to the message
        for file in self.attachments:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Might be set for Rpi path or vice versa. Error: ", sys.exc_info()[0])
                raise

        # attach the text
        text = "The chart is attached to this email. Data comes from " \
               + "openweathermap.com. Sent automatically via Raspberry Pi."
        part1 = MIMEText(text, 'plain')
        outer.attach(part1)

        composed = outer.as_string()

        # Send the email
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipient_list, composed)
            s.close()
            # print("Email sent!")
        except:
            # print("Unable to send the email. Error: ", sys.exc_info()[0])
            raise

if __name__ == '__main__':
    e = EmailForecast('Chicago', '10')
    date, values = e.get_data()
    # e.chart_R_Linux()  # run on the raspberri pi
    e.chart_R_Windows()  # run on windows when needed

    for person in config_email.recipient_list:
        e.daily_email(person)


