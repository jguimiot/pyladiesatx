def lookup_capital(countries_dict):
    """write a dictionary comprehension that can return a dictionary of capital: country
    pairs given a dictionary of country: capital pairs"""
    return {
        capital: country
        for country, capital in countries_dict.items()
    }

def word_length(sentence):
    """Use a dictionary comprehension to count the length of each word in a
    sentence and return a dictionary with the word as the key and the number of times it
    was used as the value """

    return {
        word:len(word)
        for word in sentence.split()
    }

def double_values(numbers_dict):
    """ write a dictionary comprehension to double the values associated with
    each key """
    return {
        key: value * 2
        for key, value in numbers_dict.items()
    }
