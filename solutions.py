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
Challenge: 03-search_insert

Difficulty: Basic

Prompt:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Examples:
search_insert([1, 3, 5, 7], 5)) # 2
search_insert([1, 3, 5, 6, 9], 2)) # 1
search_insert([1, 3, 6], 7)) # 3

-----------------------------------------------------------------
'''
# Your solution for 03-search_insert here:
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
    result = nums[0]

    for i in nums:
        if i == result:
            count += 1
        else:
            count -= 1

    return result