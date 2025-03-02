import pytest
from test_questions import jacobsthal_num

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
