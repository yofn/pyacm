#include <bits/stdc++.h>
using namespace std;

typedef long long ll;   const ll p=1e9+7;
const int N=16;         int n=10;
typedef int mt[N][N];   mt S,B; //s for SMALL, b for BIG
typedef int vt[N];      vt ST;  //state

void init(mt a,int v){for(int i=0;i<n;i++) for(int j=0;j<n;j++) a[i][j]=v;}
void diag(mt a){init(a,0); for(int i=0;i<n;i++) a[i][i]=1;}
void copy(const mt a,mt b){for(int i=0;i<n;i++) for(int j=0;j<n;j++) b[i][j]=a[i][j];}
void mult(const mt a,const mt b,mt c){
  init(c,0); for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) c[i][j]=(c[i][j]+(ll)a[i][k]*b[k][j])%p;
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
  ll  a;
  int T,ans,b;
  init(S,0);   S[0][9]=1; S[1][9]=1;
  for(int i=0;i<=8;++i) S[i+1][i]=1;

  cin >> T;
  for(int i=1;i<=T;++i){
    scanf("%lld",&a); scanf("%d",&b);
    for(int j=0;j<=9;j++) ST[j]=0;
    while(a){ST[a%10]++; a/=10;}
    diag(B); ans=0;
    binpow(S,b,B);
    //repr(B,10);
    for(int j=0;j<10;j++) for(int k=0;k<10;k++) ans=(ans+B[j][k]*ll(ST[k]))%p;
    printf("%d\n",ans);
  }
}
