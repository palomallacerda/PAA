#include <stdio.h>

void asterisco(int n, int k){
    if(n>0){ 
        asterisco(n-1, k);
        for (int i = 1; i <= n; i++)
        {
            k++;
            printf("* ");
        }
        printf("\n");
        asterisco(n-1, k);
    }
}

int main(){
    int n;
    asterisco(3, 0);
    return 0;
}