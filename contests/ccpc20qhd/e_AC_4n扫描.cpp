#include <bits/stdc++.h>
using namespace std;
//scanning

// template to simplify INPUT (but SLOWER)
template <class T> void read(T &x){
  char ch=getchar(); int s;
  for(s=0; !isdigit(ch); ch=getchar())     s |= (ch=='-');
  for(x=0;  isdigit(ch); ch=getchar())     x  = x*10 + ch - '0';
  if(s) x=-x;
}

typedef long long ll;
const int N = 200005;
pair<int,int> sl[N<<2];
const int inf = 1e9 + 99;

int p;

int calc(int x){
  return min((ll)inf,x*100ll/p);
}

int solve(){
  int n; read(n); read(p);
  int a,b;
  int cnt=0;
  int  mb=0;
  for(int i=1;i<=n;i++){
    read(a); read(b);
    mb = max(mb,b);
    int l1 = b, r1=calc(b);
    int l2 = a, r2=calc(a);
    sl[++cnt]=make_pair(l1,  +1);
    sl[++cnt]=make_pair(r2+1,-1);
    if(l2>r1+1){
      sl[++cnt]=make_pair(r1+1, -1);
      sl[++cnt]=make_pair(l2,   +1);
    }
  }
  sort(sl+1,sl+cnt+1);  //S[1]~S[cnt]
  int ans=0;
  int now=0;
  for(int i=1;i<=cnt;i++){
    now += sl[i].second;
    if( sl[i].first!=sl[i+1].first || i==cnt){
      if(sl[i].first >= mb)
        ans = max(now,ans);
    }
  }
  return ans;
}

int main(){
  int Case; read(Case); int tc=Case;
  while(Case--) printf("Case #%d: %d\n",tc-Case,solve());
}
