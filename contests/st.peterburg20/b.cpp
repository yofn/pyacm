//cout << a[i].first << ':' << a[i].second << '\n';

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6;
typedef unsigned long long ll;
pair<ll,int> a[MAXN];

ll solve(){
  ll  i,j,n,s,L,x,cl;
  scanf("%lld%lld",&n,&L);
  for(i=j=0;i<n;i++){
    scanf("%lld",&x);
    a[j++]   = make_pair(  (x<<1),+1);
    a[j++]   = make_pair(L+(x<<1),-1);
    if((x<<1)<=L) a[j++] = make_pair((L+x)<<1,+1);
  }
  sort(a,a+j);
  for(cl=0,i=0,s=0; i<j; i++){
    cl  += a[i].second;
    if(a[i].second==-1) s += cl*(cl-1)/2;
  }
  return (n*(n-1)/2)*(n-2)/3 - s;
}

int main(){
  printf("%lld\n",solve());
}
