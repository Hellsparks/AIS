#---------------------------------------------------------------------------------
#                       Libraries and global variables
#---------------------------------------------------------------------------------
import random
import string
import matplotlib.pyplot as plt
import numpy as np

itteration  = 0
Generation  = []
results     = []
letters     = string.ascii_lowercase + " " +string.ascii_uppercase
GraphFit    = []
#---------------------------------------------------------------------------------
#                       Functions
#---------------------------------------------------------------------------------
def fitness(inPut):
    fitnessScore = 0
    for i in range(len(name)):
        if inPut[i] == name[i]:
            fitnessScore += 1
    return fitnessScore / len(name)

def uniCross(inA, inB):
    outA = []
    outB = []
    for i in range(len(name)):
        chance = random.randint(1, 100)
        if chance <= Cross:
            outA.append(inB[i])
            outB.append(inA[i])
        else:
            outA.append(inA[i])
            outB.append(inB[i])
    return "".join(outA), "".join(outB)

def sortGen(Gen, Res):
    bib = sorted(zip(Res, Gen))
    return bib[-1], bib[-2]

def mutation(guess, rate, size):
    foo = []
    foo[:0] = guess
    for i in range(size):
        digit = random.randint(0, len(name) - 1)
        chance = random.randint(1, 100)
        if chance <= rate:
            foo[digit] = "".join(random.choice(letters))
    return "".join(foo)

def populate(genlist, n):
    genFoo = [""] * n
    for i in range(1, len(genlist) + 1):
        for j in range(1, n + 1):
            if j % i == 0:
                genFoo[j - 1] = mutation(genlist[i - 1], mRate, mSize)
    return genFoo

#---------------------------------------------------------------------------------
#                       User input variables
#---------------------------------------------------------------------------------
gen     = 10               # num of instances per gen
name    = "Thomas Hellstrom Olsen"    # Key name
mRate   = 30                # Mutation chance %
mSize   = 3                 # Num of possible mutations
cutoff  = 100000              # Max itterations in while loop
Cross   = 10

#---------------------------------------------------------------------------------
#                       Initialization of random names
#---------------------------------------------------------------------------------
for i in range(gen):
    Generation.append("".join(random.choice(letters) for j in range(len(name))))
print("Population size:"+str(gen)+"   MutationRate:"+str(mRate)+"   MutationSize:"+str(mSize)+"   CrossoverChance:"+str(Cross)+"   Name: "+name)
#---------------------------------------------------------------------------------
#                       AG itteration
#---------------------------------------------------------------------------------
while itteration < cutoff:
    for i in range(gen):
        results.append(fitness(Generation[i]))
    best = sortGen(Generation, results)
    if best[-1][0] == 1:
        print("Generation: " + str(itteration) + ".   name found: " + str(best[-1][1]))
        fix, ax = plt.subplots()
        ax.plot(np.linspace(0, itteration, itteration), GraphFit)
        ax.set(xlabel="Generations", ylabel="Best Fitness score", title="Top preformers")
        plt.show()
        break
    print("Generation: " + str(itteration) + ".   Closest match: " + f'{best[-1][0]:.5f}' + "  Guess: " + str(best[-1][1]))
    GraphFit.append(best[-1][0])
    mangled = uniCross(best[0][1], best[1][1])
    Generation = []
    results = []
    Generation = populate(mangled, gen)
    itteration += 1
