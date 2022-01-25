 
# Function to traverse the DAG
# and apply Dynamic Programming
# to find the longest path
def dfs(node, adj, dp, vis):
  
    # Marcar como visitado
    vis[node] = True
   
    for i in range(0, len(adj[node])): 
   
        # se nao foi visitado
        if not vis[adj[node][i]]:
            dfs(adj[node][i], adj, dp, vis)
   
        # Guarda o caminho max
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])
   
#add um edge
def addEdge(adj, u, v):
    adj[u].append(v)
   
# Funcao que encontra e retorna o caminho max
def findLongestPath(adj, n): 
    # Dp array
    dp = [0] * (n + 1)
    # array visitado para saber 
    # se o nó foi visitado antes ou nao
    vis = [False] * (n + 1)
     
    # Chama dfs para cada vertice nao visitado
    for i in range(1, n + 1): 
        if not vis[i]:
            dfs(i, adj, dp, vis)
      
    ans = 0
   
    for i in range(1, n + 1): 
        ans = max(ans, dp[i])
      
    return ans
  
if __name__ == "__main__":
  
    n = 5
    adj = [[] for i in range(n + 1)]
   
    # Exemplo
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 3, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 3, 4)
   
    print(findLongestPath(adj, n))
