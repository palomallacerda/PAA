/* Apenas um algoritimo */

subsequence_max_sum(A[1 … n]){
    //Criando arrays G e K com n tamanho
    G[0] = A[0]
    K[0] = 0
    for(i = 1 to n-1){
        // sabemos que G[i] = max{G[i-1] + A[i], A[i]}
        if (G[i-1] > 0)
            G[i] = G[i-1] + A[i]
            K[i] = K[i-1]
        else
            G[i] = A[i]
            K[i] = i
    }
    return G
}