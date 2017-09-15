a = [11,8,12,0]
b = [1,2,3,4,5,6,7,8,9,10]


def minn(arr):
 mn=0
 i=1
 while (i<len(arr)):
     if arr[i]<arr[mn]:
         mn=i
     i=i+1
 print(arr[mn])
 None


def SrArf(arr):
 i=0
 sum=0
 while (i<len(arr)):
     sum=sum+arr[i]
     i=i+1
 print(sum/len(arr))
 None


minn(a)
SrArf(b)