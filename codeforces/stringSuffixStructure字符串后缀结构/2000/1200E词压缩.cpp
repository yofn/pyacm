#include <bits/stdc++.h>
#include <stdio.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
#define N 1000005
char  T[N];
char  A[N]; //A=Ans
int   last[N];

void get_last(char *t,int len){
  int i=0,j=last[0]=-1;
  while(i<len){
    while(j!=-1&&t[i]!=t[j]) j=last[j];
    last[++i]=++j;
  }
}

int okmp(char *p,char *t){
  int i,j; i=j=0;
  while(t[i]){
    while(j!=-1 && t[i]!=p[j]) j=last[j];
    i++;j++;
  }
  return j; //overlap@kmp => p11@ML04AppliedCombinatorics@Words
}

int main(){
  int  n,alen,tlen,toff;
  scanf("%d",&n);
  scanf("%s",A);
  alen = strlen(A);
  while(--n){
    scanf("%s",T);
    tlen = strlen(T);
    get_last(T,tlen);
    toff = okmp(T,A+max(alen-tlen,0)); 
    strcpy(A+alen,T+toff);
    alen += tlen-toff;
  }
  cout << A << endl;
}
