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
from collections import Counter


def sayHello():
    return 'Hello!'


'''
-----------------------------------------------------------------
Challenge: 01-fizz_buzz

Difficulty: Basic

Prompt:
Write a function called fizz_buzz that accepts a single numeric argument called max_num and returns a list.

The function code block will include:
- A list called `fb_list` that collects each element
- A variable `count` assigned the integer: 1
- count could be assigned from a range of 1 → max_num using an iterator (Hint: look at what range class does in python)

For each iteration:
- appending to bf_list one of four things for each number:
    - If the number is divisible by 3, append "fizz".
    - If the number is divisible by 5, append "buzz".
    - If the number is divisible by 3 and 5, append "fizzbuzz".

fizzbuzz(5) # [1, 2, 'fizz', 4, 'buzz']
fizzbuzz(15) # [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
-----------------------------------------------------------------
'''
# Your solution for 01-fizzbuzz here:


def fizz_buzz(max_num):
    fb_list = []
    for count in range(1, max_num+1):
        if count % 3 == 0 and count % 5 == 0:
            fb_list.append('fizzbuzz')
        elif count % 3 == 0:
            fb_list.append('fizz')
        elif count % 5 == 0:
            fb_list.append('buzz')
        else:
            fb_list.append(count)
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
length_of_last_word(' Face    difficult situations    and conflict head     on     ') # 2
-----------------------------------------------------------------
'''
# Your solution for 02-length_of_last_word here:


def length_of_last_word(s):
    words = s.split()
    if len(words) == 0:
        return 0
    else:
        return len(words[-1])


'''
-----------------------------------------------------------------
Challenge: 03-sum_of_maximums

Difficulty: Basic

Prompt:
Given a 2D array, get the max number of each list and return the sum of maximum numbers.

Examples:
sum_of_maximums([[3,2,3], [5,2,8], [4,6,2]])) # 17
sum_of_maximums([[8,2,6], [2,9,17,8], [3,6,4], [-1,-23]])) # 30
sum_of_maximums([[1,2,3], [4,5], [6,7,8,9]])) # 17

-----------------------------------------------------------------
'''
# Your solution for 03-sum_of_maximums:


def sum_of_maximums(arr):
    return sum(max(sub_arr) for sub_arr in arr)


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
    count = Counter(nums)
    for num in nums:
        if count(nums) > len(nums) // 2:
            return num


'''
-----------------------------------------------------------------
Challenge: 05-search_insert

Difficulty: Basic

Prompt:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Examples:
search_insert([1, 3, 5, 7], 5) # 2
search_insert([1, 3, 5, 6, 9], 2) # 1
search_insert([1, 3, 6], 7) # 3

-----------------------------------------------------------------
'''
# Your solution for 05-search_insert here:


def search_insert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


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

max_profit([1, 3, 6], 7) # 3

-----------------------------------------------------------------
'''
# Your solution for 06-max_profit here:


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


'''
-----------------------------------------------------------------
Challenge: 09-prime_factors

Difficulty: Intermediate

Prompt:
Write a function named prime_factors that accepts a whole number greater than one (1) as an argument and returns an list of that argument's prime factors.

The prime factors of a whole number are the prime numbers that, when multiplied together, equals the whole number.

If the argument provided is not greater than 1, or not a whole number, then primeFactors should return an empty list.

Examples:
prime_factors(2) //=> [2]
prime_factors(3) # [3]
prime_factors(4) # [2, 2]
prime_factors(18) # [2, 3, 3]
prime_factors(29) # [29]
prime_factors(105) # [3, 5, 7]
prime_factors(200) # [2, 2, 2, 5, 5]

-----------------------------------------------------------------
'''
# Your solution for 09-prime_factors here:


'''
-----------------------------------------------------------------
Challenge: 10a-create_phone_number

Difficulty: Basic

Prompt:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

If the string isn't a valid phone number: return 'Not a valid phone number'

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // '(123) 456-7890'
-----------------------------------------------------------------
'''
# Your solution for 10a-create_phone_number here:


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
