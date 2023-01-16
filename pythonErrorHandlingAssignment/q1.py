"""
Create a function to read csv file and convert to python data structure (dict, list, set)
first_name, last_name,roll
John,Ken,11
Ronny,Baggs,12
Sam,Shone,13
"""

with open('text.csv', 'w') as f:
  f.writelines(['first_name, last_name,roll\n',
'John,Ken,11\n',
'Ronny,Baggs,12\n',
'Sam,Shone,13\n'])

def readFile(fileName):
  output = []
  with open(fileName, 'r') as f:
     line = f.read()  
  lines = line.splitlines()
  header = [heading for heading in lines[0].split(',')] #excluding headers from lines (list)
  for line in lines[1:]: #excluding header, the first element in lines list
    entry = [i for i in line.split(',')]
    tem = dict(zip(header, entry))  #zip function to map heading and entry
    output.append(tem)
  return output

print(readFile('text.csv'))
