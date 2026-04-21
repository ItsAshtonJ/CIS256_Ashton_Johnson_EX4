#Ashton Johnson
#CIS256 Spring 2026
#Exercise Assignment 4

# Part 3: Writing Tests

import unittest
from guess_the_word import (
    valid_guess, select_random_word, display_word, answer_list_computers, answer_list_creatures
)

class TestGuessWord(unittest.TestCase):
    def test_word_from_category(self):
        # Make sure the word comes from the lists
        word1 = select_random_word(answer_list_computers)
        self.assertIn(word1, answer_list_computers, f"{word1} not in computer terms list")

        word2 = select_random_word(answer_list_creatures)
        self.assertIn(word2, answer_list_creatures, f"{word2} not in creatures list")

    def test_contains_letter(self):
        #Tests if c would be a valid guess
        guessed_letters = set('ab')
        self.assertTrue(valid_guess("c", guessed_letters))
    
    def test_invalid_guess(self):
        #Some invalid options to make sure false would work
        self.assertFalse(valid_guess("abc", set()))
        self.assertFalse(valid_guess("1", set()))
    
    def test_display_word(self):
        #sets the variables to help guide this test
        word = "frog"
        user_guess = set('ro')

        #gives expected result, and tells itself if that result is what it shown
        result = display_word(word, user_guess)
        expected = "_ r o _"
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
 
if __name__ == "__main__":
     unittest.main(verbosity=2, exit=False) #looked up verbosity explains more of unittest

