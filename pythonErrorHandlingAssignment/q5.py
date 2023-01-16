"""Create a file hash.txt with some content. Append '#' to every next character and display the content on screen.​
Example :​
If the file hash.txt has the following content stored in it :​
THE WORLD IS NOT FLAT​
"""

with open('hash.txt', 'w') as f:
  f.write('THE WORLD IS NOT FLAT')


def append(fileName):
  with open(fileName, 'r') as f:
    line = f.read()

  out = [ch+'#' for ch in line]
  return ('').join(out)


print(append('hash.txt'))

