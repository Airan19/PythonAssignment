# -*- coding: utf-8 -*-
"""Aryan_Dev_Chourasia Python Assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10bJuvEC1kguuOj9BmQ3tSF2-QufGnbdW

Slicing
Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]
"""

def slicing(li, start, end):
  return li[start-1:end]


li = [1, 2, 3, 4, 5, 6]
print(slicing(li, 2, 5))

"""Condition
Check if string palindrome or not “ab”, “abc”, “aba”


"""

def isPalindrome(string):
  if string[::-1] == string:
    return True
  return False


li = ['ab','abc','aba']
for string in li:
  print(isPalindrome(string))

"""Loop
Check if string contains repeated characters “aab”, “abc”, “def”


"""

def repeatedCharacters(string):
  for ch in string:
    if string.count(ch) > 1:
      return True
  return False


li = ['aab', 'abc', 'def']
for string in li:
  print(repeatedCharacters(string))

"""Function
Convert all the above to function which can work on variadic number of arguments
"""

li = ['aab', 'abc', 'def', 'addcf', 'aabbaa']
print(slicing(li, 1,4))
print(isPalindrome(li[-1])) #'aabbaa
print(repeatedCharacters(li[3])) #'addcf