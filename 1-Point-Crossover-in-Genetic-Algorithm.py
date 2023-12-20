
# lib to generate a random number 
import random 
  
# function for implementing the 1-point crossover 
def crossover(l, R): 
  
# converting the string to list for crossover 
    l = list(l) 
    R = list(R) 
  
# generating the random number to  crossover 
    k = random.randint(0, 15) 
    print("Crossover point :", k) 
  
# swap the genes 
    for i in range(k, len(s)): 
        l[i], R[i] = R[i], l[i] 
    l = ''.join(l) 
    R = ''.join(R) 
    print(l) 
    print(R, "\n\n") 
    return l, R 
  
  
# patent chromosomes: 
  
s = '1100110110110011'
p = '1000110011011111'
print("Parents") 
print("P1 :", s) 
print("P2 :", p, "\n") 
 
# next generation crossover 
for i in range(5): 
    print("Generation ", i+1, "Childrens :") 
    s, p = crossover(s, p) 
