#Sissi Xu S3C2
class Dictionary():
    def __init__(self,length=50):
        self.length = length
        self.key = [[] for i in range(50)]
        self.value = [[] for i in range(50)]
    def Hash(self,key):
        Address = 0
        for i in range (len(key)):
            Address += ord(str(key)[i])
        Address=Address % self.length
        return Address
    def insert(self,key,value):
        Index=self.Hash(key)
        while self.key[Index] !=[]:
            Index += 1
            if Index > self.length:
                Index=1
            print("Checking index",Index)
        self.key[Index] = key
        self.value[Index] = value
    def Find(self,SearchKey):
        Index=self.Hash(SearchKey)
        print("Checking index",Index)
        while (self.key[index] != SearchKey) and (self.key[index]!=[]):
            Index += 1
            if Index > self.length:
                Index=0
                print("Checking index",Index)
        if self.key[Index]:
            return self.value[Index]

