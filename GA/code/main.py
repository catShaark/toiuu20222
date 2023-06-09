import read_file
from Ga import *
from Solution import *

# /Users/duongdong/toiuu20222/Dataset/Medium/input_12_8_4.txt
FILE_NAME = "Medium/input_12_8_4.txt"

input = read_file.read(FILE_NAME)

sol = Solution(input)

N = 20
Gen = 10
remove = 3

ga = Ga(N, Gen, remove, sol)
ga.run()
