#include <bits/stdc++.h>
#define bug(x) cout<<#x<<" is "<<x<<endl
using namespace std;
typedef long long ll;

#define N 300005
char  S[N];
int *gend;
int *gl;

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
    int now=_newn(); L[now]=L[last]+1; pre[now]=true;
    int p=last; while(p&&adj[p][c]==0){adj[p][c]=now;p=f[p];}
    if(p){
      int q=adj[p][c];
      if(L[q]>L[p]+1){ //Case3:split factor class!
        int nq=_newn(); L[nq]=L[p]+1;
        memcpy(adj[nq],adj[q],sizeof(adj[q]));
        f[nq] =f[q];
        f[now]=f[q]=nq;
        while(p&&adj[p][c]==q){adj[p][c]=nq;p=f[p];}
      }else f[now]=q;
    }else f[now]=1;
    last = now;
  }
  void topo_order(){
    memset(v,0,tot*sizeof(v[0]));
    for(int i=1;i<=tot;++i) v[L[i]]++;    //map i to |L[v]==i|
    for(int i=1;i<=tot;++i) v[i]+=v[i-1]; //map i to |L[v]<=i|, thus map L to segs of [0..tot]
    for(int i=tot;i>=1;--i) tos[v[L[i]]--]=i;//tos[i] is a permutation of i, which is topological ordered!
  }
  static bool myfunction(int i,int j){return (gend[i]<gend[j] ||(gend[i]==gend[j] && gl[i]<gl[j]));}
  void endp_order(){sort(tos+1,tos+tot+1,myfunction);}
  void printSlogan(){
    int p,q,fp,maxcool;
    for(int i=1;i<=tot;++i) end[i]=pre[i]?L[i]:0; //set prefix's end
    topo_order();
    for(int i=tot;i>=1;--i){p=tos[i]; fp=f[p]; if(!end[fp] || end[p]<end[fp]) end[fp]=end[p];}
    maxcool=coo[1]=end[1]=0;
    endp_order();
    for(int i=2;i<=tot;++i){p=tos[i]; fp=f[p];
      if(end[fp]>end[p])  cout << end[fp] << '@' << fp << '>' << end[p] << '@' << p << endl; //TODO fix it!
      if(end[fp]==end[p]){coo[p]=coo[fp]; L[p]=L[fp];} //first child 
      if(end[fp]<end[p]){
        int rl = end[p]-end[fp]+L[fp];
        if(rl>L[p]){coo[p]=coo[fp];   L[p]=L[fp];}
        else       {coo[p]=coo[fp]+1; L[p]=rl; maxcool=max(maxcool,coo[p]);}
        end[fp]=end[p];
      }
    }
    cout << maxcool << endl;
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
  gl   = sam.L;
  for(int i=0;S[i];++i) sam.add(S[i]-'a');
  sam.printSlogan();
  //sam.debug();
}
