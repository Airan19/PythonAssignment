"""Write a program that asks the user for two numbers. Then ask them if they would like to add, subtract, divide, or multiply these numbers. Perform the chosen operation on the values, showing the operation being performed.​
Write four functions, one for each mathematical operation.​
Example: add(), subtract(), Multiply(), and Divide()​

"""

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    return 'ZeroDivisionError'
  return num1 / num2

def inp():
  try:
    num1 = int(input('Enter number 1 (incase of subtract or divison, write accordingly): '))
    num2 = int(input('Enter number 2 (incase of subtract or divison, write accordingly): '))
    operation = int(input(('''Write the assigned NUMBER to perform operation :
    1 Addition
    2 Subtraction
    3 Multiplication
    4 Division\n''')))
    
    if operation == 1:
      ans = add(num1, num2)
    elif operation == 2:
      ans = subtract(num1, num2)
    elif operation == 3:
      ans = multiply(num1, num2)
    elif operation == 4:
      ans = divide(num1, num2)
    else:
      ans = 'Wrong Selection'
  except ValueError:
    print('Please provide input as integer.')
    ans = 'Wrong Input'
  finally:
    print('Answer:', ans)
    nex = input(('Write "q" to quit or "c" to continue: '))
    if nex == 'c':
      inp()
    elif nex == 'q':
      print('Quitting program')
    else:
      print('Unidentified input')
    return

inp()
