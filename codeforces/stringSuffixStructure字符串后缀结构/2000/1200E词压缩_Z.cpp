#include <bits/stdc++.h>
#include <stdio.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
char  S[1000003];
char  T[1000003]; int tsize;
int   Z[1000003];

//P=S[0....b-1] + '$' + T[t-b..t-1]
//  P[0....b-1]  P[b]   P[b+1...2b]
//  Z[0..                         ]
int maxBorder(){
  int b,n,l;
  b = min(tsize,(int)strlen(S));
  n = (b<<1)+1;
  Z[0] = n;
  l    = 0;
  while(l+1<b && S[l]==S[l+1]) l++;
  Z[1] = l;
  l    = 1;
  for(int k=2;k<n;++k){
    if(k==b){Z[k]=0;l=k;continue;}
    int r = l+Z[l]-1; if(k+Z[k-l]<r+1){Z[k]=Z[k-l]; continue;}  //CASE2a: Z-box has all info!
    int j = max(0,r-k+1);
    while(k+j<n){
      if(k<b && S[j]!=S[k+j])         break;
      if(k>b && S[j]!=T[tsize-n+k+j]) break;
      j++;
    }
    if(k+j==n) return j;
    Z[k]=j;
    l=k;
  }
  return 0;
}

int main(){
  int n,mb;
  scanf("%d",&n);
  scanf("%s",S); strcpy(T,S); tsize=strlen(S);
  while(--n){
    scanf("%s",S);
    mb = maxBorder();
    strcpy(T+tsize,S+mb);
    tsize += strlen(S+mb);  //avoid strlen @ T!
  }
  printf("%s\n",T);
}
