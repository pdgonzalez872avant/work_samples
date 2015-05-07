class DreamsForKids:
    """
    Class for Dreams for Kids volunteer work
    """

    def __init__(self):
        """
        May load some variables later
        :return:
        """
        self.file_storage_path = r"C:\Users\Paulo\PycharmProjects\work_samples\Dreams_for_Kids\applications_associate_board"
        self.file_path = r"C:\Users\Paulo\PycharmProjects\work_samples\Dreams_for_Kids"

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

    def create_pdf_application_associate_board(self, person_details):
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

    def main(self):
        """
        Puts everything together
        :return:
        """
        d = DreamsForKids()
        data_list = d.unpacks_data_csv()

        for itm in data_list[1:]:  # Skips header
            d.create_pdf_application_associate_board(itm)

        # for itm in data_list:
        # pass
        #     # d.create_pdf_application_associate_board("test")


if __name__ == "__main__":
    d = DreamsForKids()
    d.main()