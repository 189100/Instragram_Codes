" @author: everydaycodings"

# Python program to Find day of
# the week for a given date
import datetime


def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))
    born = datetime.date(year, month, day)
    return born.strftime("%A")

# Driver program
date = '11 06 2016'
print(findDay(date))
