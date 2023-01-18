"""
Build a counter generator
"""

def counter(start, end, interval):
  for i in range(start,end, interval):
    yield i

counter = counter(1,10,1)
for i in counter:
  print(i)

