"""
Tests File_Handling_Homework.py with TDD 
"""

import unittest
import tempfile
import shutil
import os
import File_Handling_Homework
import time


class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        self.file_names = ['test1.txt',
                           'test2.txt',
                           'test3.doc',
                           'test4.xls']
        for fn in self.file_names:
            f = open(self.dirname + '\\' + fn, "w")
            f.close()
            time.sleep(1)
        #print(os.path.exists(self.dirname + '\\' + 'test1.txt'))
        os.chdir(self.dirname)


    def test_Print_Count_Files_Directory(self):
        """Verifies examining the file and printing a summary"""
        observed = File_Handling_Homework.summarize_file_count(str(self.dirname) + '\\')
        expected = [('.doc', 1),('.txt', 2),('.xls', 1)]
        print(self.dirname)
        self.assertEquals(observed, expected,)


    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()