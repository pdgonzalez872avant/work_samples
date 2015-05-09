import os
from Dreams_for_Kids import config as c


class DreamsForKids:
    """
    Class for Dreams for Kids volunteer work

    This class is the toolbox for my work with Dreams for Kids. I will try to add
    anything that is pertinent for any processes they have in store.

    Can unpack data from csv and also google sheets by using "gspread" library
    """

    def __init__(self):
        """
        May load some variables later
        :return:
        """
        self.file_storage_path = c.file_storage_path
        self.file_path = c.file_path
        self.gs_sheet_add = c.gs_sheet_add
        self.gs_key = c.gs_key
        self.sender = c.sender
        self.gmail_password = c.gmail_password
        self.recipient_list = c.recipient_list

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "{}\{}".format(self.file_path,
                                                                      "DreamsForKids-0661d09ef1fc.json")

    def unpacks_data_csv(self):
        """
        Takes data from a csv file and returns a list
        """
        import csv

        with open("{}\{}".format(self.file_path,
                                 "application_responses.csv"), "r") as f:
            reader = csv.reader(f, delimiter=",")

            all_data = [line for line in reader]

        return all_data

    def unpacks_data_google_sheets(self):
        """
        Deals with Google sheets instead of csv

        Resources:
        - http://gspread.readthedocs.org/en/latest/oauth2.html
        - https://github.com/burnash/gspread/issues/224
        - http://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
        - Set environment variables on windows: https://docs.python.org/3.4/using/windows.html
        - http://www.indjango.com/access-google-sheets-in-python-using-gspread/
        """

        import json
        import gspread
        from oauth2client.client import GoogleCredentials
        from oauth2client.client import OAuth2Credentials

        # The environment variable GOOGLE_APPLICATION_CREDENTIALS has to be set
        # This is done in the __init__ method
        credentials = GoogleCredentials.get_application_default()  # works

        scope = ['https://spreadsheets.google.com/feeds']

        credentials = credentials.create_scoped(scope)  # ok
        gs = gspread.authorize(credentials)  # ok

        # # By key
        # gs.open_by_key("1H6jSfg7haOUmfqRLM43K5usSqpGRWyBKHKHWHYxi-Cg")
        # # By Name
        # worksheet = gs.open('test').sheet1
        # By url
        sh = gs.open_by_url(self.gs_sheet_add)

        worksheet = sh.get_worksheet(0)

        list_of_lists = worksheet.get_all_values()

        # print(list_of_lists)

        return list_of_lists

    def create_pdf_application_associate_board_reportlab(self, person_details):
        """
        Takes in csv file and creates pdfs for each row

        Data lives here:
        - https://docs.google.com/spreadsheets/d/1Q0BUOIUx7akKG5vjYlZR3wKzogmh5
        u_S7cSWsB1RMh8/edit#gid=1739315830

        Resources:
        - http://www.reportlab.com/snippets/

        """

        # Imports
        import reportlab
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.enums import TA_JUSTIFY
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        import csv

        application_headers = ['Signed up',
                               'First Name',
                               'Last Name',
                               'Mailing Address',
                               'City',
                               'Zip',
                               'Phone Number',
                               'Email',
                               'Current Position/Employer',
                               'Are you currently a member/involved with other non-profit organizations?',
                               'If Yes, please list them below',
                               'What volunteer experience do you have?',
                               'What contributions would you make as an Associate Board Member for Dreams for Kids?',
                               'Why are you interested in serving as a member for the Dreams for Kids Associate Board?']

        # Combines data
        zipped = zip(application_headers, person_details)

        # Unpacks to save
        first_name, last_name = person_details[1], person_details[2]
        storage_path = "{}\{}{}.pdf".format(self.file_storage_path,
                                            first_name,
                                            last_name)

        # Creates report
        doc = SimpleDocTemplate(storage_path, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)

        # loads styles, pdf framework
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        # Creates centered Style
        centered = ParagraphStyle(name='centered',
                                  fontSize=30,
                                  leading=16,
                                  alignment=1,
                                  spaceAfter=1)
        # Starts the report
        story = []

        # Title
        ptext = '<font size=14><b>{}</b></font>' \
            .format("Associate Board Application")
        story.append(Paragraph(ptext, centered))
        story.append(Spacer(1, 20))

        # Creates question/answer format
        for line in zipped:
            header, data = line[0], line[1]

            # Question
            ptext = '<font size=12><b>{}</b></font>'.format(header)
            story.append(Paragraph(ptext, styles["Normal"]))
            story.append(Spacer(1, 6))

            # Answer
            ptext = '<font size=10>{}</font>'.format(line[1])
            story.append(Paragraph(ptext, styles["Normal"]))
            story.append(Spacer(1, 6))

        # Finishes building report
        doc.build(story)

    def create_pdf_application_associate_board_html(self, person_details):
        """
        Creates a better looking pdf

        Will look into this later, if possible

        Resources:
        - http://pbpython.com/pdf-reports.html
        - Virtualenv - http://flask.pocoo.org/docs/0.10/installation/
        """
        import pandas
        pass

    def unpacks_data_individual(self, person_details):
        """
        Lots of unpacking if needed
        :return:
        """

        # unpack person_details
        timestamp, first_name, last_name, mailing_add = person_details[0], \
                                                        person_details[1], \
                                                        person_details[2], \
                                                        person_details[3]
        # more unpacking
        city, zipcode, phone, email, current = person_details[4], \
                                               person_details[5], \
                                               person_details[6], \
                                               person_details[7], \
                                               person_details[8]
        # Last unpacking
        q1, q2, q3, q4, q5 = person_details[9], \
                             person_details[10], \
                             person_details[11], \
                             person_details[12], \
                             person_details[13]

    def email_response_update(self, recipient_list, responses):
        """
        Gives periodic updates on the people who have signed up for the associate
        board. Will be a scheduled task on Paulo's machine, will run every 30 min.

        Source:
        http://robertwdempsey.com/python3-email-with-attachments-using-gmail/
        """
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.mime.base import MIMEBase
        from email import encoders
        import datetime

        sender = self.sender
        gmail_password = self.gmail_password

        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        fmt = datetime.datetime.now().strftime("%b-%d-%Y  -  %H:%M")
        outer['Subject'] = "Associate Board Responses {}".format(fmt)
        outer['To'] = recipient_list
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        # attach the text
        text = "There are currently {} people who have signed up.".format(responses)
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

    def main(self):
        """
        Puts everything together
        """
        d = DreamsForKids()
        # data_list_csv = d.unpacks_data_csv()

        # # Creates the pdfs - ok
        # for itm in data_list_csv[1:]:  # Skips header
        #     d.create_pdf_application_associate_board_reportlab(itm)

        # Google Sheets data
        data_list_gs = d.unpacks_data_google_sheets()

        responses = len(data_list_gs) - 1
        print(len(data_list_gs))

        # d.email_response_update(recipient_list=self.recipient_list,
        #                         responses=responses)

        # Creates the pdfs via Google Sheets - ok
        for itm in data_list_gs[1:]:  # Skips header
            d.create_pdf_application_associate_board_reportlab(itm)

        # # Testing for concurrency
        # d.create_pdf_application_associate_board_html("hi")

if __name__ == "__main__":
    d = DreamsForKids()
    d.main()
    # print(help(DreamsForKids))