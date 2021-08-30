# Coding Challenge Sky IT Services Ltd.

## **Assumptions:** 
- Each asset has been on the road since 5 years (2016-09-01 and onwards)
- A random value has been assigned to mileage for each day within this 
period (stored in **Daily_Mileage** table)
- All random values in **Daily_Mileage** table for an asset sums to mileage in **Vehicle** table
- Whenver mileage is updated in **Vehicle** table for an asset, a concurrent entry is made in **Daily_Mileage** table
- An asset has become inoperative since 2021-08-29 and updating mileage for it would result in exception


### How I populated Daily_Mileage table?

- Lines 67-73 in https://github.com/mwaraic/codingChallenge/blob/main/MyProject/api_basic/views.py
- Various functions in scripts.py https://github.com/mwaraic/codingChallenge/blob/main/MyProject/api_basic/scripts.py

## **Run Commands:**

docker compose build <br/>
docker compose up<br/>

## **URL:**<br/>
127.0.0.1:8000/api/ <br/>

## **APIs:**

### **Vehicle:**<br/>
- Send a **GET** request on vehicle/ to retrieve the list
of assets. <br/>
- Send a **PUT** request on vehicle/<:unit#> with mileage 
property to update the mileage.<br/>

#### Example Of Request:</br>
{

"mileage": +int

}

### **Distance:**<br/>
- Send a **POST** request on distance/<:unit#> with date 
property to calculate distance. <br/>

#### Example Of Request:</br>

{

"date": "YYYY-mm-dd"

}

