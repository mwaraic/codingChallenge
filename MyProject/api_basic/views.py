from rest_framework.views import APIView
from .models import Vehicle, Daily_Mileage
from .serializers import VehicleSerializer, VehicleGetSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from datetime import datetime
from .script import dates, miles

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class=VehicleSerializer
    permission_classes= [AllowAny]
    queryset=Vehicle.objects.all()
    
    def update(self, request, pk):
        
        mileage=json.loads(json.dumps(request.data))['mileage']
        
        if int(mileage)>=0 and Vehicle.objects.get(unit=pk).status=='Active':
           
           try:
               
              Daily_Mileage.objects.get(unit=Vehicle.objects.get(unit=pk), date=datetime.today().strftime('%Y-%m-%d'))
              return Response(status=status.HTTP_400_BAD_REQUEST)
          
           except:
               
              Daily_Mileage.objects.create(unit=Vehicle.objects.get(unit=pk), mileage=int(mileage), date=datetime.today().strftime('%Y-%m-%d'))     
              Vehicle.objects.filter(unit=pk).update(mileage=Vehicle.objects.get(unit=pk).mileage+int(mileage))
              return Response(status=status.HTTP_201_CREATED)  
            
        else:
            
           return Response(status=status.HTTP_400_BAD_REQUEST)

class VehicleListViewSet(viewsets.ModelViewSet):
    serializer_class=VehicleGetSerializer
    permission_classes= [AllowAny]
    queryset=Vehicle.objects.all()
    
    """ 
    for i, j in zip(dates(), miles(35459)):
        Daily_Mileage.objects.create(unit=Vehicle.objects.get(unit="F1AEJ13A"), date=i, mileage=j)
    
    """ 

class Distance(APIView):
    
    def post(self, request,pk):
        
        try:
            
         date = datetime.strptime(json.loads(json.dumps(request.data))['date'], '%Y-%m-%d')
         curr_date=datetime.today()
         total_days=(curr_date-date).days
         
         queryset=Daily_Mileage.objects.filter(unit=pk).order_by('-date')[:total_days]
         
         total=[]
         for i in queryset:
            total.append(i.mileage)
            
         return Response({"distance":sum(total)})
         
        except:
            
         return Response(status.HTTP_400_BAD_REQUEST)    

    