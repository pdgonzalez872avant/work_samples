"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""

import unittest
import tempfile
import shutil
import glob
import os


class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        #print("Created", self.dirname)
        os.chdir(self.dirname)

# modify so The test_1() method includes code to verify that the test directory contains only the files created by the for loop.
# Hint: You might create a set containing the list of three filenames, and then create a set from the os.listdir() method.

    def test_1(self):
        """Verify creation of files is possible"""
        for filename in sorted(["this.txt", "that.txt", "the_other.txt"]):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        self.assertEquals(os.listdir(self.dirname), sorted(["this.txt", "that.txt", "the_other.txt"]), 'Directories should match')

    def test_2(self):
        """Verify that the current directory is empty"""
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

#A test_3() method creates a binary file that contains exactly a million bytes, closes it 
#and then uses os.stat to verify that the file on disk is of the correct length (with os.stat
#, statinfo.st_size returns the size in bytes).

    def test_3(self):
        "Creating a file with fixed length of a million bytes"
        fn = "megabyte.text"
        mega_text = open(fn, "wb")
        mil = 1000000
        mega_text.write(bytes(mil))
        mega_text.close()
        mega_text_file_stats  = os.stat(fn)
        self.assertEqual(mega_text_file_stats.st_size, mil,
                         "the file size is not {} bytes".format(mil))


    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        #print("Deleted", self.dirname)

if __name__ == "__main__":
    unittest.main()