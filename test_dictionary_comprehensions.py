import pytest
import unittest

from dictionary_comprehensions import (
    lookup_capital,
    word_length,
    double_values,

)

class TestDictionaryComprehensions(unittest.TestCase):
    def test_lookup_capital(self):
        country_to_capital = {'Brazil': 'Brasilia', 'Morocco': 'Rabat', 'Sweden': 'Stockholm'}
        capital_to_country = {'Brasilia': 'Brazil', 'Rabat': 'Morocco', 'Stockholm': 'Sweden'}
        test_dict = lookup_capital(country_to_capital)
        self.assertEqual(test_dict, capital_to_country)

    def test_word_length(self):
        sentence = "It was a rainy Sunday and the trees were turning red"
        lengths_dict = {'It': 2, 'was': 3, 'a': 1, 'rainy': 5, 'Sunday': 6, 'and': 3, 'the': 3, 'trees': 5, 'were': 4, 'turning': 7, 'red': 3}
        test_dict = word_length(sentence)
        self.assertEqual(test_dict, lengths_dict)

    def test_double_values(self):
        numbers_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        test_dict = double_values(numbers_dict)
        doubled_dict = {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
        self.assertEqual(test_dict, doubled_dict)
