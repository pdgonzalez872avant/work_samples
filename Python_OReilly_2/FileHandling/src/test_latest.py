import unittest
import latest
import time
import os

PATHSTEM = "v:\\workspace\\FileHandling\\src\\"

class TestLatest(unittest.TestCase):
    
    def setUp(self):
        self.path = PATHSTEM
        self.file_names = ['file.old', 'file.bak', 'file.new']
        for fn in self.file_names:
            f = open(self.path + fn, "w")
            f.close()
            time.sleep(1)
    
    def test_latest_no_number(self):
        """
        Ensure that calling the function with no arguments returns
        the single most recently-created file.
        """
        expected = [self.path + 'file.new']
        latest_file = latest.latest(path=self.path)
        self.assertEqual(latest_file, expected, )
        
    def test_latest_with_args(self):
        """
        Ensure that calling the function with arguments of 2 and some 
        directory returns the two most recently created files in the directory.
        """
        expected = set([self.path + 'file.new',
                       self.path + 'file.bak'])
        latest_files = set(latest.latest(2, self.path))
        self.assertEqual(latest_files, expected)
        
    def tearDown(self):
        for fn in self.file_names:
            os.remove(self.path + fn)

if __name__ == "__main__":
    unittest.main()
    
