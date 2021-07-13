#include <bits/stdc++.h>
#include <stdio.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
char  S[1000003];
char  T[1000003]; int tsize;
int   L[1000003];

//P=S[0....b-1] + '$' + T[t-b..t-1]
//  P[0....b-1]  P[b]   P[b+1...2b]
//  L[1..                        n]
int maxBorder(){
  int b,n,i,j,toff;
  b = min(tsize,(int)strlen(S));
  n = (b<<1)+1;
  i = 0;
  j = L[0]=-1;
  toff = tsize-n;
  while(i<n){
    if(i==b){L[++i]=j=0; continue;} //can't miss j!
    while(j!=-1 && (i<b?S[i]:T[i+toff])!=(j<b?S[j]:T[j+toff])) j=L[j];
    L[++i]=++j;
  }
  return L[n];
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
