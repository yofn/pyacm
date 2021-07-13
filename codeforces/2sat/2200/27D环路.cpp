#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 202; vector<int> e[N]; bool match[N]; int sta[N],top;
int c[N]; //city
#define bug(x) cout<<#x<<" is "<<x<<endl
 
bool dfs(int x){
  if(match[x])    return true;
  if(match[x^1])  return false;
  sta[top++]=x;
  match[x]=true;
  for(auto &y:e[x]) if(!dfs(y)) return false;
  return true;
}

bool cross(int s0,int t0,int s1,int t1){return (s0-s1)*(s0-t1)*(t0-s1)*(t0-t1)<0;}
 
bool solve(){
  int n,m;
  cin >> n >> m;
  for(int i=0;i<N;  ++i)  e[i].clear();
  for(int i=0;i<m*2;++i)  cin>>c[i];
  for(int i=0;i<m*2;i+=2) for(int j=i+2;j<m*2;j+=2) if(cross(c[i],c[i^1],c[j],c[j^1])){
    e[i].push_back(j^1); e[i^1].push_back(j);
    e[j].push_back(i^1); e[j^1].push_back(i);
  }
  //dfs solve 2-sat
  memset(match,false,sizeof(match));
  for(int i=0;i<m*2;i+=2) if(!match[i] && !match[i^1]){ //<=!
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  for(int i=0;i<m*2;i+=2) cout << (match[i]?'i':'o');
  cout << endl;
  return true;
}
 
int main(){
  int tc; tc=1; //scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"Impossible\n";
}

