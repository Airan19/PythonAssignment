"""
Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension
"""

def li_comprehension(li:list)->list:
  out = [i*2 for i in li]
  return out

li = [1, 2, 3, 4, 5]
print(li_comprehension(li))
