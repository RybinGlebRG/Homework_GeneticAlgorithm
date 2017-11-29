import reader

class Packer():
    knapsack=None
    items=None

    def __init__(self):
        rd = reader.Reader()
        f = rd.read("28.txt")
        self.knapsack = rd.getKnapsack(f)
        self.items = rd.getItems(f)

    def pack(self,ind1,ind2):
        w1,v1,va1=self.getWVV(ind1)
        w2,v2,va2=self.getWVV(ind2)

        payload={"1": {"value":int(va1),"weight":int(w1),"volume":int(v1), "items": ind1 },"2":{"value":int(va2),"weight":int(w2),"volume":int(v2), "items": ind2 }}
        return payload

    def getWVV(self,ind):
        w=0
        v=0
        va=0

        for el in ind:
            w+=self.items[el][0]
            v += self.items[el][1]
            va += self.items[el][2]

        return w,v,va

