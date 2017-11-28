

class Reader:
    n=0


    def read(self,path):
        f = open(path)
        return f
    def getKnapsack(self,file):
        limits=[]

        for string in file:
            for word in string.split():
                limits.append(float(word))
                if len(limits)==2:
                    return limits
    def getItems(self,file):
        items=[]

        for string in file:
            loc=[]
            for word in string.split():
                loc.append(float(word))
            items.append(loc)
            self.n+=1
        return items
