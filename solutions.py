'''
-----------------------------------------------------------------
Challenge: 00-sayHello (example)

Difficulty: Basic

Prompt:

Write a function called sayHello that returns the string "Hello!".

Examples:

sayHello() # => Hello!
-----------------------------------------------------------------*/
'''
# Your solution for 00-sayHello (example) here:

def sayHello():
    return 'Hello!'

'''
-----------------------------------------------------------------
Challenge: 01-fizzbuzz

Difficulty: Basic

Prompt:
Write a function called fizzbuzz that accepts a single numeric argument called max_num.

The function code block will include:
- A variable `count` assigned the integer: 1
- count could be assigned from a range of 1 → max_num using an iterator (Hint: look at what range class does in python)

For each iteration:
- printing 1 of four things for each number.
- If the number is divisible by 3, `print` "fizz".
- If the number is divisible by 5, `print` "buzz".
- If the number is divisible by 3 and 5, `print` "fizzbuzz".

Examples:
fizzbuzz(15)
1
2
fizz
4
buzz
6
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
-----------------------------------------------------------------
'''
# Your solution for 01-fizzbuzz here:
def fizzbuzz(max_num):
    fb_list = []
    for i in range(1, max_num + 1):
        if i % 15 == 0:
            fb_list.append('FizzBuzz')
        elif i % 3 == 0:
            fb_list.append('Fizz')
        elif i % 5 == 0:
            fb_list.append('Buzz')
        else:
            fb_list.append(i)
    
    return fb_list

'''
-----------------------------------------------------------------
Challenge: 02-length_of_last_word

Difficulty: Basic

Prompt:
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Examples:
length_of_last_word('hello world') # 5
length_of_last_word("I'm sorry Dave, I'm afraid I can't do that") # 4
length_of_last_word(' Face    difficult situations    and conflict head     on     ' # 2
-----------------------------------------------------------------
'''
# Your solution for 02-length_of_last_word here:
def length_of_last_word(s):
        length = 0
        i = len(s) - 1
        # if there are spaces after the last word, decrement i until character is found
        while s[i] == ' ' and i >= 0:
            i -= 1
        
        # count the characters in the last word
        while s[i] != ' ' and i >= 0:
            length += 1
            i -= 1

        return length


'''
-----------------------------------------------------------------
Challenge: 03-sum_of_maximums

Difficulty: Basic

Prompt:
Given a 2D array, get the max number of each list and return the sum of maximum numbers.

Examples:
sum_of_maximums([[3,2,3], [5,2,8], [4,6,2]])) # 14
sum_of_maximums([[8,2,6], [2,9,17,8], [3,6,4], [-1,-23]])) # 31
sum_of_maximums([[1,2,3], [4,5], [6,7,8,9]])) # 17

-----------------------------------------------------------------
'''
# Your solution for 03-sum_of_maximums:
def sum_of_maximums(nums):
    sum = 0
    for num in nums:
        sum += max(num)
    
    return sum

'''
-----------------------------------------------------------------
Challenge: 04-majority_element

Difficulty: Basic

Prompt:
Given an list nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the list.

Examples:
majority_element([3,2,3])) # 3
majority_element([2,2,1,1,1,2,2]) # 2

-----------------------------------------------------------------
'''
# Your solution for 04-majority_element:
def majority_element(nums):
    count = 0
    result = None

    for i in nums:
        if count == 0:
            result = i
        if i == result:
            count += 1
        else:
            count -= 1

    return result

    
'''
-----------------------------------------------------------------
Challenge: 05-search_insert

Difficulty: Basic

Prompt:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Examples:
search_insert([1, 3, 5, 7], 5)) # 2
search_insert([1, 3, 5, 6, 9], 2)) # 1
search_insert([1, 3, 6], 7)) # 3

-----------------------------------------------------------------
'''
# Your solution for 05-search_insert here:
import math
def search_insert(nums, target):
    length = len(nums)
    if length == 0 or target in [0, 1]:
        return 0
    elif target <= nums[0]:
        return nums[0] - 1
    elif target > nums[length - 1]:
        return length
    elif target == nums[length - 1]:
        return length - 1
    else:
        half = math.ceil(len(nums) / 2)
        if nums[half] < target:
            return search_insert(nums[half:], target)
        else:
            return search_insert(nums[:half], target)

'''
-----------------------------------------------------------------
Challenge: 06-max_profit

Difficulty: Intermediate

Prompt:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
max_profit([7,1,5,3,6,4]) # 2
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

max_profit([7,6,4,3,1]) # 0
Explanation: In this case, no transactions are done and the max profit = 0.

max_profit([8,2,6,1,7]) # 6

-----------------------------------------------------------------
'''
# Your solution for 06-max_profit here:
def max_profit(prices):
    cheapest = prices[0]
    max_profit = 0

    for price in prices:
        if price < cheapest:
            cheapest = price
        
        curr_profit = price - cheapest
        max_profit = max(curr_profit, max_profit)

    return max_profit


'''
-----------------------------------------------------------------
Challenge: 07-is_palindrome

Difficulty: Intermediate

Prompt:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:
is_palindrome('A man, a plan, a canal: Panama') # True
Explanation: "amanaplanacanalpanama" is a palindrome.

is_palindrome('race a car') # False
is_palindrome(' ') # True

-----------------------------------------------------------------
'''
# Your solution for 07-is_palindrome here:
import re
def is_palindrome(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1

    return True


'''
-----------------------------------------------------------------
Challenge: 08-title_to_number

Difficulty: Intermediate

Prompt:
Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Examples:
title_to_number('A') # 1

title_to_number('AB') # 28
title_to_number('ZY') # 701


-----------------------------------------------------------------
'''
# Your solution for 08-title_to_number here:
def title_to_number(column_title):
    columns = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26,
        }
    
    if len(column_title) == 1:
        return columns.get(column_title)
        
    col_length = len(column_title)
    
    col_num = 0
    for i in range(col_length):
        col_pos = 26 ** (col_length - 1 - i)
        col_num += columns.get(column_title[i]) * col_pos
    
    return col_num


'''
-----------------------------------------------------------------
Challenge: 09-prime_factors

Difficulty: Intermediate

Prompt:
Write a function named prime_factors that accepts a whole number greater than one (1) as an argument and returns an list of that argument's prime factors.

The prime factors of a whole number are the prime numbers that, when multiplied together, equals the whole number.

If the argument provided is not greater than 1, or not a whole number, then primeFactors should return an empty list.

Examples:
prime_factors(2) # [2]
prime_factors(3) # [3]
prime_factors(4) # [2, 2]
prime_factors(18) # [2, 3, 3]
prime_factors(29) # [29]
prime_factors(105) # [3, 5, 7]
prime_factors(200) # [2, 2, 2, 5, 5]

-----------------------------------------------------------------
'''
# Your solution for 09-prime_factors here:
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_factors(num, primes=None):
    # Common gotcha: Python’s default arguments are evaluated once when the function is defined
    # A new list is created once when the function is defined, and the same list is used in each successive call.
    # A way around this is the following lines
    if primes is None:
        primes = []

    if is_prime(num):
        primes.append(num)
        return sorted(primes)
    
    for i in range(2, num):
        is_divisible = num % i == 0
        if is_prime(i) and is_divisible:
            primes.append(i)
            num = int(num / i)
            return prime_factors(num, primes)

'''
-----------------------------------------------------------------
Challenge: 10a-create_phone_number

Difficulty: Basic

Prompt:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // '(123) 456-7890'
-----------------------------------------------------------------
'''
# Your solution for 10a-create_phone_number here:
import re
def create_phone_number(nums):
    if len(nums) != 10:
        return 'Not a valid phone number'
    
    stringify_nums = ''
    for num in nums:
        stringify_nums += str(num)

    # regex
    return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', stringify_nums)

'''
-----------------------------------------------------------------
Challenge: 10b-rgb

Difficulty: Basic

Prompt:
The RGB function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

**Note**: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples:
rgb(255, 255, 255) # 'FFFFFF'
rgb(255, 255, 300) # 'FFFFFF'
rgb(0,0,0) # '000000'
rgb(148, 0, 211) # '9400D3'
-----------------------------------------------------------------
'''
# Your solution for 10b-rgb here:
import math
def rgb(r, g, b):
    double_digits = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    hex_conversion = ''
    arr = [r, g, b]

    for num in arr:
        if num % 1 != 0:
            num = round(num)
        if num > 255:
            num = 255
        elif num < 0:
            num = 0

        whole_number = math.floor(num / 16)
        remainder = num % 16

        if whole_number < 10:
            hex_conversion += str(whole_number)
        else:
            hex_conversion += double_digits[whole_number]
        if remainder < 10:
            hex_conversion += str(remainder)
        else:
            hex_conversion += double_digits[remainder]
    return hex_conversion