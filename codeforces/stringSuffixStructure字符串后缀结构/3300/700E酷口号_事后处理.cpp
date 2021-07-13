#include <bits/stdc++.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
typedef long long ll;

#define N 200005
char  S[N];

//notations from ML04book
struct SAM{
  int tot,last;
  int adj[N<<1][26],L[N<<1],f[N<<1]; //adj,L,f from ML04book
  int v[N<<1],tos[N<<1];   //tos=topo-ordered states; v is aux in building q.
  //meaning of cnt and sum is application dependent!
  bool pre[N<<1];  //isPrefix mark
  int  coo[N<<1];  //cool position from right for slogon! see this problem!
  int _newn(){++tot;memset(adj[tot],0,sizeof(adj[tot]));L[tot]=f[tot]=v[tot]=pre[tot]=0;return tot;}
  void init(){tot=0;last=_newn();}
  void add(int c){
    int now=_newn(); L[now]=L[last]+1; pre[now]=true; //len[now]=max(len[last],1);
    int p=last; while(p&&adj[p][c]==0){adj[p][c]=now;p=f[p];}
    if(p){
      int q=adj[p][c];
      if(L[q]>L[p]+1){  //Case3:split factor class!
        int nq=_newn(); L[nq]=L[p]+1;
        memcpy(adj[nq],adj[q],sizeof(adj[q]));
        f[nq]=f[q];
        f[q] =f[now]=nq;
        while(p&&adj[p][c]==q){adj[p][c]=nq; p=f[p];}
      }else f[now]=q;   //Case2:z=z'; len[now]=max(len[now],len[q]+1); //chance to be updated by +1 from q or nq!
    }else f[now]=1;     //Case1:new symbol
    last = now;
  }
  void topo_order(){
    memset(v,0,tot*sizeof(v[0]));
    for(int i=1;i<=tot;++i) v[L[i]]++;    //map i to |L[v]==i|
    for(int i=1;i<=tot;++i) v[i]+=v[i-1]; //map i to |L[v]<=i|, thus map L to segs of [0..tot]
    for(int i=tot;i;--i) tos[v[L[i]]--]=i;//tos[i] is a permutation of i, which is topological ordered!
  }
  void printSlogan(){
    int rp=1;
    topo_order();
    coo[0]=0; //for convience
    for(int i=tot;i;--i) coo[i]=0;
    for(int i=tot;i;--i){
      int p = tos[i];
      int c = 0;
      for(int j=0;j<26;++j) c=max(coo[adj[p][j]],c);
      coo[p]= c==coo[p]? c+1:max(coo[p],c);
      coo[f[p]]=coo[p];
    }
    cout << coo[1]-1 << endl;
  }
}sam;

int main(){
  int k;
  scanf("%d",&k);
  scanf("%s",S);
  sam.init();
  for(int i=0;S[i];++i) sam.add(S[i]-'a');
  sam.printSlogan();
  //sam.debug();
}
