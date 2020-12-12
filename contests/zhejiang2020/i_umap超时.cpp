/* find the maxium connected component?  
 * note the range of a & b!
  int el[N<<1]={0}, dl[N]={0};  //edge list and degree list; degree always = 2
  use Multiple Map, instead of [k,list]
  int st[N]={0},vs[N+1]={0};
  use orderd edge, so that it's a tracking of edges!
  1 2
  1 3
  2 4
  3 5
  4 5
  dsu??
    if(el.count(b)>0) el[b].second =    a ;
    else              el[b]        = {a,0};
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
typedef unordered_map<int,pair<int,int>>  EdgesMap;
typedef unordered_map<int,bool>           VisitMap;
typedef set<int>                          NodesSet;
int st[N]={0};
int i,t,sp=0,ii,nn,mx;
pair<int,int> ep;
int Case,n,a,b;

int dfs(NodesSet ns, EdgesMap el,VisitMap vs){
  mx = 0;
  for(auto i : ns){
    if(vs[i]) continue; //if not initialized, = false?
    st[++sp] = i;
    nn       = 0;
    //cout << 'R' << i << "\n";
    while(sp){
      ii     = st[sp--];
      if(vs[ii]) continue;
      vs[ii] = true;
      nn    += 1;
      //cout << 'n' << ii << "\t";
      if(el.count(ii)>0){
        ep   = el[ii];
        if(!vs[ep.first ])              st[++sp]=ep.first ;
        if(ep.second && !vs[ep.second]) st[++sp]=ep.second;
      }
    }
    if(nn>mx) mx=nn;
  }
}

int solve(){
  EdgesMap el;
  VisitMap vs; //unordered_map:visited
  NodesSet ns;
  read(n);
  el.reserve(n);
  vs.reserve(n);
  for(i=1;i<=n;i++){
    read(a),read(b);  if(a>b){t=a;a=b;b=t;}
    if(el.count(a)>0) el[a].second =    b ;
    else              el[a]        = {b,0};
    if(el.count(b)>0) el[b].second =    a ;
    else              el[b]        = {a,0};
    ns.insert(a);
    ns.insert(b);
  }
  dfs(ns,el,vs);
  return mx;
}

int main(){
  read(Case);
  while(Case--) printf("%d\n",solve());
}
