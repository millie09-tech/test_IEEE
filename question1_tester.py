import pytest
from test_questions import list_of_int

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
