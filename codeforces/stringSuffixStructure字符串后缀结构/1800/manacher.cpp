#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
#define N 110005
char a[N],s[N*2];
int  p[N*2],ans,cnt=0,n;
void rebuild(){
  s[0]='$';s[1]='#';
  n=strlen(a);
  for(int i=0;i<n;++i)
    s[2*i+2]=a[i],s[2*i+3]='#';
  s[n=n*2+2]=0;
}
int Manacher(){
  int mx=0,id,i;
  int ans=1;
  for(i=0;i<n;++i){
    p[i]=(mx<=i)?1:min(p[2*id−i],mx−i);
    while(s[i−p[i]]==s[i+p[i]])p[i]++;
    if(p[i]+i>mx)mx=p[i]+i,id=i;
    ans=max(ans,p[i]−1);
  }
  return ans;
}
int main(){
  int t;
  cout << t;
  while(scanf("%s",a)!=EOF){
    rebuild();
    printf("%d\n",Manacher());
  }
}
