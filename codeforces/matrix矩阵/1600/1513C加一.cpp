#include <bits/stdc++.h>
using namespace std;

typedef long long ll;   const ll p=1e9+7;
const int N=2e5+1;
typedef int vt[N];      vt DP;  // dp(i)=len(f^i(10))

int main() {
  ll  a;
  int T,ans,b,c;
  for(int i=0;i<=8;++i) DP[i]=2;  DP[9]=3;
  for(int i=10;i<N;++i) DP[i]=(DP[i-9]+DP[i-10])%p;

  cin >> T;
  for(int i=1;i<=T;++i){
    scanf("%lld",&a); scanf("%d",&b);
    ans = 0;
    while(a){
      c    = b-(10-a%10);  //1912
      ans  = (ans+(c<0?1:DP[c]))%p;
      a   /=10;
    }
    printf("%d\n",ans);
  }
}
