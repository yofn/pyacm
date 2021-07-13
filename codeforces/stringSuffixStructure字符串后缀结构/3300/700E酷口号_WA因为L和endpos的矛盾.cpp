#include <bits/stdc++.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
typedef long long ll;

#define N 200005
char  S[N];
int *gend;
int *gtos;

//notations from ML04book
struct SAM{
  int tot,last;
  int adj[N<<1][26],L[N<<1],f[N<<1]; //adj,L,f from ML04book
  int v[N<<1],tos[N<<1];   //tos=topo-ordered states; v is aux in building q.
  //meaning of cnt and sum is application dependent!
  bool pre[N<<1];   //isPrefix mark
  int  end[N<<1];   //end=end position..used for coo!
  int  coo[N<<1];   //cool position from right for slogon! see this problem!
  int _newn(){++tot;memset(adj[tot],0,sizeof(adj[tot]));L[tot]=f[tot]=v[tot]=pre[tot]=0;return tot;}
  void init(){tot=0;last=_newn();}
  void add(int c){
    int q=1; //q=f[now], for CASE1
    int p=last; while(p&&adj[p][c]==0) p=f[p];
    //Case3: CLONE first, then add NOW so that endpos is maintained!
    if(p){q=adj[p][c];
      if(L[q]>L[p]+1){  //Case3:split factor class!
        int nq=_newn(); L[nq]=L[p]+1;
        memcpy(adj[nq],adj[q],sizeof(adj[q]));
        f[nq]=f[q]; f[q]=nq; //insert nq between q and f[q]!
        while(p&&adj[p][c]==q){adj[p][c]=nq; p=f[p];}
        q=nq;  //for assignment
      }
    }
    //COMMON@CASE1-3
    int now=_newn(); pre[now]=true; L[now]=L[last]+1;
    f[now]=q; for(p=last;p&&adj[p][c]==0;p=f[p]) adj[p][c]=now;
    last  =now;
  }
  void topo_order(){
    memset(v,0,tot*sizeof(v[0]));
    for(int i=1;i<=tot;++i) v[L[i]]++;    //map i to |L[v]==i|
    for(int i=1;i<=tot;++i) v[i]+=v[i-1]; //map i to |L[v]<=i|, thus map L to segs of [0..tot]
    for(int i=tot;i>=1;--i) tos[v[L[i]]--]=i;//tos[i] is a permutation of i, which is topological ordered!
  }
  static bool myfunction(int i,int j){return (gend[gtos[i]]<gend[gtos[j]]);}
  void endp_order(){  //optimize by vv if necessary
    memset(v,0,tot*sizeof(v[0]));
    for(int i=1;i<=tot;++i) v[L[i]]++;    //map i to |L[v]==i|
    for(int i=1;i<=tot;++i) v[i]+=v[i-1]; //map i to |L[v]<=i|, thus map L to segs of [0..tot]
    for(int i=1;i<=tot;++i) cout << tos[i] << ' ';  cout<<endl;
    for(int i=1;i<=tot;++i){
      int l=v[i-1]+1; int r=v[i]+1; if(l==r) break;
      if(l<r-1) sort(tos+l,tos+r,myfunction);
    }
    for(int i=1;i<=tot;++i) cout << tos[i] << ' ';  cout<<endl;
  }
  void printSlogan(){
    int p,q,fp;
    for(int i=1;i<=tot;++i) end[i]=pre[i]?L[i]:0; //set prefix's end
    for(int i=1;i<=tot;++i) coo[i]=0;
    topo_order();
    for(int i=tot;i>=1;--i){p=tos[i]; fp=f[p]; if(!end[fp] || end[p]<end[fp]) end[fp]=end[p];}//update end along suffix path
    end[1]=0; //for(int j=0;j<26;++j){q=adj[1][j]; if(q) coo[q]=1;}
    endp_order();
    for(int i=2;i<=tot;++i){p=tos[i]; fp=f[p];
      if(end[fp]>end[p]) cout << end[fp] << '@' << fp << '>' << end[p] << '@' << p << endl; //TODO fix it!
      if(end[fp]<end[p] && end[fp]-L[fp]>=end[p]-L[p] && coo[fp]>=coo[p]) coo[p]=coo[fp]+1;
      end[fp]=end[p];
      for(int j=0;j<26;++j){q=adj[p][j]; if(q && coo[p]>coo[q]) coo[q]=coo[p];}
    }
    cout << coo[tos[tot]] << endl;
  }
  void debug(){
    for(int i=1;i<=tot;++i){
      cout << i << " : ";
      for(int j=0;j<26;++j) if(adj[i][j]) cout<<(char)(j+'a')<<"->"<<adj[i][j]<<" ";
      cout << "| f->"   << f[i];
      cout << "| L->"   << L[i];
      cout << "| end->" << end[i];
      cout << "| coo->" << coo[i];
      cout << endl;
    }
  }
}sam;

int main(){
  int k;
  scanf("%d",&k);
  scanf("%s",S);
  sam.init();
  gend = sam.end;
  gtos = sam.tos;
  for(int i=0;S[i];++i) sam.add(S[i]-'a');
  sam.printSlogan();
  sam.debug();
}
