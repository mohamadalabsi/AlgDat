def fakultaet(Number):
  if Number == 0 :
    return 1
  else :
    return Number *fakultaet(Number-1)
  
  
  
  
Number=input("Type the Number you want it's5 fakultaet  ")
# Number=4
result=fakultaet(int(Number)) #making sure that the number is in int forum not string 
print(result)
