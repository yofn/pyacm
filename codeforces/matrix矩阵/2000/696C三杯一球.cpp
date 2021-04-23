#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N=2;
typedef ll mt[N][N];
int n=2;
mt  S,B;  //s for SMALL, b for BIG
const ll  q=1e9+7;

void init(mt a,int v){for(int i=0;i<n;i++) for(int j=0;j<n;j++) a[i][j]=v;}
void diag(mt a){init(a,0); for(int i=0;i<n;i++) a[i][i]=1;}
void copy(const mt a,mt b){for(int i=0;i<n;i++) for(int j=0;j<n;j++) b[i][j]=a[i][j];}
void mult(const mt a,const mt b,mt c){
  init(c,0); for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) c[i][j] = (c[i][j]+a[i][k]*b[k][j])%q;
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
  ll  p,q,a;
  int k;
  cin >> k;
  //make S
  init(S,0); S[0][1]=S[1][1]=1; S[1][0]=2;
  diag(R);
  for(int i=0;i<k;++i){
    cin >> a;
    binpow(S,a,R);
    p = S[1][1];
  }
  if(exp==1){
    cout << state[k] << '\n';
    return 0;
  }
  diag(B);
  binpow(A,exp-1,B);
  ans=0;
  //repr(B,n);
  for(int i=0;i<n;++i) ans=(ans+B[k][i]*state[i])%q;
  cout << ans << '\n';
}
