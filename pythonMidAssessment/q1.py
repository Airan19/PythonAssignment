"""
[“name512”, “same1example”, “joy18full”] replace the digits from string inside list
"""

def stringFormat(str_list):
  output = []
  for word in str_list:
    # iterating the string word and only appending the ele which is not numeric by using the check from is.numeric function and simultaneously joining the list.
    formatted_word = ('').join([ ch for ch in word if not ch.isnumeric()])
    output.append(formatted_word)
  return output

li = ['name512', 'same1example', 'joy18full'] 
print(stringFormat(li))
