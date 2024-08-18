def RadixSort (A):
  ArrayMax=max(A)
  pos=1
  while ArrayMax/pos> 0 :
    countSort(A,pos)
    pos=pos*10
  return A  
    
    
    
def countSort(A, pos) :
  count=[0]*len(A)
  
  for i in range(0,len(A)):
    count[int(A[i]/pos)%10]+=1
    
  for i in range(1,len(count)):
    count[i]=count[i]+count[i-1]  
    
  output = [0] * len(A)
  
  for i in range(len(A)-1,-1,-1):
    output[count[int(A[i]/pos)%10]-1] = A[i]
    count[int(A[i]/pos)%10] -= 1
    
  for i in range(0,len(A)) :
     A[i] = output[i]
     
    

A=[9,88,99,333,543,6,212,778,0,22]    
result=RadixSort(A)
print(result)
