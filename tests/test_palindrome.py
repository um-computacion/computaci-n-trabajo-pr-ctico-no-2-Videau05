import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("level"))
    
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Adan salta y Atlas nada"))
        self.assertTrue(is_palindrome("Sometamos o matemos"))
    
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))


if __name__ == '__main__':
    unittest.main()