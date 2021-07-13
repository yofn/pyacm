#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N = 20003; vector<int> e[N]; bool match[N]; ll mt[N]; int sta[N<<4],top;
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
  int n,m,nm,ii,jj;
  ll  x,y;
  scanf("%d",&n); scanf("%d",&m); nm=n*m;
  for(int i=0;i<N; ++i) e[i].clear();
  memset(match,false,sizeof(match));
  memset(mt,       0,sizeof(mt));
  for(int i=0;i<nm;++i) scanf("%lld",mt+i);
  for(int i=0;i<nm;++i){
    x=mt[i]; ii=i<<1;
    if(i%m>0){  //%m is important
      y  = mt[i-1];
      jj = (i-1)<<1;
      if     (y==x+1) e[ii^1].push_back(jj^1);
      else if(x==y+1) e[jj^1].push_back(ii^1); 
      else if(y==x)  {e[jj].push_back(ii^1);e[jj^1].push_back(ii);e[ii].push_back(jj^1);e[ii^1].push_back(jj);}
    }
    if(i>=m){
      y  = mt[i-m];
      jj = (i-m)<<1;
      if     (y==x+1) e[ii^1].push_back(jj^1);
      else if(x==y+1) e[jj^1].push_back(ii^1);
      else if(y==x)  {e[jj].push_back(ii^1);e[jj^1].push_back(ii);e[ii].push_back(jj^1);e[ii^1].push_back(jj);}
    }
  }
  //dfs solve 2-sat
  for(int i=0;i<2*nm;i+=2) if(!match[i] && !match[i^1]){
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  for(int i=0;i<nm;++i) if(match[(i<<1)^1]) mt[i]++;
  for(int i=0;i<n;++i) for(int j=0;j<m;++j) cout << mt[i*m+j] << (j<m-1?' ':'\n');
  return true;
}

int main(){
  int tc;
  cin >> tc;
  while(tc--) if(!solve()) cout<<"NO\n";
}
