import read_file
from Ga import *
from Solution import *


FILE_NAME = "Small/input_6_4_2.txt"

input = read_file.read(FILE_NAME)

sol = Solution(input)

N = 20
Gen = 100
remove = 3

ga = Ga(N, Gen, remove, sol)

ga.initialize_population()
ga.evaluate_population()
print(ga.fitness)
ga.sort_selective()
ga.print_gen(0)

print(ga.top_fitness)
print(ga.expulsion_set)
