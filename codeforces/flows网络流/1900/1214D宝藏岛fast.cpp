#include <bits/stdc++.h>
using namespace std;

const   int N=1e6;
typedef int mt[N];
mt I,J,C; //I,J for two directions, C for count
int m,n;

int solve(){
  int mstp=n+m-3;
  int last=n*m-2;
  int min=2;
  for(int i=1;i<=mstp;++i)   C[i]=0;
  for(int i=1;i<=last;++i)   I[i] = I[i] && ((i>=m       && I[i-m]) || (i%m>0   && I[i-1]));
  for(int i=last;i>=1;--i)   J[i] = J[i] && ((i<=m*n-1-m && J[i+m]) || (i%m<m-1 && J[i+1]));
  for(int i=1;i<=last;++i)   C[(i/m)+(i%m)] += I[i]&&J[i];
  for(int i=1;i<=mstp;++i)   if(C[i]<min) min=C[i];
  return min;
}

int main() {
  int i,j,k;
  cin >> n >> m; getchar();
  for(i=0,k=0;i<n;++i,getchar()) for(j=0;j<m;++j,++k) J[k]=I[k]=(getchar()=='.');
  cout << solve() << '\n';
}
