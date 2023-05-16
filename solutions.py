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