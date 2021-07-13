#include <bits/stdc++.h>
using namespace std;
#define bug(x) cout<<#x<<" is "<<x<<endl

#define N 1000006
int p[N],head[N],last[N],e;   //TODO 1-based!
int dfn[N],low[N],dfncnt;     //dfn/low@tarjan
int sta[N],top; bool ins[N];  //stack, top, in-stack
int csz[N],n2c[N],ccnt;       //(strong)component-size, n\mapsto c, cnt;

//e admits y as its head(destination); e admits x's old 1st edge as next edge; x admits e as 1st edge;
void add(int x,int y){head[++e]=y;last[e]=p[x];p[x]=e;}

void tarjan(int x){
  int y; dfn[x]=low[x]=++dfncnt; ins[sta[++top]=x]=true;
  for(int j=p[x]; j; j=last[j]){
    y = head[j];
    if(!dfn[y]){tarjan(y); low[x]=min(low[x],low[y]); continue;} //not visited
    if( ins[y])            low[x]=min(low[x],dfn[y]); //visted and @stack
  }
  if(low[x]==dfn[x]){
    csz[++ccnt]=0; //1-based
    do{ins[y=sta[top--]]=false; csz[n2c[y]=ccnt]++;}while(y!=x);
  }
}

bool solve(){
  int  n,m,x,y,ppl,cat;
  cin >> n >> m; ++n; ++m; //n,m++
  memset(p,   0,n*sizeof(int)); //#node
  memset(dfn, 0,n*sizeof(int));
  memset(low, 0,n*sizeof(int));
  memset(ins, 0,n*sizeof(bool));
  ccnt=dfncnt=top=e=0;  //NO need to memset: scz&sta(ccnt&top); n2c(write all); head(write all); last(write all);
  for(int i=1;i<m;++i){scanf("%d",&x);scanf("%d",&y);add(x,y);} //edge from x to y;
  for(int i=1;i<n;++i) if(!dfn[i]) tarjan(i);
  if(ccnt==1) return false;
  ppl = csz[1]; cat=n-1-ppl;
  cout << "Yes\n" << ppl << ' ' << cat << endl; //1-based!
  for(int i=1;i<n;++i) if(n2c[i]==1) cout << i << (--ppl?' ':'\n');
  for(int i=1;i<n;++i) if(n2c[i]!=1) cout << i << (--cat?' ':'\n');
  return true;
}

int main(){
  int tc; scanf("%d",&tc);
  while(tc--) if(!solve()) cout<<"No\n";
}
