#Ashton Johnson
#CIS256 Spring 2026
#Exercise Assignment 4

# Part 3: Writing Tests

import pytest
from guess_the_word import (
    valid_guess, select_random_word, display_word
)

def test_word_from_category():
      # Make sure the word comes from the lists
      from guess_the_word import answer_list_computers, answer_list_creatures

      word1 = select_random_word(answer_list_computers)
      assert word1 in answer_list_computers, f"'{word1}' not in computer terms list"

      word2 = select_random_word(answer_list_creatures)
      assert word2 in answer_list_creatures, f"'{word2}' not in creatures list"

def test_display_word():
     word = "frog"
     user_guess = set('ro')

     result = display_word(word, user_guess)
     expected = "_ r o g"
     assert result == expected, f"Expected '{expected}', got '{result}'"

def test_valid_guess():    
    guessed_letters = set('ab')

    #Test some valid or true statements
    assert valid_guess('c', guessed_letters) == True #allows valid guess
    assert valid_guess('Z', set()) == True #allow uppercase

    #Test the false statements
    assert valid_guess('abc', set()) == False #dont allow multiple letters
    assert valid_guess('1', set()) == False  #dont allow numbers