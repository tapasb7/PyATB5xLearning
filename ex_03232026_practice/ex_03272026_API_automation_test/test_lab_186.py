import pytest

def method_1():
    print("Not part of Pytest")

def test_method_2():
    print("Well done! This my pytest method_2")
    assert 5 == 5

def test_method_3():
    print("Well done! This is not pytest method_3")
    assert 5 == 5

