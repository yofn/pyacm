#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N=100;
typedef ll mt[N][N];
typedef ll vt[N];
int n;
mt  A,B;
vt  state;
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
  ll  exp,ans;
  int x,k,m,v;
  //n,b,k,x; #digits in one block, #blocks, interesting remainder modulo x and modulo x itself.
  cin >> m >> exp >> k >> n; //n = matrix-size = x
  init(A,0);
  for(int i=0;i<n;++i) state[i]=0;
  for(int i=0;i<m;++i){
    cin >> v;
    state[v%n]++;
    for(int j=0;j<n;++j){
      //A[(v*10+j)%n][j]++; MUST NOT!
      A[(v+j*10)%n][j]++;
    }
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
