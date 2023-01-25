"""[1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce"""

def separate(ele_list):

  # using filter function to iterate the list and apply given function on each element, element will be added if it satisfies the condition
  
  # digits = list(filter(lambda x: type(x) == int, ele_list))
  # or
  digits = list(filter(lambda x: isinstance(x, int), ele_list))


  # alphabets = list(filter(lambda y: type(y) == str, ele_list))
  # or
  alphabets = list(filter(lambda y: isinstance(y,str), ele_list))
  return digits, alphabets


li = [1, 'a', 2, 'b', 3, 'c']
print(separate(li))
