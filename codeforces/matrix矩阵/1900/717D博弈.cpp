#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef double dl;
const int N=128;
typedef dl mt[N][N];
typedef dl vt[N];
int n;
mt  A,B;
vt  al;

void init(mt a,int v){for(int i=0;i<n;i++) for(int j=0;j<n;j++) a[i][j]=v;}
void diag(mt a){init(a,0); for(int i=0;i<n;i++) a[i][i]=1;}
void copy(const mt a,mt b){for(int i=0;i<n;i++) for(int j=0;j<n;j++) b[i][j]=a[i][j];}
void mult(const mt a,const mt b,mt c){
  init(c,0); for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) c[i][j] += a[i][k]*b[k][j];
}

void repr(const mt a,int n){
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++) 
      cout << a[i][j] << ' ';
    cout << '\n';
  }
}

mt t,r;
void binpow(const mt a,ll b,mt c){
  copy(a,t);
  while(b){
    if(b&1){ mult(c,t,r); copy(r,c);}
    mult(t,t,r); copy(r,t);
    b>>=1;
  }
}

int main() {
  ll  exp;
  int x,k;
  dl  p=0;
  cin >> exp >> x;
  n = N;
  for(int i=0;i<=x;++i) cin>>al[i];
  init(A,0);
  for(int i=0;i<n;++i)
    for(int j=0;j<=x;++j)
      A[i^j][i] += al[j];
  diag(B);
  binpow(A,exp-1,B);
  for(int i=0;i<=x;++i) p+=al[i]*B[0][i];
  cout << 1-p << '\n';
}
