#include <bits/stdc++.h>
using namespace std;
/* find the maxium connected component?  
 * note the range of a & b!
  int el[N<<1]={0}, dl[N]={0};  //edge list and degree list; degree always = 2
  use Multiple Map, instead of [k,list]
  int st[N]={0},vs[N+1]={0};
*/

// template to simplify INPUT (but SLOWER)
int s;
template <class T> void read(T &x){
  char ch=getchar();
  for(s=0; !isdigit(ch); ch=getchar())     s |= (ch=='-');
  for(x=0;  isdigit(ch); ch=getchar())     x  = x*10 + ch - '0';
  if(s) x=-x;
}

#define N 100005
multimap<int,int> el; //multimap:edge-list
map<int,bool>     vs; //map:visited
int st[N]={0};
//typedef multimap<int,int>::iterator EdgeIterator;
//pair<EdgeIterator,EdgeIterator> res; //iterator:result
int i,sp=0,ii,nn,j,mx,k;
int Case,n,a,b;

int dfs(){
  mx = 0;
  for(i=1;i<=n;i++){
    if(vs[i]) continue;
    st[++sp] = i;
    nn       = 0;
    while(sp){
      ii     = st[sp--];
      if(vs[ii]) continue;
      vs[ii] = true;
      nn    += 1;
      auto it = el.equal_range(ii);
      for(auto itr=it.first; itr!=it.second; ++itr){
        j = itr->second;
        if(!vs[j]) st[++sp]=j;
      }
    }
    if(nn>mx) mx=nn;
  }
  el.clear();
  vs.clear();
}

int solve(){
  read(n);
  for(i=1;i<=n;i++){
    read(a),read(b);
    el.insert({a,b});
    el.insert({b,a});
    vs[a] = false;
    vs[b] = false;
  }
  dfs();
  return mx;
}

int main(){
  read(Case);
  while(Case--) printf("%d\n",solve());
}
