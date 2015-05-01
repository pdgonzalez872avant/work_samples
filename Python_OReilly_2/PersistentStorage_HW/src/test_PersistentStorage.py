import unittest
import PersistentStorage_HW
import tempfile
import os
import shutil

class Test_player_scores(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_player_score_function(self):
        
        name_score_exp = [('Bree', 50, 50),  #new score
                          ('Bree', 60, 60),  #higher score
                          ('Bree', -10, 60), #lower score
                          ('Fred', 0, 0)    #new score for new player
                          ]

        for name, score, exp in name_score_exp:
            observed = PersistentStorage_HW.player_scores(name, score)
            self.assertEqual(observed, exp, 
                             "I'm looking for: " + str(exp) + 
                             " but got:  " + str(observed))
         
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()