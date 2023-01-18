"""Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec"""

import time

def retry_deco(fun):
  def wrapper():
    
    # if we want to take user specific time intervals.
    # r_t = int(input('For how many times do you want to execute function: '))
    # r_i = int(input('Retry after how many seconds: '))

    r_t, r_i = 3,3
    print('Execution started')
    for i in range(r_t):
      time.sleep(r_i)
      print(fun(i+1, j=r_i))
    print('Execution ended')
  return wrapper


@retry_deco
def retry_fun(i=0, j=0):
  return (f'Function ran after {j} seconds, executed {i} time/s.')


retry_fun()
