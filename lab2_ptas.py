from itertools import combinations

def calc_weight(w, M):
    m_sum = 0
    for j in M:
        m_sum += w[j]

    return m_sum

def calc_profit(p, M):
    p_sum = 0
    for j in M:
        p_sum += p[j]
        
    return p_sum
    
def GS(n, c, p, w, M):
    zg = 0
        
    c_hat = c - calc_weight(w, M)
    X = set()
    
    for j in range(n):
        if j not in M and w[j] <= c_hat:
            zg += p[j]
            c_hat = c_hat - w[j]
            X.add(j)
            
    return zg, X

def ptas(k, n, c, p, w):
    zh = 0
    Xh = set()
    
    for subset_len in range(1, k+1):
        for M in combinations(set(range(n)), subset_len):
            if calc_weight(w, M) > c:
                continue
            
            zg, X = GS(n, c, p, w, M)
            if zg + calc_profit(p, M) > zh:
                zh = zg + calc_profit(p, M)
                Xh = X.union(set(M))
    return zh, Xh

profit = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
weight = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
W = 165
n = len(profit)

cost, items = ptas(3, n, W, profit, weight)
print(cost)
print(items)