#include <bits/stdc++.h>
using namespace std;

const int N=1e6;
typedef bool mt[N];
mt I; //true=okay,false=NOT-PASSABLE
int m,n;

int solve(){
  int cur,p;  //#passable in each diagoal!
  int last=n*m-2;
  int min =2;
  for(int i=1;i<=n+m-3;i++){
    cur = 0;
    p = i<m ? i:(i-m+1)*m+(m-1);
    while(true){
      I[p] = I[p] && ((p>=m && I[p-m]) || (p%m>0 && I[p-1])); //self-passable and passable from up or left!
      if(I[p]) cur++;
      cout << p%m << ' ' << p/m << '\n';
      if(p%m==0) break;
      p   += (m-1);
      if(p>last) break;
    }
    cout << "cur:" << cur << '\n';
    if(cur==0)  return 0;
    if(cur<min) min=cur;
  }
  return min;
}

int main() {
  int k = 0;
  cin >> n >> m; getchar();
  for(int i=1;i<=n;i++){
    for(int j=1;j<=m;j++) I[k++]=(getchar()=='.');
    getchar();
  }
  cout << solve() << '\n';
}
