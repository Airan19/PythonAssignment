"""Develop a module over datetime library for calculating difference between 2 given time and date.​

"""

from datetime import datetime, date

def diff_of_date(date1, date2):
    try:
      d1 = date(date1[0], date1[1], date1[2])
      d2 = date(date2[0], date2[1], date2[2])
      c = (d1-d2)
    except:
      return ('Provide date in form of tuples like (year, month, day) and exclude any starting zeroes like 01 be like 1.')
    return c


def diff_of_time(time1, time2):
    try:
      t1 = datetime.strptime(time1, '%H:%M:%S')
      t2 = datetime.strptime(time2, '%H:%M:%S')
      d = str(t1-t2).split(':')
    except:
      return ('Provide time in string format of H:M:S (hours:minutes:seconds)')
    return ('Difference: ' +d[0]+' hours '+ d[1]+' minutes '+ d[2]+' seconds')


def diff_of_datetime(datetime1:tuple, datetime2:tuple):
  try:
    d1 = datetime(*datetime1)
    d2 = datetime(*datetime2)
    c = d1-d2
  except:
    return ('Provide date in form of tuples like (year[must], month, day, hour, minutes, seconds) and exclude any starting zeroes like 01 be like 1.')

  print(c)


print(diff_of_date((2023,1,16),(2023,1,14)))
print(diff_of_time("11:46:38", "2:13:57"))
print(diff_of_datetime((2023, 1, 16, 12,15), (2023, 1, 14, 10,4)))
