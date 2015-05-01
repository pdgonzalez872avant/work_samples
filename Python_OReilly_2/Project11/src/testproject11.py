import unittest
from project11 import build_row

class test_project11(unittest.TestCase):
    
    def test_retrieve_method1(self):
        import mysql.connector
        from database import login_info
        db = mysql.connector.Connect(**login_info)
        c = db.cursor()
        
        a = build_row('animal', 'id', 'name', 'family', 'weight', 
                  cursor=c, condition="WHERE name ='Peaches'")
    
        result = [i for i in a.retrieve(a,cursor=c, condition="WHERE name ='Peaches'")]    
#        print(result) # this returns what I want
#        expected = """["(1000, 'Peaches', 'Porcupine', 50)"]"""
        expected = "[animal_record(1000, 'Peaches', 'Porcupine', 50)]"
# diagnostic print
#        for i in a.retrieve(a,cursor=c, condition="WHERE name ='Peaches'"):
#            print(i)

        self.assertEqual(str(result), expected)

    def test_retrieve_method2(self):
        import mysql.connector
        from database import login_info
        db = mysql.connector.Connect(**login_info)
        c = db.cursor()
        
        a = build_row('animal', 'id', 'name', 'family', 'weight', 
                  cursor=c, condition="WHERE name ='Peaches'")
    
        result = [i for i in a.retrieve(a,cursor=c, condition="WHERE family ='Snake'")]    
        expected = "[animal_record(5, 'Sam', 'Snake', 24), animal_record(6, 'Steve', 'Snake', 35)]"
        

        self.assertEqual(str(result), expected)


if __name__ == "__main__":
    unittest.main()