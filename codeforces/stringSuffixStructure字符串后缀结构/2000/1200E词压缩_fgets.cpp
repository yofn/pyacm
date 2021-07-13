#include <bits/stdc++.h>
#include <stdio.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
char  S[1000003];
int   Z[1000003];

int maxBorder(int h,int m,int t){
  int b,n,r,l,bl,gl,j,rj,rkj;
  b =(m-h-1);   //P=S[h+1..m-1] + '$' + [t-b..t-1]
  n =(b<<1)+1;  //  P[0....b-1]  P[b]  P[b+1...2b]
  Z[0]  = n;    //  Z[0.. ..                     ]
  r     = 0;
  while(r+1<b && S[h+1+r]==S[h+2+r]) r++;
  Z[1]  = r;
  l     = r>0;
  for(int k=2;k<n;++k){
    bl = r+1-k;   //|beta|,aka.k2l
    gl = Z[k-l];  //|gamma|
    if(gl<bl){
      Z[k]=Z[k-l];
    }else{
      j   = max(0,r-k+1);
      rj  = h+1+j;
      rkj = k<b ? (rj+k):(t-n+k);
      if(k<b){
        while(k+j<n && S[rj++]==S[rkj++]) j++;
        Z[k]=j;
        l   =k;
        r   =k+j-1;
      }
    }
    if(Z[k]+k==n){
      return Z[k];
    }
  }
  return 0;
}

//  aaaaBBB xxxx AAA CCC
//         t    h   m   //t=tail,h=head;m=middle
int main(){
  int n,h,m,t;
  scanf("%d",&n); getchar(); fgets(S,1e6,stdin);
  for(h=0;S[h] && S[h]!=' ';++h) ;
  if(S[h]){
    t=m=h;
    do{
      ++m;
      if(S[m]==' '||!S[m]){
        h += maxBorder(h,m,t);
        while(h<m) S[t++]=S[h++];
        bug(S);
      }
    }while(S[m]);
    S[t]=0;
  }
  printf("%s\n",S);
}
