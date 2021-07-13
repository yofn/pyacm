#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
const int N = 400005;
int pa[N]; int find(int x){return pa[x]==x ? x: pa[x]=find(pa[x]);} //find & compression
int c[N];
int p[N];
int d[N];
#define bug(x) cout<<#x<<" is "<<x<<endl
 
bool solve(){
  int  i,n,nn,x,n1,n2,j1,j2,c1,c2,ans;
  cin>>n; nn=n<<1; //special case 1 FAIL due to violation of [1,n] range
  memset(c,0,nn*sizeof(int)); for(i=0;i<nn;i+=2)  c[i]=1;
  for(i=0;i<nn;++i)   pa[i]=i;
  for(i=0;i<nn;++i) cin>>d[i]; //read all input! don't LEAVE anything!
  memset(p,0,nn*sizeof(int));
  for(i=0;i<nn;++i){
    x=(d[i]<<1)-2;
    if(x<0||x>=nn||p[x^1]) return false;
    p[p[x]?x^1:x]=i+1;
  }
  for(int xx=0;xx<nn;xx+=2){ //xx refs2 value*2
    j1=p[xx  ]-1; //[0,nn)
    j2=p[xx^1]-1;
    if(j1<n){ n1 =  j1   <<1; n2 = j2<n ? j2<<1^1 : (j2-n)<<1;  } //cross or parallel
    else{     n1 = (j1-n)<<1; n2 = j2<n ? j2<<1   : (j2-n)<<1^1;} //parallel or cross, union n1 and n2!
    c1=find(n1); c2=find(n2);if(c1==c2) continue;
    pa[c2]=c1; c[c1]+=c[c2];  c[c2]=0; c1=c1^1;c2=c2^1; //c1=find(n1^1); c2=find(n2^1); if(c1==c2) continue;
    pa[c2]=c1; c[c1]+=c[c2];  c[c2]=0; //noc-=2; if(noc<2) return false;
  }
  //for(int i=0;i<nn;i+=2) if(find(i)==find(i^1)) return false;
  ans = 0;
  for(i=0;i<nn;i+=2) if(c[i]||c[i^1]){  //c[i] might be zeo!
    if(c[i]>c[i^1]){  ans += c[i^1]; c[i]=0;}
    else{             ans += c[i]; c[i^1]=0;}
  }
  cout << ans << endl;
  for(i=0;i<n;++i) if(c[find(i<<1)]) cout << i+1 << (--ans?" ":"");
  cout << endl;
  return true;
}
 
int main(){
  int tc; scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"-1\n";
}

