#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 8004; vector<int> e[N]; bool match[N]; int sta[N],top;
const int M = 4000006; char S[M]; char T[M];
char v[N];
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
  int  n,nn,x,i,j,ans,ni,nj,n1;
  vector<int> flips;
  cin >> n; nn=n*n;
  for(int i=0;i<N;++i) e[i].clear();
  for(int i=0;i<n;++i) scanf("%s",S+i*n);
  for(int i=0;i<n;++i) scanf("%s",T+i*n);
  scanf("%s",v);
  for(int i=0;i<n; ++i) v[i] -= '0';
  for(int k=0;k<nn;++k){
    i=k/n; j=k%n;
    ni=(1  +i)<<1;  //row-i node: no-yes
    nj=(1+n+j)<<1;  //col-j node: no-yes
    //cout << i << ':' << j << ':' << ni << ':' << nj << endl;
    if(S[k]!=T[k]){
      if(!v[i]&&!v[j]) return false;  //imposible if both 0;
      //cout << 1 << "=" << i << ":" << j << endl;
      if( v[i]&& v[j]){
        e[ni].push_back(nj^1); e[ni^1].push_back(nj); //cross if m[k]=1
        e[nj].push_back(ni^1); e[nj^1].push_back(ni);
      }else{
        n1 = v[j]?ni:nj;        //NOTE:v[j] need ni to take effect!
        e[ 0].push_back(n1^1);  //must select this only 1
        e[n1].push_back(1);     //deselect the only 1 will lead to fail!
      }
    }else{
      if(!v[i]&&!v[j]) continue;        //anyway will do if both 0;
      //cout << 0 << "=" << i << ":" << j << endl;
      if( v[i]&& v[j]){
        e[ni].push_back(nj); e[ni^1].push_back(nj^1); //parallel if m[k]=0
        e[nj].push_back(ni); e[nj^1].push_back(ni^1);
      }else{
        n1 = v[j]?ni:nj;
        e[   0].push_back(n1);  //must NOT select this only 1
        e[n1^1].push_back(1);   //select the only 1 will lead to fail!
      }
    }
  }
  //dfs solve 2-sat
  memset(match,false,sizeof(match));
  for(int i=0;i<n*4+2;i+=2) if(!match[i] && !match[i^1]){ //<=!
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  if(match[1]) return false;  //nesssary!
  for(int i=1;i<=n*2;++i) if(!match[i<<1]) flips.push_back(i-1);
  ans  = flips.size();
  cout << ans << endl;
  for(int i=0;i<ans;++i) cout << (flips[i]<n?"row ":"col ")<< flips[i]%n << endl;
  return true;
}
 
int main(){
  int tc; tc=1; //scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"-1\n";
}

