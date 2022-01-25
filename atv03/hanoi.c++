// Número de aneis, torre de origem, torre de destino,
// 1ª torre auxiliar, 2º torre auxiliar.
void hanoi(int rings, int from, int to, int aux1, int aux2){
    if(rings==0)
        return;
    if(rings==1){
        cout<<from<<" to "<<to<<endl;ct++;
        return;
    }
    hanoi(rings-2, from, aux2, aux1, to);
    cout<<from<<" to "<<aux1<<endl;
    cout<<from<<" to "<<to<<endl;
    cout<<aux1<<" to "<<to<<endl;
    ct+=3;
    hanoi(rings-2,aux2, to, from, aux1);
}

int main(){
    int i,n,j,k,l,m;
    cin>>n;
    hanoi(n,0,1,2,3);
    cout<<ct<<endl;
}