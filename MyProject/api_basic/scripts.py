import numpy as np
from datetime import timedelta, date

# flatten function changes list of list into a list
# reference: https://stackoverflow.com/a/952952

def flatten(t):
    return [item for sublist in t for item in sublist]

# miles function takes mileage and divides it into 1825 random values(approx. days for 5 years) and returns a list 
# reference: https://stackoverflow.com/a/49669044

def miles(n):
 totals = np.array([n]) 

 a = np.random.random((1825,1))  
 a = a/np.sum(a, axis=0) * totals  

 a = np.round(a)  
 remainings = totals - np.sum(a, axis=0)  
 for j, r in enumerate(remainings):  
    step = 1 if r > 0 else -1
    while r != 0:
        i = np.random.randint(6)
        if a[i,j] + step >= 0:
            a[i, j] += step
            r -= step

 mileage_list=flatten(a.tolist())
 return mileage_list

# dates function takes two dates and creates a list of all dates between these two dates including them
# reference: https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php 
      
def dates():        
 date_list=[]
 start_dt = date(2016, 8, 31)
 end_dt = date(2021, 8, 29)
 for dt in daterange(start_dt, end_dt):
    date_list.append(dt.strftime("%Y-%m-%d"))
 return date_list

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)




