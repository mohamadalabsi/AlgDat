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
  
# def counting_sort(arr):
#     # Find the maximum value in the array
#     max_value = max(arr)
    
#     # Initialize the count array with zeros
#     count = [0] * (max_value + 1)
    
#     # Store the count of each element in the count array
#     for num in arr:
#         count[num] += 1
    
#     # Modify the count array to store the cumulative sum
#     for i in range(1, len(count)):
#         count[i] += count[i - 1]
    
#     # Initialize the output array
#     output = [0] * len(arr)
    
#     # Build the output array
#     for num in reversed(arr):
#         output[count[num] - 1] = num
#         count[num] -= 1
    
#     return output

# # Example usage:
# arr = [4, 2, 2, 8, 3, 3, 1, 7]
# sorted_arr = counting_sort(arr)
# print("Sorted array:", sorted_arr)
