import pytest
from test_questions import longest_word
# Test for longest_word function
def test_longest_word_case_1():
    assert longest_word("the banana is red") == ("banana", 6, 1)

def test_longest_word_case_2():
    assert longest_word("") == (-1, -1, -1)

def test_longest_word_case_3():
    assert longest_word("that cats") == ("that", 4, 1)

def test_longest_word_case_4():
    assert longest_word("it is great") == ("great", 5, 3)

def test_longest_word_case_5():
    assert longest_word("great it is") == ("great", 5, 1)

def test_longest_word_case_6():
    assert longest_word("I like candy right") == ("candy", 5, 3)

def test_longest_word_case_7():
    assert longest_word("ban") == ("ban", 3, 1)

def test_longest_word_case_8():
    assert longest_word("a b c") == ("a", 1, 1)

