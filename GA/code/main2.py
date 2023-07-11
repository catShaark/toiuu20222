import read_file
from Ga import *
from Solution import *

# path_output,N,M,K,t,s,g,a,b,c,d,e,f
input = []


sol = Solution(input)

N = 10
Gen = 20

ga = Ga(N, Gen, sol)
ga.run()