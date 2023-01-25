"""Create function to check if date is in given range"""

from datetime import datetime

def date_in_range(date, start_date, end_date):

    # striping the date according the pattern or format we need or defined
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    if start_date_obj <= date_obj <= end_date_obj:
        return True
    else:
        return False


print(date_in_range("2023-10-01", "2022-01-25", "2023-10-31"))  
print(date_in_range("2020-09-01", "2022-03-14", "2022-10-12"))   
print(date_in_range("2021-08-01", "2019-05-07", "2021-10-26"))

