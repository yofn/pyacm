#include <bits/stdc++.h>
using namespace std;
char  S[6000003];
const int N=1e6+3;
const int NC=3;
struct TRIE{
  int  nex[N][NC],end[N],tot;
  int  _new(){for(int i=0; i<NC; i++) nex[tot][i]=0; end[tot]=0; return tot++;}
  void init(){tot=0; _new();}
  void adds(char *s){int v=0; for(int i=0;s[i];++i){int c=s[i]-'a';v=nex[v][c]?nex[v][c]:(nex[v][c]=_new());} end[v]++;}
  int  find(char *s,int v){for(int i=0;s[i];v=nex[v][s[i++]-'a']) if(!nex[v][s[i]-'a']) return 0; return end[v];}
  int  solv(char *s){
    int v=0;
    for(int i=0;s[i];++i){
      int c = s[i]-'a';
      for(int j=0;j<NC;++j) if(j!=c && nex[v][j] && find(s+i+1,nex[v][j])) return 1;
      if(!nex[v][c]) return 0;
      v=nex[v][c];
    }
    return 0; //end[v];
  }
}kt;

int main(){
  int n,m;
  scanf("%d",&n); scanf("%d",&m);
  kt.init();
  for(int i=0;i<n;++i){scanf("%s",S);kt.adds(S);}
  for(int i=0;i<m;++i){scanf("%s",S);printf(kt.solv(S)?"YES\n":"NO\n");}
}
