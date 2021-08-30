from rest_framework.views import APIView
from .models import Vehicle, Daily_Mileage
from .serializers import VehicleSerializer, VehicleGetSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from datetime import datetime
from .scripts import dates, miles

class VehicleViewSet(viewsets.ModelViewSet):
    
    """
    Calls Vehicle method which serves the purpose
    of updating mileage of an asset.
    
    Send a PUT request on vehicle/<:unit#> with 
    mileage property to update the mileage.
    """
    
    serializer_class=VehicleSerializer
    permission_classes= [AllowAny]
    queryset=Vehicle.objects.all()
    
    def update(self, request, pk):
        
        mileage=json.loads(json.dumps(request.data))['mileage']

# checks if mileage is non-negative and status is active not inoperative for the given asset
        
        if int(mileage)>=0 and Vehicle.objects.get(unit=pk).status=='Active':
           
# try except block is set in place to check whether an entry for today has already been made          
           
           try:
               
              Daily_Mileage.objects.get(unit=Vehicle.objects.get(unit=pk), date=datetime.today().strftime('%Y-%m-%d'))
              return Response(status=status.HTTP_400_BAD_REQUEST)
          
           except:

# mileage in vehicle table is incremented and an entry is made in daily_mileage table for today 

              Daily_Mileage.objects.create(unit=Vehicle.objects.get(unit=pk), mileage=int(mileage), date=datetime.today().strftime('%Y-%m-%d'))     
              Vehicle.objects.filter(unit=pk).update(mileage=Vehicle.objects.get(unit=pk).mileage+int(mileage))
              return Response(status=status.HTTP_201_CREATED)  
            
        else:
            
           return Response(status=status.HTTP_400_BAD_REQUEST)

class VehicleListViewSet(viewsets.ModelViewSet):
    
    """
    Calls Vehicle List method which serves the purpose
    of listing all the assets.
    
    Send a GET request on vehicle/ to retrieve the list
    of assets.
    """
    
    serializer_class=VehicleGetSerializer
    permission_classes= [AllowAny]
    queryset=Vehicle.objects.all()


# populated daily_mileage table with dummy data for each asset using the code given below
    
    """ 
    for i, j in zip(dates(), miles(35459)):
        Daily_Mileage.objects.create(unit=Vehicle.objects.get(unit="F1AEJ13A"), date=i, mileage=j)
    
    """ 

class Distance(APIView):
    
    """
    Calls Distance method which serves the purpose
    of calulating distance an asset has travelled 
    from a particular date to today.
    
    Send a POST request on distance/<:unit#> with 
    date property to calulate distance.
    """
    
    def post(self, request,pk):
    
# try except block is set in place to check whether particular date to calculate distance from exists and have right syntax 
       
     try:
            
         date = datetime.strptime(json.loads(json.dumps(request.data))['date'], '%Y-%m-%d')
         curr_date=datetime.today()
# finding total number of days from the given date to current date          

         total_days=(curr_date-date).days
         
# future date provided 
         if(total_days==-1):
            return Response(status=status.HTTP_400_BAD_REQUEST)
         
# case where today's mileage is required 
         if(total_days==0):

# try except block to check whether mileage was reported today otherwise send 0 distance

             try:
                 mileage=Daily_Mileage.objects.get(unit=pk, date=date)
                 return Response({"distance": mileage })
             except:
                 return Response({"distance": 0})
        
# getting all entries in the daily_mileage table by reverse order of date for the asset (upto days required)
         
         queryset=Daily_Mileage.objects.filter(unit=pk).order_by('-date')[:total_days]
         
# calculating total distance travelled for the time period          

         total=[]
         for i in queryset:
            total.append(i.mileage)
            
         return Response({"distance":sum(total)})
         
     except:
            
         return Response(status=status.HTTP_400_BAD_REQUEST)    

    