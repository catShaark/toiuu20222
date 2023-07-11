import time

class Bob():
    def __init__(self, input) -> None:
        pathout, N, M, K, t, s, g, a, b, c, d, e, f = input
        # input
        self.num_thesis = N
        self.num_teacher = M
        self.num_council = K
        self.thesis_teacher = t
        self.thesis_similarity_matrix = s
        self.thesis_teacher_similarity_matrix = g
        self.num_thesis_in_council_lower_bound = a
        self.num_thesis_in_council_upper_bound = b
        self.num_teacher_in_council_lower_bound = c
        self.num_teacher_in_council_upper_bound = d
        self.thesis_similarity_lower_bound = e
        self.thesis_teacher_similarity_lower_bound = f
        # use
        self.thesis_allocation = [0]*N
        self.teacher_allocation = [0]*M
        self.total_thesis_similarity = 0
        self.total_thesis_teacher_similarity = 0
        self.fit = 0
        self.thesis_allocation_map = dict()
        self.teacher_allocation_map = dict()
        self.time_start = time.time() 
        # output
        self.x_good = None
        self.y_good = None
        self.fit_good = 0
        self.path_output = pathout
        
    def run(self):
        with open(self.path_output, 'w') as file:
            file.truncate(0)

        start = [-1]*(self.num_thesis+self.num_teacher)
        self.try_bob(start, 0)

        with open(self.path_output, 'a') as file:
            print("    fitniss:{}".format(self.fit_good), file=file)
            print("    x:{} |y:{}".format(self.x_good, self.y_good), file=file)
            print("", file=file)

    def try_bob(self, a, t):
        if t == self.num_thesis+self.num_teacher:
            self.thesis_allocation = a[:self.num_thesis]
            self.teacher_allocation = a[self.num_thesis: t]
            self.tinhk_xy()
            if self.rang_buoc():
                if self.fit > self.fit_good:
                    self.fit_good = self.fit
                    self.x_good = self.thesis_allocation
                    self.y_good = self.teacher_allocation
        else:
            current_time = time.time() 
            if current_time - self.time_start > 600:
                return
            else:
                for i in range(self.num_council):
                    a[t] = i
                    self.try_bob(a, t+1)

    def tinhk_xy(self):
        k_x = {}
        for i in range(self.num_council):
            k_x[i] = []
        
        for i in range(self.num_thesis):
            k_x[self.thesis_allocation[i]] = k_x[self.thesis_allocation[i]] + [i]

        k_y = {}
        for i in range(self.num_council):
            k_y[i] = []
        
        for i in range(self.num_teacher):
            k_y[self.teacher_allocation[i]] = k_y[self.teacher_allocation[i]] + [i]

        self.thesis_allocation_map = k_x
        self.teacher_allocation_map = k_y

    def rang_buoc(self)->bool:
        # RB1
        for so_DA in self.thesis_allocation_map.values():       
            if (len(so_DA) > self.num_thesis_in_council_upper_bound) or (len(so_DA) < self.num_thesis_in_council_lower_bound):
                return False
        # RB2
        for so_GV in self.teacher_allocation_map.values():       
            if (len(so_GV) > self.num_teacher_in_council_upper_bound) or (len(so_GV) < self.num_teacher_in_council_lower_bound):
                return False
        # RB3
        for i in range(self.num_thesis):
            if self.thesis_allocation[i] == self.teacher_allocation[self.thesis_teacher[i] - 1]:
                return False
            
        # RB4 do tuong dong DA&DA
        if not self._DA_and_DA():
            return False
        # RB5 do tuong dong GV&DA
        if not self._GV_and_DA():
            return False
        
        self.fit = self.total_thesis_similarity/2 + self.total_thesis_teacher_similarity
        return True
    
    def _DA_and_DA(self):
        self.total_thesis_similarity = 0
        for xs in self.thesis_allocation_map.values():
            for DA1 in xs:
                for DA2 in xs:
                    if DA1 == DA2: continue
                    if self.thesis_similarity_matrix[DA1][DA2] < self.thesis_similarity_lower_bound:
                        return False
                    else:
                        self.total_thesis_similarity += self.thesis_similarity_matrix[DA1][DA2]
        return True
    
    def _GV_and_DA(self):
        self.total_thesis_teacher_similarity = 0
        for k in range(self.num_council):
            for GV in self.teacher_allocation_map[k]:
                for DA in self.thesis_allocation_map[k]:
                    if self.thesis_teacher_similarity_matrix[DA][GV] < self.thesis_teacher_similarity_lower_bound:
                        return False
                    else:
                        self.total_thesis_teacher_similarity += self.thesis_teacher_similarity_matrix[DA][GV]
        return True
