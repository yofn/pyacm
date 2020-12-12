#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5; //segtree: max size
int  n;               //segtree: real size
int  t[2*MAXN];       //segtree-data
bool lazy[MAXN];      //segtree-lazy
int  bulb[MAXN+1];    //bulb

void action(int p,int x){
  t[p] = x; if(p<n) lazy[p]=1;
}

void apply(int p,int x){
  for(int i=1,l=2,r=3,h=sizeof(int)*8-__builtin_clz(p)-1;
      i<p; lazy[i]=0,i=p>>(--h),l=i<<1,r=i<<1|1) if(lazy[i]){ //wake up lazy parents!
    if(t[l]<t[i]) action(l,t[i]);
    if(t[r]<t[i]) action(r,t[i]);
  }
  if(x>t[p])      action(p,x);
}

void flush(){
  for(int i=1,l=2,r=3;
      i<n; lazy[i++]=0,         l=i<<1,r=i<<1|1) if(lazy[i]){  //onetime-flush of all parent values;
    if(t[l]<t[i]) action(l,t[i]);
    if(t[r]<t[i]) action(r,t[i]);
  }
}

void modify(int l, int r, int x){
  for(l+=n,r+=n; l<r; l>>=1,r>>=1){
    if(l&1) apply(l++,x);
    if(r&1) apply(--r,x);
  }
}

void solve(){
  int x,xx,tt;
  scanf("%d%d",&x,&n);                 //x=#bulbs, n=#seconds (aka.segtree size)!
  for(int i=1;i<2*n;  i++)     t[i]=0; //segtree-data
  for(int i=1;i<n;    i++)  lazy[i]=0; //segtree-lazy
  for(int i=1;i<=MAXN;i++)  bulb[i]=0; //bulb at t
  for(int i=1;i<=x;   i++){
    scanf("%d%d",&tt,&xx);
    bulb[tt] = max(bulb[tt],xx);
  }
  for(int i=MAXN;i>=1;i--) if(bulb[i]>0){
    for(int l=0;l<=n;l+=(i<<1)) modify(l,min(n,l+i),bulb[i]);
  }
  flush();
}

int main(){
  int Case;
  scanf("%d",&Case);
  for(int i=1;i<=Case;i++){
    solve();
    cout << "Case #" << i << ":";
    for(int j=0;j<n;j++) cout << " " << t[j+n]; cout << "\n";
  }
}
