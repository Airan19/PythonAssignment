"""Create function to generate data randomly with python standard library"""

import random
import string

def randomData():
  output = []

  # fetching list of all aplhabets by using string module both upper as well as lower case
  alphabets = string.ascii_letters

  # using randrange method of random module to generate the length of output list, how many random words are gonna be there
  for _ in range(random.randrange(1,10)):

    # randomly determing the length of word in each loop
    random_length = random.randint(2,10)
    word = ''

    # looping for the random length we got above or length of word for this specific loop
    for loop in range(random_length):
      
      # this will determine whether to add a integer or a string in this particular loop in word
      integer = random.randrange(2)
      if integer:
        word += str(random.randint(0,10))
      else:
        word += random.choice(alphabets)
    output.append(word)
  return output


print(randomData())
print(randomData())
print(randomData())
print(randomData())
print(randomData())
