def unique_doubled(numbers):
    """write a set comprehension that takes a list of numbers and return
    a set of unique doubled numbers from that list"""

    return {
        x*2
        for x in numbers
    }

def unique_factorial():
    """write a set comprehension that returns a set containing the unique number
    of digits in the factorials between 0 and 20"""
    import math
    return {
        len(str(math.factorial(x)))
        for x in range(20)
    }

def unique_word(sentence):
    """write a set comprehension that takes a long sentence and returns a set
    containing only unique words. Make sure to account for punctuation and
    capitalization in the test string."""
    words = sentence.lower().replace('.', '').replace(',', '').split()

    return {
        word
        for word in words
    }

def unique_short_words(sentence):
    """write a set comprehension that takes a long sentence and returns a set
    containing only unique words that are three letters or fewer. Make sure to
    account for punctuation and capitalization in the test string."""
    words = sentence.lower().replace('.', '').replace(',', '').split()

    return {
        word
        for word in words
        if len(word) <=3
    }

def unique_consonants(sentence):
    """Remove all of the vowels in a string [make a set of the unique non-vowels]"""
    return {
        letter
        for letter in sentence.lower()
        if letter.lower() not in 'aeiou '
    }
