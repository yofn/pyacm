#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 400005; vector<int> e[N]; bool match[N]; int sta[N],top;
int p[N]; //position of x
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
  int  n,nn,x,xx,j1,j2,n1,n2,ans;
  vector<int> swaps;
  bool b;
  cin >> n; nn=n<<1;
  for(int i=0;i<N;  ++i)  e[i].clear();
  memset(p,0,sizeof(p));
  b = true;
  for(int i=1;i<=nn;++i){
    cin>>x;xx=(x-1)<<1; //1-n =>0-(n-1)
    if(p[xx^1]) b=false;
    p[p[xx]?xx^1:xx]=i; //1-index, or WA!
  }
  if(!b) return false;
  for(int xx=0;xx<nn;xx+=2){ //xx refs2 value*2
    j1=p[xx]-1;   n1=(j1%n)<<1;
    j2=p[xx^1]-1; n2=(j2%n)<<1;
    if((j1<n)^(j2<n)){  //parallel
      e[n1].push_back(n2); e[n1^1].push_back(n2^1);
      e[n2].push_back(n1); e[n2^1].push_back(n1^1);
    }else{  //cross
      e[n1].push_back(n2^1); e[n1^1].push_back(n2);
      e[n2].push_back(n1^1); e[n2^1].push_back(n1);
    }
  }
  //dfs solve 2-sat
  memset(match,false,sizeof(match));
  for(int i=0;i<nn;i+=2) if(!match[i] && !match[i^1]){ //<=!
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  ans = 0;
  for(int i=0;i<nn;i+=2) if(match[i]) ans++;
  b   = ans*2>n;  //WA if ans>n/2
  ans = b?n-ans:ans;
  for(int i=0;i<n;++i) if(b^match[i<<1]) swaps.push_back(i+1);
  cout << ans << endl;
  for(int i=0;i<ans;++i) cout << swaps[i] << (i==ans-1?"":" ");
  cout << endl;
  return true;
}
 
int main(){
  int tc; scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"-1\n";
}

