#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 200005; vector<int> e[N]; bool match[N]; int sta[N],top;
int p[N];
#define bug(x) cout<<#x<<" is "<<x<<endl
//cout<< i/2 << '+' << it->second/2 << ':' << p[i/2] << '+' << p[it->second/2] << '=' << (i%2==0?a:b) << (i%5==0?'\n':' ');
 
bool dfs(int x){
  if(match[x])    return true;
  if(match[x^1])  return false;
  sta[top++]=x;
  match[x]=true;
  for(auto &y:e[x]) if(!dfs(y)) return false;
  return true;
}
 
bool solve(){
  int n,a,b,ii,jj;
  unordered_map<int,int> um;
  cin >> n >> a >> b;
  for(int i=0;i<N; ++i) e[i].clear();
  for(int i=1;i<=n;++i){cin>>p[i]; um[p[i]]=i<<1;}
  for(int i=1;i<=n;++i){
    ii = i<<1;
    auto ac = um.find(a-p[i]);
    auto bc = um.find(b-p[i]);
    if(ac==um.end()){ e[ii  ].push_back(1); }
    else            { jj = ac->second; e[ii].push_back(jj); e[ii^1].push_back(jj^1);}
    if(bc==um.end()){ e[ii^1].push_back(1); }
    else            { jj = bc->second; e[ii].push_back(jj); e[ii^1].push_back(jj^1);}
  }
  //dfs solve 2-sat
  memset(match,false,sizeof(match));
  for(int i=0;i<(n+1)*2;i+=2) if(!match[i] && !match[i^1]){ //<=!
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  //if(match[1]) return false; not necessary?
  cout << "YES\n";
  for(int i=1;i<=n;++i) cout << int(!match[i<<1]) << (i==n?'\n':' ');
  return true;
}
 
int main(){
  int tc; tc=1; //scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"NO\n";
}

