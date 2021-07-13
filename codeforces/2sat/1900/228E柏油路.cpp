#include <bits/stdc++.h>
using namespace std;

const int N = 302;   vector<int> e[N]; bool match[N];
const int M = 10003; int sta[M],top;
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
  int n,m,a,b,c,t,ans;
  scanf("%d",&n); scanf("%d",&m);
  for(int i=0;i<2*n;++i) e[i].clear();
  for(int i=0;i<m;++i){
    scanf("%d",&a); scanf("%d",&b); scanf("%d",&c);
    if(a>b){t=a;a=b;b=t;}
    e[a*2-2].push_back(b*2-1-c);  //if c==1, switch both or none
    e[a*2-1].push_back(b*2-2+c);  //if c==0, switch one of them!
    e[b*2-2].push_back(a*2-1-c);  //if c==1, switch both or none
    e[b*2-1].push_back(a*2-2+c);  //if c==0, switch one of them!
  }
  memset(match,false,sizeof(match));
  for(int i=0;i<2*n;i+=2) if(!match[i] && !match[i^1]){
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  ans = 0;
  for(int i=0;i<n;++i) if(match[i<<1]) ++ans;
  cout << ans  << endl;
  for(int i=0;i<n;++i) if(match[i<<1]) cout << i+1 << (--ans>0?' ':'\n');
  return true;
}

int main(){
  if(!solve()) cout << "Impossible" << endl;
}
