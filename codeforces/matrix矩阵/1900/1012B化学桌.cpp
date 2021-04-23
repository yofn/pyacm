#include <bits/stdc++.h>
using namespace std;
//union-find set!

// template to simplify INPUT (but SLOWER)
template <class T> void read(T &x){
  char ch=getchar(); int s;
  for(s=0; !isdigit(ch); ch=getchar())     s |= (ch=='-');
  for(x=0;  isdigit(ch); ch=getchar())     x  = x*10 + ch - '0';
  if(s) x=-x;
}

const int C0 = 200001;
const int N  = 400001;
int pa[N]; int find(int x){return pa[x]==x ? x: pa[x]=find(pa[x]);} //find & compression

int solve(){
  int n,m,q,ce;
  int r,c,rg,cg;
  int noc;
  read(n); read(m); read(q); ce = C0+m; noc=n+m;
  for(int i=1; i<=n; i++)   pa[i]=i;  //row-idx nodes
  for(int i=1+C0;i<=ce;i++) pa[i]=i;  //col-idx nodes

  for(int i=1;i<=q;i++){
    read(r); rg = find(r);
    read(c); cg = find(c+C0);
    if(rg!=cg){
      pa[rg] = cg;     //union
      noc --;
    }
  }
  return noc-1;
}

int main(){
  //read(Case); int tc=Case; while(Case--) printf("Case #%d: %d\n",tc-Case,solve());
  printf("%d\n",solve());
}
