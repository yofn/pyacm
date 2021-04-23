#include <bits/stdc++.h>
using namespace std;

const int N=1e6;
typedef int mt[N];
mt I; //true=okay,false=NOT-PASSABLE
mt J; //order..topological order
int m,n;

int solve(){
  int cur,p;  //#passable in each diagoal!
  int last=n*m-2;
  int min =2;
  for(int i=1;i<=n+m-3;++i){
    p = i<m ? i:(i-m+1)*m+(m-1);
    while(true){
      I[p] = I[p] && ((p>=m && I[p-m]) || (p%m>0 && I[p-1])); //self-passable and passable from up or left!
      if(p%m==0) break;
      p   += (m-1);
      if(p>last) break;
    }
  }
  for(int i=n+m-3;i>=1;--i){
    p = i<n ? i*m:(i-n+1)+(n-1)*m;
    while(true){
      J[p] = J[p] && ((p<m*(n-1) && J[p+m]) || (p%m<m-1 && J[p+1])); //self-passable and passable from down or right!
      if(p%m==m-1) break;
      p   -= (m-1);
      if(p<1) break;
    }
  }
  for(int i=1;i<=n+m-3;i++){
    cur = 0;
    p = i<m ? i:(i-m+1)*m+(m-1);
    while(true){
      if(I[p]&&J[p]) cur++;
      if(p%m==0) break;
      p   += (m-1);
      if(p>last) break;
    }
    if(cur==0)  return 0;
    if(cur<min) min=cur;
  }
  return min;
}

int main() {
  int k = 0;
  cin >> n >> m; getchar();
  for(int i=1;i<=n;i++){
    for(int j=1;j<=m;j++){
      J[k]=I[k]=(getchar()=='.');
      ++k;
    }
    getchar();
  }
  cout << solve() << '\n';
}
