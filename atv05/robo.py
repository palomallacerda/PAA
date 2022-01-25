import numpy as np
#Função para encontrar o máximo de moedas
def MaxCoin(r,c,CoinMatrix):
    #2d matriz com rows=r+1 e columns=c+1 
    MaxCoin=[[0]*(r+1) for _ in range(c+1)]
 
    for i in range(1,r+1):
        for j in range(1,c+1):
          #Encontra o numero máximo de numeros na 2d matriz e add 1 se a celula tiver uma moeda
          MaxCoin[i][j]=max(MaxCoin[i-1][j],MaxCoin[i][j-1])+CoinMatrix[i-1][j-1]
    
   
    #print o caminho
    print('Coins collected by Robot at each level are:''\n''', np.matrix(MaxCoin))
    #print maximo de moedas coletados pelo robo 
    print('Maximum Coins collected by Robot are: ',MaxCoin[r][c])
rows=3 #numero de linhas
col=3 #numero de colunas
#2d matriz exemplo contendo 3 linhas e 3 colunas
CoinMatrix=[[0]*rows for _ in range(col)]
CoinMatrix=[[1,0,1],
           [1,0,1],
           [1,1,1]]
MaxCoin(rows,col,CoinMatrix)