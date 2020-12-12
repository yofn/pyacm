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
const int N = 400005;
pair<int,int> S[N];
int CS[N]; //count student;
int BM[N]; //above max count; should always <=1
 
int solve(){
  int n,p; read(n); read(p);
  int a,b;
  int ii=0;
 
  for(int i=0;i<n;i++){
    read(a); read(b);
    S[ii++]=make_pair(-a,i);
    S[ii++]=make_pair(-b,i);
    CS[i]  =0;
    BM[i]  =0;
  }
  sort(S,S+(n*2));
  //for(int i=0;i<n*2;i++) cout << S[i].first << "," << S[i].second << "\n";
 
  int pl;
  int si;
  int pi=0;
  int ans=0,now=0;
  for(int i=0;i<=n;i++){
    pl = (S[i].first*(ll)p-1)/100;
    if(i>0 && S[i-1].first<S[i].first){
      si = S[i-1].second;
      CS[si]--; if(CS[si]==0) now--;
      BM[si]++; if(BM[si]==2) return ans;
    }
    while(pi<(n*2) && (S[pi].first<=pl)){
      si = S[pi].second;
      CS[si]++; if(CS[si]==1) now++;
      pi++;
    }
    ans = max(now,ans);
  }
  return ans;
}
 
int main(){
  int Case; read(Case); int tc=Case;
  while(Case--) printf("Case #%d: %d\n",tc-Case,solve());
}
