import read_file
from Ga import *
from Solution import *


FILE_NAME = "Small/input_6_4_2.txt"

input = read_file.read(FILE_NAME)

sol = Solution(input)

N = 20
Gen = 10
remove = 3

ga = Ga(N, Gen, remove, sol)
ga.run()
