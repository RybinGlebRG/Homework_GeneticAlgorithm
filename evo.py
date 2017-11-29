import reader
import random

class Evo():
    knapsack=None
    items=None
    popN=1
    n=0
    fittestPopulation=None

    def __init__(self,n):
        self.n=n
        rd = reader.Reader()
        f = rd.read("28.txt")
        self.knapsack = rd.getKnapsack(f)
        self.items = rd.getItems(f)

    def getWVV(self,individual):
        weight=0
        volume=0
        value=0
        for i in range(0,len(individual)):
            if individual[i]==1:
                weight+=self.items[i][0]
                volume += self.items[i][1]
                value += self.items[i][2]
        return weight,volume,value

    def isFit(self,weight,volume):
        if weight> self.knapsack[0] or volume>self.knapsack[1]:
            return False
        else:
            return True

    def getStartPopulation(self,n):
        population=[]
        individual=[0 for i in self.items]
        while len(population)<n:
            i=random.randint(0,len(self.items))
            for j in range(i,len(individual)):
                individual[j]=1
                weight,volume,value=self.getWVV(individual)
                if not self.isFit(weight,volume):
                    individual[j]=0
                    break
            for j in range(0,i):
                individual[j]=1
                weight,volume,value=self.getWVV(individual)
                if not self.isFit(weight,volume):
                    individual[j]=0
                    break
            population.append(individual)
        return population

    def selection(self,population):
        amount=self.n*0.2
        selected=[]
        while len(selected)<amount:
            max=0
            for i in range(0,len(population)):
                if population[i] not in selected:
                    max=i
            for i in range(max+1,len(population)):
                weight, volume, value = self.getWVV(population[i])
                mw,mv,mva=self.getWVV(population[max])
                if population[i] not in selected and value>mva:
                    max=i
            selected.append(population[max])
        return selected

    def crossbreeding(self,selected):
        newborn=[]

        while len(newborn)<self.n*0.2:
            points=[]
            children=[]
            parents=[]
            points.append(0)
            while len(points)<3:
                i=random.randint(0,len(selected[0])-1)
                if i not in  points:
                    points.append(i)
            points.sort()
            parents.append(selected.pop(0))
            parents.append(selected.pop(0))
            for j in range(0,2):
                parent = 0
                indexes = [0 for i in parents[0]]
                for i in range(0,len(indexes)):
                    if i in points:
                        parent=random.randint(0,1)
                    indexes[i]=parent
                child=[]
                for i in range(0,len(indexes)):
                    child.append(parents[indexes[i]][i])
                children.append(child)
            w,v,va=self.getWVV(children[0])
            w2,v2,va2=self.getWVV(children[1])
            if self.isFit(w,v) and self.isFit(w2,v2):
                newborn.append(children[0])
                newborn.append(children[1])
        return newborn

    def mutation(self,newborn):

        i=random.randint(0,len(newborn)-1)
        for j in range(0,len(newborn[i])):
            newborn[i][j]^=1
        return newborn


    def newPopulation(self,mutated,population):
        # Хранит индексы
        worst=[]
        while len(worst)<self.n*0.2:
            min=0
            for i in range(0, len(population)):
                if i not in worst:
                    min = i
            for i in range(min+1,len(population)):
                weight, volume, value = self.getWVV(population[i])
                mw,mv,mva=self.getWVV(population[min])
                if i not in worst and value<mva:
                    min=i
            worst.append(min)
        newPopulation=[]

        for el in population:
            newPopulation.append(el)
        for i in range(0,len(worst)):
            newPopulation[worst[i]]=mutated[i]
        return newPopulation



    def evaluation(self,newPopulation,population):
        maxP = 0
        for i in range(1, len(population)):
            weight, volume, value = self.getWVV(population[i])
            mw, mv, mva = self.getWVV(population[maxP])
            if  value > mva:
                maxP = i
        maxN = 0
        for i in range(1, len(newPopulation)):
            weight, volume, value = self.getWVV(newPopulation[i])
            mw, mv, mva = self.getWVV(newPopulation[maxN])
            if  value > mva:
                maxN = i

        if min(maxP,maxN)*0.1+min(maxP,maxN)>max(maxP,maxN):
            return True
        else:
            return False

    def routine(self,population):
        selected=self.selection(population)
        newborn=self.crossbreeding(selected)
        mutated=self.mutation(newborn)
        newPopulation=self.newPopulation(mutated,population)
        isConverged=self.evaluation(newPopulation,population)
        population=newPopulation
        self.popN+=1
        return isConverged

    def check(self,fittestPopulation):
        for individual in fittestPopulation:
            w,v,va=self.getWVV(individual)
            if w>self.knapsack[0] or v>self.knapsack[1]:
                raise Exception("Incorrect weight or volume")


    def run(self):
        population=self.getStartPopulation(self.n)

        while True:
            isConverged=self.routine(population)
            if isConverged or self.popN>=100:
                break
        self.fittestPopulation=population
        self.check(self.fittestPopulation)

        maxP = 0
        for i in range(1, len(self.fittestPopulation)):
            weight, volume, value = self.getWVV(self.fittestPopulation[i])
            mw, mv, mva = self.getWVV(self.fittestPopulation[maxP])
            if  value > mva:
                maxP = i
        indexes=[]
        for i in range(0,len(self.fittestPopulation[maxP])):
            if self.fittestPopulation[maxP][i]==1:
                indexes.append(i)
        print(indexes)
        return indexes
