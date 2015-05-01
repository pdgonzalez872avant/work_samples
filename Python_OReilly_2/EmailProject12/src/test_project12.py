import project12
import unittest

class DBTest(unittest.TestCase):
        
    def test_email_txt(self):
        msg = project12.write_email('anybody@home.com', 'another body of email woooo')
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())
        
        self.assertEqual(lst, ['multipart/mixed', 'text/plain'],
                         "Email with only text was not correctly formed")
    def test_email_image(self):
        msg = project12.write_email('anybody@home.com',
                                    'another body of email woooo',
                                    ['python_logo.png'])
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())
#            print(part)
        
        self.assertEqual(lst, ['multipart/mixed',
                               'text/plain',
                               'image/png',
                               'multipart/python_logo.png'],
                         "Email with image was not correctly formed")
    
    def test_email_audio(self):
        msg = project12.write_email('anybody@home.com',
                                    'another body of email woooo',
                                    ['cubs.mp3'])
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())
        
        self.assertEqual(lst, ['multipart/mixed',
                               'text/plain',
                               'audio/mpeg'],
                         "Email with audio was not correctly formed")

    def test_email_other(self):
        msg = project12.write_email('anybody@home.com',
                                    'another body of email woooo',
                                    ['cubs.xxx'])
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())
        
        self.assertEqual(lst, ['multipart/mixed',
                               'text/plain',
                               'multipart/cubs.xxx'],
                         "Email with 'other' was not correctly formed")
    
if __name__ == "__main__":
    unittest.main()
    
#print(write_email('anybody@home.com', 'another body of email woooo', ['python_logo.png', 'wooo.png', 'dog.txt', "cubs.html", "pat.xxx"]))