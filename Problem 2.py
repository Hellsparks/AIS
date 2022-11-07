#---------------------------------------------------------------------------------
#                       Libraries and global variables
#---------------------------------------------------------------------------------
import random
import string
import matplotlib.pyplot as plt
import numpy as np

Best        = []
Deformation = 50
length      = 2000
AoIn        = ()
Force       = 100000
Emodul      = 210*(10**9)
List        = []
Result      = []
GenSize     = 100
cutoff      = 1000
itteration  = 0
Cross       = 50
mRate       = 30
#beam requirements
MaxThick    = 20
MaxWidth    = 200
MaxHeight   = 300
MinWidth    = 20
MinHeight   = 20
MinThick    = 10

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
def MomInertia(W,H,T):
    return ((W*(H**3))-(((W-T)/2)*((H-2*T)**3)))/12
def AreaBeam(W,H,T):
    return W*H - (((W-T)*(H-T)))
def Deformation(Q,E,I,L):
    return (Q/E*I) * ((L**3)/8)
def Fitness(A,D,Weight):
    return (A*Weight)*D
def SortBest():
    bib = sorted(zip(Result,List))
    return bib[0], bib[1]
def mutation(guess, rate):
    foo = []
    foo[:0] = guess
    for i in range(3):
        digit = random.randint(0, 2)
        chance = random.randint(1, 100)
        if chance <= rate:
            foo[digit] = foo[digit] +random.randint(-1, 1)
    return foo
def uniCross(inA, inB):
    outA = []
    outB = []
    for i in range(3):
        chance = random.randint(1, 100)
        if chance <= Cross:
            outA.append(inB[1][i])
            outB.append(inA[1][i])
        else:
            outA.append(inA[1][i])
            outB.append(inB[1][i])
    res = [outA,outB]
    return res
def populate(genlist, n):
    genFoo = []
    #print(mutation(genlist[0],mRate))
    for i in range(int(n/2)):
        genFoo.append(mutation(genlist[0],mRate))
    for i in range(int(n/2)):
        genFoo.append(mutation(genlist[1],mRate))
    return genFoo



for i in range(GenSize):
    foo = []
    foo.append(random.randint(MinWidth, MaxWidth))
    foo.append(random.randint(MinHeight, MaxHeight))
    foo.append(random.randint(MinThick, MaxThick))
    List.append(foo)

for i in range(cutoff):
    #print(List)
    for i in range(GenSize-1):
        W = clamp(List[i][0],MinWidth,MaxWidth)
        H = clamp(List[i][1],MinHeight,MaxHeight)
        T = clamp(List[i][2],MinThick,MaxThick)
        Result.append(int(Fitness(AreaBeam(W,H,T), Deformation(Force,Emodul,MomInertia(W,H,T),length), 1)))
    Best = SortBest()
    mangled = uniCross(Best[0],Best[1])
    List = []
    Result = []
    List = populate(mangled, GenSize)
    for i in range(GenSize):
        List[i][0] = clamp(List[i][0],MinWidth,MaxWidth)
        List[i][1] = clamp(List[i][1],MinHeight,MaxHeight)
        List[i][2] = clamp(List[i][2],MinThick,MaxThick)
print(Best[0])

print(Deformation(Force,Emodul,MomInertia(Best[0][1][0],Best[0][1][1],Best[0][1][2]),length))
