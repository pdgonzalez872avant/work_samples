import os, email
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.text import MIMEText
import mimetypes


def write_email(email_address, input_string, list_attach=None):
    """
    Function to write emails
    """
    msg = MIMEMultipart()
    msg['From'] = 'always@me.com'  # constant
    msg['To'] = email_address  # adds email To
    msg.attach(MIMEText(input_string))  # adds text
    
    path = str(os.getcwd())
    
    if not list_attach:
        pass
    else:   
        for file in list_attach:
            fp = path + "\\" + file
            mime = mimetypes.guess_type(fp)  # Dangerous, there is a MimeTypes as well...
            
#            if not mime: # if guess_type returns None - this is not true, as it returned NoneType, must use a try except
#                mime = 'application/octet-stream' 
    
            try:
                mime_type = mime[0].split('/')[0]
                mime_type_encoding = mime[0].split('/')[1]
            except AttributeError:
                mime = 'application/octet-stream'
                mime_type = mime.split('/')[0]
                mime_type_encoding = mime.split('/')[1]
            
            if mime_type == 'image':
                to_attach = MIMEImage(file, mime_type_encoding)
                msg.attach(to_attach)
            if mime_type == 'text':
                to_attach = MIMEText(file, mime_type_encoding)
                msg.attach(to_attach)
            if mime_type == 'audio':
                to_attach = MIMEAudio(file, mime_type_encoding)
                msg.attach(to_attach)
            else:
                to_attach = MIMEMultipart(file, mime_type_encoding)
                msg.attach(to_attach)

#    return msg.as_string() # had to change this... wanted whole msg.
    return msg
    

#write_email('pdgonzalez872@gmail.com', 'body of email yeah yeah')
#print(write_email('anybody@home.com', 'another body of email woooo', ['python_logo.png', 'wooo.png', 'dog.txt', "cubs.html", "pat.xxx"]))
#print("*" * 10, 'Complete', "*" * 10)