#include<bits/stdc++.h>
using namespace std;
#define N 4
 
//  Encontrando a proxima soma
int maxPathSum(int triangle[][N], int m, int n)
{
     // loop para calcular o  bottom-up 
     for (int i=m-1; i>=0; i--)
     {
        for (int j=0; j<=i; j++)
        {
            /*Para cada elemento, vai analisar todos 
             os elementos logo abaixo e o abaixo a direita*/
            if (triangle[i+1][j] > triangle[i+1][j+1])
                triangle[i][j] += triangle[i+1][j];
            else
                triangle[i][j] += triangle[i+1][j+1];
        }
     }
 
     // Retorna o elemento ao topo que tem a maior soma
     return triangle[0][0];
}
int main()
{
   int triangle[N][N] = {  {2, 0, 0, 0},
                      {5, 4, 0, 0},
                      {3, 4, 7, 0}, 
                      {1, 6, 9, 6}};

   cout << maxPathSum(triangle, 2,4);
   return 0;
}