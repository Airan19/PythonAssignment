"""Create a function to division by provided argos: [[1, 0], [1, 2], [6, 3], [1, “a”] handle with specific errors.

"""

def division(li):
  for ele in li:
    try:
      dividend = int(ele[0])
      divisor = int(ele[1])
      ans = dividend / divisor
    except ZeroDivisionError as e:
      print(e)
    except ValueError as t:
      print(t)
    else:
      print(ans)
  return


li = [[1, 0], [1, 2], [6, 3], [1, 'a']]
division(li)
