#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 200005; vector<int> e[N]; bool match[N]; int sta[N],top;
int w[N];
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
  int   n,m,l,old,ll,nu,ans;
  vector<int> caps;
  bool  same;
  cin >> n >> m;
  for(int i=0;i<N;++i) e[i].clear();
  ll = 0;
  for(int i=0;i<n;++i){ //let ^0 be small, and ^1 be CAP
    same = true;
    cin >> l;
    for(int j=0;j<l;++j){
      old=w[j]; cin>>nu; w[j]=nu;
      if(!i||!same) continue;         //no compare in 1st and no more compare if different
      if(j>=ll){same=false; continue;}//if new is longer. no more compare
      if(nu==old) continue; //same, continue next!
      same = false;
      if(nu>old) e[nu<<1^1].push_back(old<<1^1);
      else{ //nu<old
        e[0].push_back(nu <<1);   //true to new
        e[0].push_back(old<<1^1); //true to OLD
        e[nu <<1^1].push_back(1); //NEW  to false
        e[old<<1  ].push_back(1); //old  to false
      }
    }
    if(same&&(ll>l))  return false; //if old is longer. IMPOSSIBLE to FIX!
    ll = l;
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
  if(match[1]) return false;  //nesssary!
  cout << "Yes\n";
  for(int i=1;i<=m;++i) if(match[i<<1^1]) caps.push_back(i);
  ans = caps.size();
  cout << ans << endl;
  for(int i=0;i<ans;++i) cout << caps[i] << (i+1==ans?'\n':' ');
  return true;
}
 
int main(){
  int tc; tc=1; //scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"No\n";
}

