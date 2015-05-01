"""Hw 2 - Demonstrates the unittest module in action."""

import unittest

def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]

def real_title(s):
    "This uses str.title() and returns the result"
    return str(s).title()


class Test_title(unittest.TestCase):
    
    #1
    def test_lowercase(self):
        self.assertEqual(title('lowercase'), 'Lowercase', "Should be Lowercase")
    def test_lowercase_real_title(self):
        self.assertEqual(real_title('lowercase'), 'Lowercase', "Should be Lowercase")
    
    #2
    def test_weirdcases(self):
        self.assertEqual(title('WeiRdCasES'), 'Weirdcases', "Should be Weirdcases")
    def test_weirdcases_real_title(self):
        self.assertEqual(real_title('WeiRdCasES'), 'Weirdcases', "Should be Weirdcases")
    
    #3
    def test_more_words(self):
        self.assertEqual(title('two words'), 'Two Words', 'Should be Two Words')
    def test_more_words_real_title(self):
        self.assertEqual(real_title('two words'), 'Two Words', 'Should be Two Words')
    
    #4
    def test_bad_input(self):
        self.assertRaises(TypeError, title, 1)
    def test_bad_input_real_title(self):
        self.assertRaises(TypeError, real_title, 1)
    
    
    
if __name__ == "__main__":
    unittest.main()
    
    
