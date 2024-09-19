import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def SumRain(arr):
    sum=0
    for rainfall in arr:
        sum=sum+rainfall
    return sum     

def avgRainEachMonth(cityx,cityy,cityz):
   for c in range(0,6):
         sum=cityx[c]+cityy[c]+cityz[c]
         print("average rainfall for ",c+1,"th month is : ",sum/3,"mm")    

def TotalRain(arr,i):
    print("Total rainfall for city ",i,":",SumRain(arr),"mm")

def avgRain(arr,i):
    print("Average rainfall for city ",i,":",SumRain(arr)/len(arr),"mm")    

def avgRainAcrossAll(cityx,cityy,citz):
    sum=0
    sum=sum+SumRain(city_x)
    sum=sum+SumRain(city_y)
    sum=sum+SumRain(city_z)
    print("total average rainfall across all cities : ",sum/len(city_x),"mm")

city_x=np.array([100, 120, 85, 90, 110, 95])
city_y=np.array( [80, 75, 60, 95, 85, 90])
city_z=np.array([150, 140, 135, 160, 155, 170])


TotalRain(city_x,"X")
TotalRain(city_y,"Y")
TotalRain(city_z,"Z")

avgRain(city_x,"X")
avgRain(city_y,"Y")
avgRain(city_z,"Z")

avgRainAcrossAll(city_x,city_y,city_z)
avgRainEachMonth(city_x,city_y,city_z)

time=[1,2,3,4,5,6]
plt.plot(time,city_x,color='blue',label='Rainfall trend of City X')
plt.title('Rainfall Trends of City')
plt.plot(time,city_y,color='black',label='Rainfall trend of City Y')
plt.plot(time,city_z,color='green',label='Rainfall trend of City Z')
plt.xlabel('Months')
plt.ylabel('Rainfall in mm')
plt.legend()
plt.show()



range_x=city_x.max()-city_x.min()
range_y=city_y.max()-city_y.min()
range_z=city_z.max()-city_z.min()
print("range of city x is ","(",city_x.min(),",",city_x.max(),")")
print("range of city y is ","(",city_y.min(),",",city_y.max(),")")
print("range of city z is ","(",city_z.min(),",",city_z.max(),")")

y=np.array([range_x,range_y,range_z])
x=np.array(["city_X","city_y","city_z"])
plt.bar(x,y)
plt.show()


