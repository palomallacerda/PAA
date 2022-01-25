topological_sort(v, checked[], pilha){
    checked[v] = true;
    for (i = 1 to adj_list(v).size()) {
        node = adj_list(v).get(i);
        if (!checked[node])
            topological_sort(node, checked, pilha);
    }
    pilha.push(v);
}

longest_path(G(V, E)){
    pilha = inicializar_pilha // pilha vazia
    dist[V]
    checked[V]
    for (i = 1 to |V|) {
    checked[i] = false
    dist[i] = -∞
    }
    for (i = 1 to |V|) {
        if (checked[i] == false)
            topologicalSortUtil(i, checked, pilha)
    }
    dist[s] = 0;
    while (pilha.is_not_empty()) {
        int u = pilha.pop();
        if (dist[u] != -∞) {
        for (i = 1 to adj_list(u).size()) {
            //vértice da lista de adjacências do vértice u, na posição i
            node = adj_list(u).get(i); 
            if (dist[node] < dist[u] + node.weight())
                dist[node] = dist[u] + node.weight();
            }
        }
    }
    return dist;
}