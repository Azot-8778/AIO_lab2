import numpy as np

def calc_c(p, M):
    s = 0
    for j in M:
        s += p[j]
        
    return s

def calc_w(w, M):
    s = 0
    for j in M:
        s += w[j]
        
    return s

def get_ub_lb(n, W, p, w, exclude, include):
    zh = calc_c(p, include)
    wh = calc_w(w, include)
    Xh = include.copy()
    
    q = np.array(p) / np.array(w)
    idx_q_sorted = np.argsort(q)[::-1]
    
    for idx in idx_q_sorted:
        if idx in Xh or idx in exclude:
            continue
        
        if wh + w[idx] > W:
            break
        
        wh += w[idx]
        zh += p[idx]
        Xh.add(idx)
    
    w_gap = W - wh
    prop = w_gap / w[idx]
    
    z_ub = zh + prop * p[idx]
    
    return z_ub, zh, Xh

def solve(n, W, p, w, branching_idx, best_sol=0, best_X=set(), exclude=set(), include=set()):
    if branching_idx >= n:
        return best_sol, best_X

    ub, lb, Xh = get_ub_lb(n, W, p, w, exclude, include) # Когда запускаем с пустыми параметрами(изначально)
                                                         # то получаем начальное решение
    got_w = calc_w(w, Xh)
    
    if lb > best_sol and got_w <= W:
        best_sol = lb
        best_X = Xh
    
    if best_sol >= ub:
        return best_sol, best_X
    
    ne = exclude.copy()
    ne.add(branching_idx)
    ni = include.copy()
    ni.add(branching_idx)
    
    sol1, sol1X = solve(n, W, p, w, branching_idx+1, best_sol, best_X, ne, include)
    if sol1 > best_sol:
        best_sol = sol1
        best_X = sol1X
    sol2, sol2X = solve(n, W, p, w, branching_idx+1, best_sol, best_X, exclude, ni)

    return sol2, sol2X
        

W = 26
profit = [24,13 ,23,15,16]
weight = [ 12,7,11,8,9]
n = len(profit)

print(solve(n, W, profit, weight, 0))