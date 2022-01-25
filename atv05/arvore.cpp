initialize(T(V,E)) {
    raiz = get_root(T)
    
    sem_raiz, contem_raiz = vertex_cover(raiz)
    return sem_raiz + contem_raiz
}

vertex_cover(raiz) {
    if (raiz == null || raiz.degree == 0)
    return 0, 0
    for each raiz.child c
        best[c][0], best[c][1] = vertex_cover(c)
    
    sem_raiz = sum over all c of best[c][1]
    contem_raiz = 1 + sum over all c of min(best[c][0], best[c][1])
    
    return (sem_raiz, contem_raiz)
}