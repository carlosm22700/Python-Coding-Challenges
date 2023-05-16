import pytest
import unittest
import solutions as c

# to run test, execute `pytest` in the terminal

''' 
@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 2], [2, 1]), 
     ([1, 2, 3], [3, 2, 1]), 
     ([1, 2, 3, 4], [4, 3, 2, 1]),
     (['hi', 'there'], ['there', 'hi'])],
)

def test_reverse(test_input, expected):
    assert reverse(test_input) == expected
'''

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz1(self):
        for i in c.fizzbuzz(20):
            if i in [3, 6, 9, 18]:
                assert i == 'Fizz'
    
    def test_fizzbuzz2(self):
        for i in c.fizzbuzz(30):
            if i in [5, 10, 20, 25]:
                assert c.fizzbuzz(i) == 'Buzz'

    def test_fizzbuzz3(self):
        for i in c.fizzbuzz(60):
            if i in [15, 30, 45, 60]:
                assert c.fizzbuzz(i) == 'FizzBuzz'


class TestLengthOfLastWord(unittest.TestCase):

    def test_lolw1(self):
        assert c.length_of_last_word('hello world') == 5
    
    def test_lolw2(self):
        assert c.length_of_last_word('tests are fun') == 3

    def test_lolw3(self):
        assert c.length_of_last_word('destiny  lies   above     us  ') == 2


class TestSearchInsert(unittest.TestCase):

    def test_search_insert1(self):
        assert c.search_insert([1, 3, 5, 7], 5) == 2
    
    def test_search_insert2(self):
        assert c.search_insert([1, 3, 5, 6, 9], 2) == 1

    def test_search_insert3(self):
        assert c.search_insert([1, 3, 6], 7) == 3


class TestMajorityElement(unittest.TestCase):

    def test_majority_element1(self):
        assert c.majority_element([3, 2, 3]) == 3
    
    def test_majority_element2(self):
        assert c.majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

    def test_majority_element3(self):
        assert c.majority_element([1, 3, 3, 5, 1, 2, 6, 2, 1]) == 1


''' move this line below test you're working on
'''