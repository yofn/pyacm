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

const int N = 300005;
int pa[N],ww[N];  //ww = #edge - #node
int i,ag,bg;
int Case,n,m,a,b,ans;

int find(int x){return pa[x]==x ? x: pa[x]=find(pa[x]);} //find while compression

int solve(){
  read(n), read(m);
  for(i=1;i<=n;i++){
    pa[i] =  i;
    ww[i] = -1;         //0 edge, 1 node!
  }
  for(i=1;i<=m;i++){
    read(a),read(b);
    ag = find(a);
    bg = find(b);
    if(ag!=bg){
      pa[bg]  = ag;     //union
      ww[ag] += ww[bg]; //before add NEW edge!
    }
    ww[ag] += 1;        //account for the NEW edge!
  }
  /*
  ans = 0;
  for(i=1;i<=n;i++){
    if(pa[i]==i && ww[i]>0) ans+=ww[i];
  }
  */
  ans = m-n;
  for(i=1;i<=n;i++){
    if(pa[i]==i && ww[i]<0) ans++;
  }
  return ans;
}

int main(){
  read(Case);
  int tc=Case;
  while(Case--) printf("Case #%d: %d\n",tc-Case,solve());
}
