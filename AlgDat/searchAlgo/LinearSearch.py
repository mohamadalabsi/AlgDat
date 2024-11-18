
def LinearSearch (A :list , target ):
  for i in range(len (A)):
    if A[i]== target :
      return True
    else   :
      return False





A =[1,2,4,5,7,9,11]
target = 11 
result =LinearSearch(A , target)
print(result)
