import pytest
import unittest
import challenges as c

# to run tests, execute `pytest` in the terminal
''' move this line below the challenge's test that you're working currently on (option + down)

# Challenge: 01-fizz_buzz
class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz1(self):
        for i in c.fizzbuzz(20):
            if i in [3, 6, 9, 18]:
                assert i == 'fizz'
    
    def test_fizzbuzz2(self):
        for i in c.fizzbuzz(30):
            if i in [5, 10, 20, 25]:
                assert c.fizzbuzz(i) == 'buzz'

    def test_fizzbuzz3(self):
        for i in c.fizzbuzz(60):
            if i in [15, 30, 45, 60]:
                assert c.fizzbuzz(i) == 'fizzbuzz'


# Challenge: 02-length_of_last_word
class TestLengthOfLastWord(unittest.TestCase):

    def test_lolw1(self):
        assert c.length_of_last_word('hello world') == 5
    
    def test_lolw2(self):
        assert c.length_of_last_word('tests are fun') == 3

    def test_lolw3(self):
        assert c.length_of_last_word('destiny  lies   above     us  ') == 2


# Challenge: 03-sum_of_maximums
class TestSumOfMax(unittest.TestCase):

    def test_sum_of_maximums1(self):
        assert c.sum_of_maximums([[3,2,3], [5,2,8], [4,6,2]]) == 17
    
    def test_sum_of_maximums2(self):
        assert c.sum_of_maximums([[8,2,6], [2,9,17,8], [3,6,4], [-1, -23]]) == 30

    def test_sum_of_maximums3(self):
        assert c.sum_of_maximums([[1,2,3], [4,5], [6,7,8,9]]) == 17


# Challenge: 04-majority_element
class TestMajorityElement(unittest.TestCase):

    def test_majority_element1(self):
        assert c.majority_element([3, 2, 3]) == 3
    
    def test_majority_element2(self):
        assert c.majority_element([2, 2, 1, 1, 1, 2, 2, 3]) == 2

    def test_majority_element3(self):
        assert c.majority_element([3, 3, 5, 1, 2, 6, 2, 1, 1]) == 1


# Challenge: 05-search_insert
class TestSearchInsert(unittest.TestCase):

    def test_search_insert1(self):
        assert c.search_insert([1, 3, 5, 7], 5) == 2
    
    def test_search_insert2(self):
        assert c.search_insert([1, 3, 5, 6, 9], 2) == 1

    def test_search_insert3(self):
        assert c.search_insert([1, 3, 6], 7) == 3


# Challenge: 06-max_profit
class TestMaxProfit(unittest.TestCase):

    def test_max_profit1(self):
        assert c.max_profit([7,1,5,3,6,4]) == 5
    
    def test_max_profit2(self):
        assert c.max_profit([7,6,4,3,1]) == 0

    def test_max_profit3(self):
        assert c.max_profit([8,2,6,1,7]) == 6


# Challenge: 07-is_palindrome
class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome1(self):
        assert c.is_palindrome('A man, a plan, a canal: Panama') == True
    
    def test_is_palindrome2(self):
        assert c.is_palindrome('race a car') == False

    def test_is_palindrome3(self):
        assert c.is_palindrome(' ') == True


# Challenge: 08-title_to_number
class TestTitleToNumber(unittest.TestCase):

    def test_title_to_number1(self):
        assert c.title_to_number('A') == 1
    
    def test_title_to_number2(self):
        assert c.title_to_number('AB') == 28

    def test_title_to_number3(self):
        assert c.title_to_number('ZY') == 701


# Challenge: 09-prime_factors
class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors1(self):
        assert c.prime_factors(3) == [3]
    
    def test_prime_factors2(self):
        assert c.prime_factors(18) == [2, 3, 3]

    def test_prime_factors3(self):
        assert c.prime_factors(200) == [2, 2, 2, 5, 5]


# Challenge: 10a-create_phone_number
class TestCreatePhoneNumber(unittest.TestCase):

    def test_create_phone_number1(self):
        assert c.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == '(123) 456-7890'
    
    def test_create_phone_number2(self):
        assert c.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 'Not a valid phone number'

    def test_create_phone_number3(self):
        assert c.create_phone_number([2, 5, 3, 1, 2, 3, 0, 0, 0, 0]) == '(253) 123-0000'


# Challenge: 10b-rgb
class TestRGB(unittest.TestCase):

    def test_rgb1(self):
        assert c.rgb(255, 255, 255) == 'FFFFFF'
    
    def test_rgb2(self):
        assert c.rgb(0, 0, 0) == '000000'

    def test_rgb3(self):
        assert c.rgb(148, 0, 211) == '9400D3'
        
'''

