#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const   ll  p=1e9+7;
const   int N=128;      int n;
typedef int  mt[N][N];  mt  S,B;
typedef int  vt[N];     vt  state;
typedef int ivt[N*2];   ivt head,midd,tail;
const   int NCNT=1e6;   int longtail[NCNT];

void init(mt a,int v){for(int i=0;i<n;i++) for(int j=0;j<n;j++) a[i][j]=v;}
void diag(mt a){init(a,0); for(int i=0;i<n;i++) a[i][i]=1;}
void copy(const mt a,mt b){for(int i=0;i<n;i++) for(int j=0;j<n;j++) b[i][j]=a[i][j];}
void mult(const mt a,const mt b,mt c){
  init(c,0); for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) c[i][j] = (c[i][j]+((ll)a[i][k]*b[k][j])%p)%p;
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
  ll  ans;
  int ncnt,L,c,i,j,t;    //cij
  // process input and init state vector
  cin >> ncnt >> L >> n;  //n = matrix-size = M
  for(i=0;i<=(n<<1);++i)  head[i]=midd[i]=tail[i]=0;
  for(i=0;i<n;++i)       state[i]=0;
  for(i=0;i<ncnt;++i){scanf("%d",&c); head[c]++;} head[0]+=head[n];
  for(i=0;i<ncnt;++i){scanf("%d",&c); midd[c]++; longtail[i]=c;} midd[0]+=midd[n];
  for(i=0;i<ncnt;++i){scanf("%d",&c); tail[longtail[i]+c]++;}    tail[n]+=tail[n<<1];
  for(i=0;i<n;i++)   tail[i] += tail[i+n]; //reduce tail[0-2n) to tail[0-n), avoid %@ncnt..
  //build transition matrix S from midd vector! AND init state!
  init(S,0);
  for(i=0;i<n;i++){for(j=0;j<n;j++){
    t        = (i+j)%n;
    state[t] = (state[t]+head[i]*(ll)tail[j])%p;
    S[t][i] += midd[j];  //state[i]*num(midd)[j] contribute to=> newstate[(i+j)%n] (+=)
  }}
  if(L==2){cout << state[0] << '\n'; return 0;}
  /*
  for(int i=0;i<n;++i){cout << head[i] << ' ';} cout << '\n';
  for(int i=0;i<n;++i){cout << midd[i] << ' ';} cout << '\n';
  for(int i=0;i<n;++i){cout << tail[i] << ' ';} cout << '\n';
  for(int i=0;i<n;++i){cout <<state[i] << ' ';} cout << '\n';
  */
  //binpow@S
  diag(B);
  //repr(S,n);
  binpow(S,L-2,B);
  ans=0;
  //repr(B,n);
  for(i=0;i<n;++i) ans=(ans+(B[0][i]*(ll)state[i])%p)%p;
  cout << ans << '\n';
}
