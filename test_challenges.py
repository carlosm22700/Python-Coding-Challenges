import pytest
import unittest
import solutions as c

# to run tests, execute `pytest` in the terminal

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


class TestSumOfMax(unittest.TestCase):

    def test_sum_of_maximums1(self):
        assert c.sum_of_maximums([[3,2,3], [5,2,8], [4,6,2]]) == 17
    
    def test_sum_of_maximums2(self):
        assert c.sum_of_maximums([[8,2,6], [2,9,17,8], [3,6,4], [-1, -23]]) == 30

    def test_sum_of_maximums3(self):
        assert c.sum_of_maximums([[1,2,3], [4,5], [6,7,8,9]]) == 17


class TestMajorityElement(unittest.TestCase):

    def test_majority_element1(self):
        assert c.majority_element([3, 2, 3]) == 3
    
    def test_majority_element2(self):
        assert c.majority_element([2, 2, 1, 1, 1, 2, 2, 3]) == 2

    def test_majority_element3(self):
        assert c.majority_element([3, 3, 5, 1, 2, 6, 2, 1, 1]) == 1


class TestSearchInsert(unittest.TestCase):

    def test_search_insert1(self):
        assert c.search_insert([1, 3, 5, 7], 5) == 2
    
    def test_search_insert2(self):
        assert c.search_insert([1, 3, 5, 6, 9], 2) == 1

    def test_search_insert3(self):
        assert c.search_insert([1, 3, 6], 7) == 3


class TestMaxProfit(unittest.TestCase):

    def test_max_profit1(self):
        assert c.max_profit([7,1,5,3,6,4]) == 5
    
    def test_max_profit2(self):
        assert c.max_profit([7,6,4,3,1]) == 0

    def test_max_profit3(self):
        assert c.max_profit([8,2,6,1,7]) == 6


class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome1(self):
        assert c.is_palindrome('A man, a plan, a canal: Panama') == True
    
    def test_is_palindrome2(self):
        assert c.is_palindrome('race a car') == False

    def test_is_palindrome3(self):
        assert c.is_palindrome(' ') == True
''' move this line below test you're working on
'''

