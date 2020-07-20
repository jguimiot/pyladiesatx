import pytest
import unittest

from set_comprehensions import (
    unique_doubled,
    unique_factorial,
    unique_word,
    unique_short_words,
    unique_consonants,
)

class TestSetComprehensions(unittest.TestCase):
    def test_unique_doubled(self):
        numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        unique_set = {0, 2, 4, 68, 6, 10, 42, 16, 26}
        test_unique = unique_doubled(numbers)
        self.assertEqual(test_unique, unique_set)

    def test_unique_factorial(self):
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}
        test_digits = unique_factorial()
        self.assertEqual(test_digits, digits)

    def test_unique_word(self):
        sentence = "Where she shines she sits, and where she sits she shines."
        test_unique = unique_word(sentence)
        unique_set = {'shines', 'she', 'sits', 'where', 'and', 'where'}
        self.assertEqual(test_unique, unique_set)

    def test_unique_short_words(self):
        sentence = "The cat in the hat is a cool cat in a hat"
        test_unique = unique_short_words(sentence)
        unique_short = {'hat', 'the', 'is', 'in', 'a', 'cat'}
        self.assertEqual(test_unique, unique_short)

    def test_unique_consonants(self):
        sentence = "The other day I met a bear"
        test_consonants = unique_consonants(sentence)
        consonants = {'d', 'h', 'b', 'm', 't', 'y', 'r'}
        self.assertEqual(test_consonants, consonants)
