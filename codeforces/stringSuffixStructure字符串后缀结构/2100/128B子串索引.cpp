#include <bits/stdc++.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
typedef long long ll;

#define N 100003
char  S[N];

//notations from ML04book
struct SAM{
  int tot,last;
  int adj[N<<1][26],L[N<<1],f[N<<1]; //adj,L,f from ML04book
  int v[N<<1],tos[N<<1];   //tos=topo-ordered states; v is aux in building q.
  //meaning of cnt and sum is application dependent!
  int cnt[N<<1];  //@contruction,cnt[p]=1 means p contains a prefix! but post-process meaning is tricky!
  ll  sum[N<<1];  //sum may have different meaning, for exmaple: pfsc=PrefixedFactorSetCardinality
  int _newn(){++tot;memset(adj[tot],0,sizeof(adj[tot]));L[tot]=f[tot]=v[tot]=cnt[tot]=0;return tot;}
  void init(){tot=0;last=_newn();}
  void add(int c){
    int now=_newn(); L[now]=L[last]+1; cnt[now]=1;
    int p=last; while(p&&adj[p][c]==0){adj[p][c]=now;p=f[p];}
    if(p){
      int q=adj[p][c];
      if(L[q]>L[p]+1){ //Case3:split factor class!
        int nq=_newn(); L[nq]=L[p]+1;
        memcpy(adj[nq],adj[q],sizeof(adj[q]));
        f[nq]=f[q];
        f[q] =f[now]=nq;
        while(p&&adj[p][c]==q){adj[p][c]=nq;p=f[p];}
      }else f[now]=q;
    }else f[now]=1;
    last = now;
  }
  void topo_order(){
    memset(v,0,tot*sizeof(v[0]));
    for(int i=1;i<=tot;++i) v[L[i]]++;    //map i to |L[v]==i|
    for(int i=1;i<=tot;++i) v[i]+=v[i-1]; //map i to |L[v]<=i|, thus map L to segs of [0..tot]
    for(int i=tot;i;--i) tos[v[L[i]]--]=i;//tos[i] is a permutation of i, which is topological ordered!
  }
  void calc_pfsc(bool posIndexed){
    topo_order();
    for(int i=tot;i;--i){int s=tos[i]; if(posIndexed) cnt[f[s]]+=cnt[s];else cnt[s]=1;}
    cnt[1]=0;
    for(int i=tot;i;--i){int s=tos[i]; sum[s]=cnt[s]; for(int j=0;j<26;++j) sum[s]+=sum[adj[s][j]];}
  }
  void dfs(int p,int k){
    if(k<=cnt[p]) return;
    k-=cnt[p];
    for(int c=0;c<26;++c) if(adj[p][c]){
      ll t = sum[adj[p][c]];
      if(k<=t){
        putchar(c+'a');
        dfs(adj[p][c],k);
        return;
      }else k-=t;
    }
  }
  void printKthFactor(int k,bool posIndexed){
    calc_pfsc(posIndexed);
    if(k>sum[1]){cout <<  "No such line.\n"; return;}
    dfs(1,k); putchar('\n');
  }
  void debug(){
    for(int i=1;i<=tot;++i){
      cout << i << " : ";
      for(int j=0;j<26;++j) if(adj[i][j]) cout<<(char)(j+'a')<<"->"<<adj[i][j]<<" ";
      cout << "| f->"   << f[i];
      cout << "| cnt->" << cnt[i];
      cout << "| sum->" << sum[i];
      cout << endl;
    }
  }
}sam;

int main(){
  int k;
  scanf("%s",S);
  scanf("%d",&k);
  sam.init();
  for(int i=0;S[i];++i) sam.add(S[i]-'a');
  sam.printKthFactor(k,true);
  //sam.debug();
}
