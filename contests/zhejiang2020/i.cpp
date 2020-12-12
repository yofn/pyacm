/* find the maxium connected component?  
  dsu?
  bucket could conflict?
  //for (auto j:nodes)  cout << nodes.bucket(j) << "\t"; cout << "\n";
  //for (i=0;i<n;i++)   cout << pa[i] << "\t"; cout << "\n";
  //for (i=0;i<n;i++)   cout << gs[i] << "\t"; cout << "\n";
*/

#include <bits/stdc++.h>
using namespace std;

// template to simplify INPUT (but SLOWER)
int s;
template <class T> void read(T &x){
  char ch=getchar();
  for(s=0; !isdigit(ch); ch=getchar())     s |= (ch=='-');
  for(x=0;  isdigit(ch); ch=getchar())     x  = x*10 + ch - '0';
  if(s) x=-x;
}

#define N 100005
int pa[N], gs[N]; //parent array and group size!
int i,ag,bg,cnt;
int Case,n,a,b;

int find(int x){ return pa[x]==x ? x: pa[x]=find(pa[x]); }

int solve(){
  unordered_map<int,int> nodes;

  read(n);
  nodes.reserve(n);
  for(i=0;i<n;i++) pa[i] = i;
  for(i=0;i<n;i++) gs[i] = 1;
  cnt = 0;

  for(i=1;i<=n;i++){
    read(a),read(b);
    if(nodes.count(a)==0) nodes.insert({a,cnt++});
    if(nodes.count(b)==0) nodes.insert({b,cnt++});
    ag = find(nodes[a]);
    bg = find(nodes[b]);
    if(ag!=bg){
      pa[bg]  = ag;
      gs[ag] += gs[bg];
    }
  }
  return *max_element(gs,gs+n);
}

int main(){
  read(Case);
  while(Case--) printf("%d\n",solve());
}
