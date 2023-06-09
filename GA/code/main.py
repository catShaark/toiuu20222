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

# ga.initialize_population()
# print("----")
# for i in range(ga.n_pop):
#     print("id:{}| dotuongdong:{}| x:{} |y:{}".format(i,ga.pop[i].dotuongdong, ga.pop[i].x, ga.pop[i].y))

# print("-----")
# ga.evaluate_population()


# ga.sort_selective()

# # print(ga.fitness)

# ga.print_gen(0)

# print(ga.expulsion_set)

# ga.reproductionss()

# print("----")
# for i in range(ga.n_pop):
#     print("id:{}| dotuongdong:{}| x:{} |y:{}".format(i,ga.pop[i].dotuongdong, ga.pop[i].x, ga.pop[i].y))

# print("-----")

# sol_init = copy.deepcopy(sol)
# sol_init.x = ga.pop[0].x
# sol_init.y = ga.pop[0].y
# sol_init.tinhk_xy()
# sol_init.rang_buoc()



# if ga._sol_not_in_pop(sol_init):
#     print("ok")
# else: print("ko")

# print(ga.top_fitness)
# print(ga.expulsion_set)

# sol1 = ga.pop[0]

# sol2 = ga.pop[2]

# print(sol1.x)
# print(sol1.y)

# print(sol2.x)
# print(sol2.y)
# print()

# chi, suc = ga._laighep(0, 2)

# if suc:
#     print("ok")
#     print(chi[0].x)
#     print(chi[0].y)

# else:
#     print("ko")
#     # print(suc)
#     # print(chi[0].x)
#     # print(chi[0].y)


# dot, ok = ga._dotbien(0)
# if ok:
#     print(dot.x)
#     print(dot.y)
# else:
#     print("nhulo")