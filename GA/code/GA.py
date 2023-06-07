import Solution
import read_file

FILE_NAME = "Small/input_6_4_2.txt"

input = read_file.read(FILE_NAME)

sol = Solution.Solution(input)
class GA():
    def __init__(self, sol:Solution) -> None:
        self.sol_sample = sol

        self.pop = []
        self.fitness = []



while(1):
    sol.init_Sol()
    if sol.rang_buoc():
        break
print(sol.x)
print(sol.y)

