#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N=52;
const ll  q=1e9+7;
typedef ll mt[N][N];
int n;
mt A,B;

void init(mt a,int v){for(int i=0;i<n;i++) for(int j=0;j<n;j++) a[i][j]=v;}
void diag(mt a){init(a,0); for(int i=0;i<n;i++) a[i][i]=1;}
void copy(const mt a,mt b){for(int i=0;i<n;i++) for(int j=0;j<n;j++) b[i][j]=a[i][j];}
void mult(const mt a,const mt b,mt c){
  init(c,0);
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
      for(int k=0;k<n;k++)
        c[i][j] = (c[i][j]+a[i][k]*b[k][j])%q;
}
ll   msum(const mt a){
  ll s=0; 
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
      s = (s+a[i][j])%q; 
  return s;
}
void repr(const mt a){
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++) 
      cout << a[i][j] << '\t';
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

int c2i(const char c){return c>='a'?c-'a':c-'A'+26;}

int main() {
  int  k;
  ll   e;
  char s[2];
  cin >> e >> n >> k; //cout << e << '\t' << n << '\t' << k << '\n';
  init(A,1);
  for(int i=1;i<=k;i++){
    cin >> s[0] >> s[1];
    A[c2i(s[0])][c2i(s[1])]=0;
  }
  //repr(A);
  diag(B);
  binpow(A,e-1,B);
  //repr(B);
  cout << msum(B) << '\n';
}
