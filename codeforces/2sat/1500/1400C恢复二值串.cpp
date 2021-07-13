#include <bits/stdc++.h>
using namespace std;

const int N = 100004;
char S[N];
char W[N];

void solve(){
  int n,x,p,q;
  scanf("%s", S); n=strlen(S);
  scanf("%d",&x);
  for(int i=0;i<n;++i) W[i]='1'; W[n]=0;
  for(int i=0,p=-x,q=x;i<n;++i,++p,++q)if(S[i]=='0'){if(p>=0)W[p]='0'; if(q<n)W[q]='0';}
  for(int i=0,p=-x,q=x;i<n;++i,++p,++q)if(S[i]=='1'){
    if(p>=0 && W[p]=='1') continue;
    if(q< n && W[q]=='1') continue;
    cout << -1 << endl;
    return;
  }
  cout << W << endl; //printf("%s\n",W);
}

int main(){
  int Case;
  cin >> Case;
  while(Case--) solve();
}
