import reader

class Evo():
    knapsack=None
    items=None

    def __init__(self):
        rd = reader.Reader()
        f = rd.read("28.txt")
        self.knapsack = rd.getKnapsack(f)
        self.items = rd.getItems(f)

    def getStartPopulation(self,n):

        pass

    def selection(self):
        pass

    def crossbreeding(self,ind1,ind2):
        pass

    def mutation(self):
        pass

    def newPopulation(self):
        pass

    def evaluation(self):
        pass
