# in java there is pre build collection called hashMap or LinkedHashMap 



from pprint import  pprint as pp

class HashTable:
  def __init__(self):
    self.Max =100
    self.arr=[[] for i in range (self.Max)]
    
    
  def get_hash(self, key):
    # here should be your hash function 
    h=0
    for i in key:
      h+=ord(i)
      
    return h%self.Max
  
  # def __setitem__(self , key , value ): this will give you the possibility to use this class Hashtable as a dictionary , btw Dictionary is the python specific implementation of the hash table
  def insert(self , key , value ):
    m= self.get_hash(key)
    found=False
    for index , element in enumerate(self.arr[m]):
      if len(element)==2 and element[0]==key:
        self.arr[m][index]=(key,value)
        found=True
        break
    if not found:  
      self.arr[m].append((key,value))
    # self.arr[m]=key
    
  # def __setitem__(self , key , value ):
  def search(self , key ) :
    m=self.get_hash(key)
    for element in self.arr[m]:
      if element[0]==key:
        return element[1]
    
    
    # return self.arr[m]
  
  # def __delitem__(self , key , value ):
  def delete(self, key):
    m=self.get_hash(key)
    for index , element in enumerate(self.arr[m]):
      if element[0]==key:
        del self.arr[m][index]

    
    
    # self.arr[m]=None
  
    
    
ht=HashTable()
ht.insert("april 9",23 )      
pp(ht.search("april 9"))
ht.insert("april 9",25 )      
pp(ht.arr)
ht.delete("april 9")
pp(ht.arr)

