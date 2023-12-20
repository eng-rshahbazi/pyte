import random

def uniform_binary_crossover(parent_one, parent_two):
    string_length = len(parent_one)
    child_one = ""
    child_two = ""
    for i in range(string_length):
        if random.random() < 0.5:
            child_one += parent_one[i]
            child_two += parent_two[i]
        else:
            child_one += parent_two[i]
            child_two += parent_one[i]
    return child_one, child_two
print(child_one, child_two)
