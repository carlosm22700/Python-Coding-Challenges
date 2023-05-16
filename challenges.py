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
fizzbuzz(15) # [1, 2, 'fizz', 4, 'buzz', 6, 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
-----------------------------------------------------------------
'''
# Your solution for 01-fizzbuzz here:

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

'''
-----------------------------------------------------------------
Challenge: 03-search_insert

Difficulty: Basic

Prompt:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Examples:
search_insert([1, 3, 5, 7], 5) # 2
search_insert([1, 3, 5, 6, 9], 2) # 1
search_insert([1, 3, 6], 7) # 3

-----------------------------------------------------------------
'''
# Your solution for 03-search_insert here:

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

'''
-----------------------------------------------------------------
Challenge: 05-sum_of_maximums

Difficulty: Basic

Prompt:
Given a 2D array, get the max number of each list and return the sum of maximum numbers.

Examples:
sum_of_maximums([[3,2,3], [5,2,8], [4,6,2]])) # 17
sum_of_maximums([[8,2,6], [2,9,17,8], [3,6,4], [-1,-23]])) # 30
sum_of_maximums([[1,2,3], [4,5], [6,7,8,9]])) # 17

-----------------------------------------------------------------
'''
# Your solution for 05-sum_of_maximums: