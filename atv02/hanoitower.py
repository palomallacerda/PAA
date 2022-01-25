def hanoi(n, r, memo={}):    
    if n == 1:               # caso base
        return 1
    if r <= 2:               #casos impossíveis
        return float("inf")
    if (n,r) not in memo:
        memo[n, r] = min(hanoi(k, r)*2 + hanoi(n-k, r-1)   # Chamada recursiva 
                         for k in range(1, n))
    return memo[n, r]

