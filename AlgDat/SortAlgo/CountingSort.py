def CountingSort(A):
  ArrayMax=max(A)
  count=[0]*(ArrayMax+1)
  i=0
  
  for i in range(len(A)):
    count[A[i]]+=1  
    
  for i in range(1,len(count)):
    count[i]=count[i]+count[i-1]
    
  output = [0] * len(A)
  
  for num in reversed(A):
     output[count[num] - 1] = num
     count[num] -= 1
     
  return output
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
A=[1,4,3,7,0,6,5,4,2,9,0,2,6,3,2,0]
result=CountingSort(A)
print(result)
  
