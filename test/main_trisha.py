class Dictionary():
    def __init__(self):
        self.dict = [None] * 50

    def add(self, key, value):
        keyConv = hash(key) % 50
        keyValP = [key,value]
        if(self.dict[keyConv] == None):
            multVal = [keyValP]
            self.dict[keyConv] = multVal
        else:
            self.dict[keyConv].append(keyValP)
        ##print("key is " + self.dict[keyConv][len(self.dict[keyConv]-1)][1])

    def retrieve(self,key):
        keyConv = hash(key) % 50
        if(self.dict[keyConv] == None):
            print("no key found")
        else:
            for i in range(len(self.dict[keyConv])):
                if(key == self.dict[keyConv][i][0]):
                    return self.dict[keyConv][i][1]
                else:
                    i = i +1

    def product(self, key1, key2):
        num1 = self.retrieve(key1)
        print("num1 is " + str(num1))
        num2 = self.retrieve(key2)
        print("num2 is " + str(num2))
        return num1*num2
