#include <bits/stdc++.h>
using namespace std;
//union-find set!

// template to simplify INPUT (but SLOWER)
int s;
template <class T> void read(T &x){
  char ch=getchar();
  for(s=0; !isdigit(ch); ch=getchar())     s |= (ch=='-');
  for(x=0;  isdigit(ch); ch=getchar())     x  = x*10 + ch - '0';
  if(s) x=-x;
}

const int N = 100001;
int xmax[N]={0},xat[N];
int Case,n,m,x,t,ans;
int l,r;
int i,j;

int solve(){
  read(n); read(m);
  for(i=1;i<=m;i++)   xat[i]=0;
  for(i=1;i<=N;i++)  xmax[i]=0;
  for(i=1;i<=n;i++){ scanf("%d",&t); scanf("%d",&x); if(x>xmax[t]) xmax[t]=x; }
  //for(i=1;i<=m;i++) cout << " " << xmax[i];
  for(t=N-1;t>=1;t--){
    if(xmax[t]>0){
      x = xmax[t];
      i = t;
      while(i>2 && i%2==0){
        i >>= 1;
        if(x>=xmax[i]){
          xmax[i]=0;
        }
      }
      l = 1;
      //cout << x << "t" << i;
      while(l<=m){
        r = min(m+1,l+t);
        //cout << l << "-" << r;
        for(j=l;j<r;j++){
          if(x>xat[j]) xat[j]=x;
        }
        l = r+t;
      }
    }
  }
  return 1;
}

int main(){
  read(Case);
  int tc=Case;
  while(Case--){
    solve();
    cout << "Case #" << tc-Case << ":";
    for(i=1;i<=m;i++)
      cout << " " << xat[i];
    cout << "\n";
  }
}
