/*
 head=head of arrow,tail of edge; last=last edge
 d[u]=distance of u; p[u]=>newest edge from u
 #edge,#node,e/2,st=start,ed=end
*/

#include <bits/stdc++.h>
using namespace std;

#define bug(x) cout<<#x<<" is "<<x<<endl

const int inf = 0x7FFFFFFF;
const int N =2e4+5; typedef int nodes[N]; nodes p,d; //n2fe, depth
const int M =1e5+2; typedef int edges[M]; edges srtd;//sorted time
const int TE=3e5;   typedef int arcs[TE]; arcs  head,flow,last,arct;
int e,n,m,st,ed;
queue<int> q;
int maxt;

void add(int u,int v,int f,int t){last[++e]=p[u]; p[u]=e; head[e]=v; flow[e]=f; arct[e]=t;}

bool bfs(){
  memset(d,0,sizeof(d));    d[st]=1;
  while(!q.empty())q.pop(); q.push(st);
  while(!q.empty()){
    int u=q.front(); q.pop();
    for(int j=p[u]; j; j=last[j]){
      if(arct[j]>maxt) continue;
      if(!d[head[j]] && flow[j]){int v=head[j]; d[v]=d[u]+1; if(v==ed) return true; q.push(v);}
    }
  }
  return false;
}

int dinic(int u,int f){
  if(u==ed) return f;
  int tem=f,k;
  for(int j=p[u]; j && tem; j=last[j]){
    if(arct[j]>maxt) continue;
    if(d[head[j]]==d[u]+1 && flow[j]>0){
      int v=head[j];
      k=dinic(v,min(tem,flow[j]));
      if(!k)d[v]=0;
      tem      -=k;
      flow[j]  -=k;
      flow[j^1]+=k;
    }
  }
  return f-tem;
}

int  MaxFlow(){int ans=0,i; while(bfs()) while(i=dinic(st,inf)) ans+=i; return ans;}
void RstFlow(){for(int i=2;i<=e;){flow[i++]=1; flow[i++]=0;}}

int binsearch(){
  int l,r,mm,f;
  int ans=-1;
  for(l=0,r=m-1;l<=r;){
    mm   = l+((r-l)>>1);
    maxt = srtd[mm];
    f    = MaxFlow(); RstFlow();
    if(f==n){
      r   = mm-1;
      ans = maxt;
    }else{
      l   = mm+1;
    }
  }
  return ans;
}

int main(){
  int u,v,t,uo,vo;
  int inst=0;
  e=1; memset(p,0,sizeof(p)); //e=0/1 reserved for null
  cin >> n >> m;
  st = 1; ed=(n<<1)+2; uo=st; vo=uo+n;
  for(int i=st+1;i<=st+n;++i){add(st,i,1,inst); add(i,st,0,inst);}//keep f[2]=1,f[3]=0
  for(int i=ed-1;i>=ed-n;--i){add(i,ed,1,inst); add(ed,i,0,inst);}
  for(int i=0;i<m;++i){scanf("%d%d%d",&u,&v,&t); srtd[i]=t; add(u+uo,v+vo,1,t); add(v+vo,u+uo,0,t);}
  sort(srtd,srtd+m);
  cout << binsearch() << endl;
}
