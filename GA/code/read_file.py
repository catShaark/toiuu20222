
def read(path): 
    input_path = "/Users/duongdong/toiuu20222/Dataset/" + path

    with open(input_path, "r") as f:
        lines = f.read().splitlines()
    N, M, K = lines[0].strip().split()
    N = int(N)
    M = int(M)
    K = int(K)

    a,b,c,d,e,f = lines[1].strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)

    t = []
    t_tmp = lines[2].strip().split()
    for i in t_tmp:
        t.append(int(i))

    s = []
    for i in range(3, N+3):
        s_tmps = lines[i].strip().split()
        s_tmp = []
        for i in s_tmps:
            s_tmp.append(int(i))
        s.append(s_tmp)
    
    g = []
    for i in range(N+3, 2*N+3):
        g_tmps = lines[i].strip().split()
        g_tmp = []
        for i in g_tmps:
            g_tmp.append(int(i))
        g.append(g_tmp)

    path_out = path.replace("input", "output")
    path_output = "/Users/duongdong/toiuu20222/Output/GA/" + path_out
    return path_output,N,M,K,t,s,g,a,b,c,d,e,f




# N = 6
# M = 4
# K = 2
# a = 2
# b = 4
# c = 1
# d = 3
# e = 1
# f = 1

# t = [1, 3, 4, 2, 2, 3]

# s = [
#     [0,2,4,1,2,5],
#     [2,0,5,5,3,5],
#     [4,5,0,4,3,5],
#     [1,5,4,0,3,2],
#     [2,3,3,3,0,3],
#     [5,5,5,2,3,0],
# ]

# g = [
#     [3,5,1,5],
#     [5,2,5,3],
#     [3,1,3,3],
#     [5,5,1,3],
#     [4,5,4,1],
#     [5,3,4,5],
# ]