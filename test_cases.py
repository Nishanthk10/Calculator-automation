import Calculator
import pytest

def test_add():
    assert Calculator.add(2,3) == 5

def test_sub():
    assert Calculator.sub(10,5) == 5

def test_mult():
    assert Calculator.mult(4,2) == 8
 
# def test_add(): 
#     assert Calculator.add(100,43) == 103   #False test case