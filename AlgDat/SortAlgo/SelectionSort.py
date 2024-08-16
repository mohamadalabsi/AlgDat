def SelectionSort(A):
  i=0
  for i in range (len(A)-1):
    min=i
    j=i+1
    for j in  range(j,len(A)):
      if (A[j]<A[min]):
         min =j
         
    if (min != i ):
      A[min],A[i]=A[i],A[min]    
      
      
     
A=[3,1,4,0,6,2]      
print(A)
SelectionSort(A)
print(A)
       
    