class MyHashMap(object):
    
    def __init__(self):
        self.myMap=[] 

    def put(self, key, value):
        x = [i for i in range (0, len(self.myMap)) if self.myMap[i][0] == key]
        if len(x) > 0:
            self.myMap[int(x[0])][1] = value
        else: 
            self.myMap.append([key,value])
            
    def get(self, key):
        index =[int(i[1]) for i in self.myMap if i[0] == key]
        if len(index) > 0:
            return int(index[0])
        else:
            return str(-1)
        

    def remove(self, key):
        index = [i for i in range (0, len(self.myMap)) if self.myMap[i][0] == key]
        if len(index) > 0:
            self.myMap.pop(int(index[0]))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
