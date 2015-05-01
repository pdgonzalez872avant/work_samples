import unittest
import Archives_hw
import tempfile
import os
import shutil
import zipfile
import glob

class Test_Archives_hw(unittest.TestCase):

    def setUp(self):
        path_name = "archive_me"
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp(path_name)
        #self.dirname = tempfile.mkdtemp()
        os.chdir(self.dirname)

    def test_create_archive_directory_only(self):
        path = self.dirname
        #print(os.path.basename(path))
        expected = [os.path.basename(path)+"\\chico",
                    os.path.basename(path)+"\\groucho",
                    os.path.basename(path)+"\\harpo",
                    ]
#        expected = ["archive_me\\chico",
#                    "archive_me\\groucho",
#                    "archive_me\\harpo",
#                    ]
        names = ["groucho", "harpo", "chico"]

        for fn in names:
            f = open(os.path.join(path, fn), "w")
            f.close()

        observed = Archives_hw.create_archive_directory_only(path)
        # print(observed)

        self.assertEqual(observed, expected)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()