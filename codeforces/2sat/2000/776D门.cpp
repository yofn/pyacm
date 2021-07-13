#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 200005; vector<int> e[N]; bool match[N]; bool door[N/2]; int sta[N],top; int d2s[N];
#define bug(x) cout<<#x<<" is "<<x<<endl
 
bool dfs(int x){
  if(match[x])    return true;
  if(match[x^1])  return false;
  sta[top++]=x;
  match[x]=true;
  for(auto &y:e[x]) if(!dfs(y)) return false;
  return true;
}
 
bool solve(){
  int n,m,nd,d,dd,ii,jj,x0,x1;
  cin >> n >> m;
  for(int i=0;i<n;++i) cin >> door[i];
  memset(  d2s,0,sizeof(  d2s));
  memset(match,0,sizeof(match));
  for(int i=0;i<m;++i){
    cin >> nd;
    for(int j=0;j<nd;++j){
      cin >> d; dd = (d-1)<<1;
      d2s[dd^(d2s[dd]?1:0)]=(i+1); //if dd is occupied, use dd^1
    }
  }
  for(int i=0;i<n;++i){ //switch is 1-indexed
    ii=(d2s[(i<<1)  ]-1)<<1;
    jj=(d2s[(i<<1)^1]-1)<<1;
    x0=door[i]?0:1;
    x1=door[i]?1:0;
    e[ii].push_back(jj^x0); e[ii^1].push_back(jj^x1);
    e[jj].push_back(ii^x0); e[jj^1].push_back(ii^x1);
  }
  //dfs solve 2-sat
  for(int i=0;i<2*m;i+=2) if(!match[i] && !match[i^1]){
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  cout << "YES\n";
  return true;
}
 
int main(){
  int tc; tc=1; //scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"NO\n";
}

