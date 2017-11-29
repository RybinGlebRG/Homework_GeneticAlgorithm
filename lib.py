
def run():

    import reader

    import random

    rd=reader.Reader()
    f=rd.read("28.txt")
    ks=rd.getKnapsack(f)
    items=rd.getItems(f)


    from deap import creator
    from deap import base
    from deap import tools
    from deap import algorithms

    creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0, 1.0))
    creator.create("Individual", set, fitness=creator.Fitness)

    toolbox = base.Toolbox()

    toolbox.register("attr_item", random.randrange, rd.n)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attr_item, 50)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def evalKnapsack(individual):
        weight = 0.0
        volume = 0.0
        value = 0.0
        for index in individual:
            weight += items[index][0]
            volume += items[index][1]
            value += items[index][2]
        if len(individual) > rd.n or weight > ks[0] or volume>ks[1]:
            return 30000, 15000, 0  # Ensure overweighted bags are dominated
        return weight, volume, value

    def cxSet(ind1, ind2):
        temp = set(ind1)
        ind1 &= ind2
        ind2 ^= temp
        return ind1, ind2

    def mutSet(individual):
        """Mutation that pops or add an element."""
        if random.random() < 0.5:
            if len(individual) > 0:  # We cannot pop from an empty set
                individual.remove(random.choice(sorted(tuple(individual))))
        else:
            individual.add(random.randrange(rd.n))
        return individual,

    toolbox.register("evaluate", evalKnapsack)
    toolbox.register("mate", cxSet)
    toolbox.register("select", tools.selNSGA2)
    toolbox.register("mutate", mutSet)

    def main():
        random.seed(64)
        NGEN = 50
        MU = 50
        LAMBDA = 100
        CXPB = 0.7
        MUTPB = 0.2

        pop = toolbox.population(n=MU)

        algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN)

        return pop


    pop=main()
    big=0
    for i in range(0,len(pop)):
        if pop[i].fitness.values[2]>pop[big].fitness.values[2]:
            big=i
    new=list(pop[big])
    print(new)
    return new
