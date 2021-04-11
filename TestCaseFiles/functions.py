import datetime
from ast import literal_eval

#define a function which determines the number of a month
def monthNumber(month):
    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    return months.index(month) + 1

def convertStringToDatetime(str):
    item = literal_eval(str)
    item_datetime = datetime.datetime(int(item[2]), monthNumber(item[1]), int(item[0]))
    return item_datetime