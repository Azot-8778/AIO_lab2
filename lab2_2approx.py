import numpy as np

def solve(n, W, p, w):
    c_greed = 0
    w_greed = 0
    X_greed = set()
    q = np.array(p) / np.array(w)
    idx_q_sorted = np.argsort(q)[::-1]
    for idx in idx_q_sorted:
        if w_greed + w[idx] > W:
            break
        w_greed += w[idx]
        c_greed += p[idx]
        X_greed.add(idx)
    
    c_maxgreed = 0
    w_maxgreed = 0
    X_maxgreed = set()
    idx_p_sorted = np.argsort(p)[::-1]
    for idx in idx_p_sorted:
        if w_maxgreed + w[idx] > W:
            break
        w_maxgreed += w[idx]
        c_maxgreed += p[idx]
        X_maxgreed.add(idx)
    
    if c_maxgreed >= c_greed:
        return c_maxgreed, X_maxgreed
    else:
        return c_greed, X_greed

profit = [442,525,511,593,546,564,617]
weight = [41,50,49,59,55,57,60]
W = 170
n = len(profit)

cost, items = solve(n, W, profit, weight)
print(cost)
print(items)