#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N=100;
const ll  q=1e9+7;
typedef ll mt[N][N];
typedef ll vt[N];
int n;
mt  A,B;
vt  al; //a1-an

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

int count_one_bits(ll v){int count=0; while(v){ v &= (v-1); count++; } return count;}

int main() {
  ll  exp;
  ll  value;
  int count;
  cin >> n >> exp; //cout << e << '\t' << n << '\t' << k << '\n';
  init(A,0);
  for(int i=0;i<n;++i) cin>>al[i];
  for(int i=0;i<n;++i){
    for(int j=i+1;j<n;++j){
      count = count_one_bits(al[i]^al[j]);
      if(count>0 && count%3==0) A[i][j]=A[j][i]=1;
    }
  }
  repr(A);
  diag(B);
  binpow(A,exp-1,B);
  repr(B);
  cout << msum(B) << '\n';
}
