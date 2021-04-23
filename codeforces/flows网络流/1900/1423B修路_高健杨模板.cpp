//https://blog.csdn.net/weixin_30907935/article/details/101288061
#define bug(x) cout<<#x<<" is "<<x<<endl
#define IO std::ios::sync_with_stdio(0)
#include <bits/stdc++.h>
using namespace  std;
const int inf=2e9+10;
const int N=2e4+5,M=2e5+5;
struct node{
  int cnt;    //cnt@edges
  int P[M], V[M],R[M];  //edge info: previous edge, node-v@edge, Residual@edge.
  int RE[N],D[N];       //node's Recent EDGE and DEPTH
  int n,s,t;  //n=#node, s=source, t=target
  void init(){cnt=-1; memset(RE,-1,sizeof(RE)); memset(P,-1,sizeof(P));}
  void _add(int u,int v,int c){P[++cnt]=RE[u]; V[cnt]=v; C[cnt]=c; RE[u]=cnt;}
  void  add(int u,int v,int c){_add(u,v,c);_add(v,u,0);}
  bool bfs(){
    memset(D,0,sizeof(D));  D[s]=1;
    queue<int>q;            q.push(s);
    while(!q.empty()){
      int u=q.front(); q.pop();
      for(int e=RE[u];e!=-1;e=P[e]) if(!D[V[e]]&&R[i]>0){D[V[e]]=D[u]+1;q.push(V[e]);}
    }
    return D[t]>0;
  }
  int dfs(int u,int f){
    if(u==t)return f;
    int tem=f,k;
    for(int e=RE[u];e!=-1 && tem>0;e=P[e])  //opt1:multiple augmenting paths
      if(D[V[e]]-D[u]=1 && R[e]>0)  {
        k=dfs(V[e],min(f,R[e]));
        if(!k){D[V[e]]=0; continue;}        //opt2:current arc
        tem   -=k;
        R[e]  -=k;
        R[e^1]+=k;
      }
    return f-tem; //original flow-left flow = flow IN
  }
  int dinic(){
    int res=0,i;
    while(bfs()) while(i=dfs(s,inf))res+=i;
    return res;
  }
}ac;
int main(){
  int n,m;
  scanf("%d%d",&n,&m);
  int s=1,t=n+n+2;
  ac.init();
  ac.n=n1+n2+2;
  ac.s=s;
  ac.t=t;
  for(int i=1;i<=n1;i++){
    ac.add(1,i+1,1);
  }
  for(int i=1;i<=m;i++){
    int x,y;
    scanf("%d%d",&x,&y);
    if(x<=n1&&y<=n2){
      ac.add(x+1,y+n1+1,1);
    }
  }
  for(int i=1;i<=n2;i++){
    ac.add(i+n1+1,t,1);
  }
  printf("%d\n",ac.dinic());
}
