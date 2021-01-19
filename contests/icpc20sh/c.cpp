#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;
typedef unsigned int ui;

ll solve(){
  bool yb,hp,nx2b,ny2b,nxy2b,yi,xi;
  ui nx,x,y,t,p;
  ll cbb,cbh,chb;
  ll wbb,wbh,whb;
  scanf("%d%d",&x,&y);
  if(x+y==0) return 0;
  if(x<y){t=x;x=y;y=t;}
  nx  = sizeof(int)*8 - __builtin_clz(x);
  p   = (1<<(nx-1));
  yb  = (y&p)>0;
  hp  = !yb;
  cbb=chb=yb; cbh=1;
  whb=wbh=yb; wbb=0;
  for(int i=1;i<nx;i++){
    p  >>= 1;
    xi   = (x&p)>0;
    yi   = (y&p)>0;
    yb   = yb || yi;
    nx2b = hp && xi;
    ny2b = hp && yi;
    nxy2b= hp && xi && yi;
    if(yb){
      cbb += (cbb<<1)   + (xi?(chb<<1):0) + (yi?(cbh<<1):0) +  nxy2b;
      wbb += (wbb<<1)   + (xi?(whb<<1):0) + (yi?(wbh<<1):0) + (nxy2b?i:0) + cbb -1;
      chb += (xi?0:chb) +  ny2b;
      whb += (xi?0:whb) + (ny2b?i:0) + chb;
    }
    cbh += (yi?0:cbh) +  nx2b;
    wbh += (yi?0:wbh) + (nx2b?i:0) + cbh - (yb?0:1);
    hp   = hp && (xi+yi<2);
  }
  return (wbb+wbh+whb+(hp?nx:0))%1000000007;
}

int main(){
  int tc;
  scanf("%d",&tc);
  for(int i=1;i<=tc;i++) printf("%lld\n",solve());
}
