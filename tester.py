import pytest
from test_questions import list_of_int, longest_word, jacobsthal_num

# Test for list_of_int function
def test_list_of_int_case_1():
    assert list_of_int([5, 12, 18, 25, 30, 45, 55, 60, 11]) == [12, 18, 30]

def test_list_of_int_case_2():
    assert list_of_int([]) == []

def test_list_of_int_case_3():
    assert list_of_int([-6, 3, 6, 9, 12, 15, 16]) == [12, 16]

def test_list_of_int_case_4():
    assert list_of_int([0, 3, 6, 9]) == []

def test_list_of_int_case_5():
    assert list_of_int([12, 50]) == [12]

def test_list_of_int_case_6():
    assert list_of_int([12, 12, 12]) == [12, 12, 12]

def test_list_of_int_case_7():
    assert list_of_int([12, 11, 48]) == [12, 48]

def test_list_of_int_case_8():
    assert list_of_int([20]) == [20]

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

# Test for jacobsthal function
def test_jacobsthal_num_case_1():
    assert jacobsthal_num(0) == 0

def test_jacobsthal_num_case_2():
    assert jacobsthal_num(1) == 1

def test_jacobsthal_num_case_3():
    assert jacobsthal_num(2) == 1

def test_jacobsthal_num_case_4():
    assert jacobsthal_num(5) == 11

def test_jacobsthal_num_case_5():
    assert jacobsthal_num(7) == 43

def test_jacobsthal_num_case_6():
    assert jacobsthal_num(12) == 1365

def test_jacobsthal_num_case_7():
    assert jacobsthal_num(10) == 341

def test_jacobsthal_num_case_8():
    assert jacobsthal_num(3) == 3
