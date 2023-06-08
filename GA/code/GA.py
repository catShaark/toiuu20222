from tqdm import tqdm
import copy
import time

import Solution

class Ga():
    def __init__(self, N, Gen, remove, sol:Solution) -> None:
        self.sol_sample = sol
        self.Gen = Gen
        self.n_pop = N
        self.remove = remove

        self.pop = []
        self.fitness = []

        self.top_fitness = None
        self.expulsion_set = []

        self.path_output = sol.path_output

    def run(self):
        with open(self.path_output, 'w') as file:
            file.truncate(0)
        # khoi toa quan the
        self.initialize_population()
        # tinh ham muc tieu
        self.evaluate_population()
        # sap xep chon loc
        self.sort_selective()
        for gen in tqdm(range(self.Gen)):
            # in ra ca the tot nhat
            self.print_gen(gen)
            # sinh san
            self.reproductionss()
            # tinh ham muc tieu
            self.evaluate_population()
            # sap xep, chon loc
            self.sort_selective()
    def reproductionss(self):
        # lai 
        child = []
        child_tmp, err = self.laighep()

        # dot bien
        child_tmp2, err = self.dotbien()

        add = 0
        if len(child) < len(self.expulsion_set):
            add = len(self.expulsion_set) - len(child)
        # init

        
    
    def print_gen(self, gen):
        with open(self.path_output, 'a') as file:
            # Ghi các lời gọi print vào file
            print("Gen: {}".format(gen + 1), file=file)
            print("    fitniss:{}".format(self.top_fitness[1]), file=file)
            print("    x:{} |y:{}".format(self.pop[self.top_fitness[0]].x, self.pop[self.top_fitness[0]].y), file=file)
            print("", file=file)

    def sort_selective(self):
        fitness = self.fitness
        sorted_lose = sorted(fitness, key=lambda x: x[1], reverse=True)
        self.top_fitness = sorted_lose[0]
        self.expulsion_set = [sol_lose[0] for sol_lose in sorted_lose[self.n_pop - self.remove:]]
    
    def evaluate_population(self):
        for i in range(self.n_pop):
            fit = [i, self.pop[i].dotuongdong]
            self.fitness.append(fit)

    def initialize_population(self):
        start_time = time.time() 
        while(len(self.pop) <= self.n_pop):
            current_time = time.time()  # Lấy thời gian hiện tại
            elapsed_time = current_time - start_time  # Tính thời gian đã trôi qua
            if elapsed_time >= 6:  # Kiểm tra nếu đã đạt đến thời gian kết thúc (ví dụ: 60 giây - 1 phút)
                self.n_pop = len(self.pop)
                break  # Thoát khỏi vòng lặp

            sol_init = copy.deepcopy(self.sol_sample)
            sol_init.init_Sol()
            if (sol_init.rang_buoc()) and (self._sol_not_in_pop(sol_init)):
                self.pop.append(sol_init)
            else:
                del sol_init
                
    def _sol_not_in_pop(self, sol:Solution) -> bool:
        for sol_id in self.pop:
            if (sol_id.x == sol.x) and (sol_id.y == sol.y):
                return False
        return True
        

