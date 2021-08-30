import numpy as np
from datetime import timedelta, date

def flatten(t):
    return [item for sublist in t for item in sublist]

def miles(n):
 totals = np.array([n])  # don't use Sum because sum is a reserved keyword and it's confusing

 a = np.random.random((1825,1))  # create random numbers
 a = a/np.sum(a, axis=0) * totals  # force them to sum to totals

# Ignore the following if you don't need integers
 a = np.round(a)  # transform them into integers
 remainings = totals - np.sum(a, axis=0)  # check if there are corrections to be done
 for j, r in enumerate(remainings):  # implement the correction
    step = 1 if r > 0 else -1
    while r != 0:
        i = np.random.randint(6)
        if a[i,j] + step >= 0:
            a[i, j] += step
            r -= step

 mileage_list=flatten(a.tolist())
 return mileage_list

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
        
def dates():        
 date_list=[]
 start_dt = date(2016, 8, 31)
 end_dt = date(2021, 8, 29)
 for dt in daterange(start_dt, end_dt):
    date_list.append(dt.strftime("%Y-%m-%d"))
 return date_list






