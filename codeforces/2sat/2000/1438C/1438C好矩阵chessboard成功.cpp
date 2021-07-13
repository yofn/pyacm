#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N=10000; ll mt[N];
#define bug(x) cout<<#x<<" is "<<x<<endl

bool solve(){
  int n,m,nm,k;
  ll  x,x0,x1;
  cin >> n >> m; nm=n*m;
  for(int i=0;i<nm;++i) scanf("%lld",mt+i);
  k = 0;
  for(int i=0;i<n;++i) for(int j=0;j<m;++j){
    x  = mt[k++];
    x1 = x|1;
    x0 = x1==x?x+1:x;
    cout << (i%2==j%2?x0:x1) << (j<m-1?' ':'\n');
  }
  return true;
}

int main(){
  int tc;
  cin >> tc;
  while(tc--) if(!solve()) cout<<"NO\n";
}
