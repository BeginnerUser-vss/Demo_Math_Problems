# Write a function to detect 13th Friday. The function can accept two parameters, and both will be numbers. The first parameter will be the number indicating the month, and the second will be the year in four digits. Your function should parse the parameters, and it must return True when the month contains a Friday with the 13th, else return False.

import datetime
from datetime import datetime
import calendar

def has_friday_13(month, year):
    date = f'{month} 13 {year}'.format()
    spooky = datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[spooky]) == "Friday"

def main():
    print(has_friday_13(6,2001))