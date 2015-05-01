import unittest
import Archives_hw
import tempfile
import os
import shutil
import zipfile
import glob

class Test_player_scores(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("archive_me")
        os.chdir(self.dirname)
        
        
    def test_create_archive_directory_only(self):
        path = self.dirname 
        expected = ["archive_me\chico",
                     "archive_me\groucho",
                     "archive_me\harpo",
                    ]
        names = ["groucho", "harpo", "chico"]
        
        for fn in names:
            f = open(os.path.join(path, fn), "w")
            f.close()

        
        observed = Archives_hw.create_archive_directory_only(path)
        #print(self.dirname) -> C:\Users\pgonzale\AppData\Local\Temp\2\tmpc3yk811larchive_me
        
        print(observed)# C:\\my_arquive.zip
        print(path) # C:\Users\pgonzale\AppData\Local\Temp\4\tmpb4tiz9d6archive_me
        #print(glob.glob(os.path.join(path, "*")))
        #print(expected)
        
        self.assertEqual(observed, expected)
        

         
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()