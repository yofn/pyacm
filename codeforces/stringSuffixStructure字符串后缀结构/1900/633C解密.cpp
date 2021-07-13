/*
  //for(int i=0;i<pl;++i)             P[i]=tolower(P[i]);
  int  find(char *s,int l){int v=0; for(int i=0;i<l;v=nex[v][s[i++]-'a'])if(!nex[v][s[i]-'a']) return 0; return end[v];}
  for(int i=0;i<pl;i+=strlen(P+i)+1)  puts(P+i);
  kt.disp();
  void disp(){
    queue<int> q;
    q.push(0);
    while(!q.empty()){
      int v=q.front(); q.pop();
      for(int j=0;j<26;++j) if(nex[v][j]){cout << char(j+'a'); q.push(nex[v][j]); if(end[nex[v][j]]) cout<<'$';}
      cout << '|';
    }
    cout << '\n';
  }
#define bug(x) cout<<#x<<" is "<<x<<endl
*/

#include <bits/stdc++.h>
using namespace std;
char  text[10003];
int   vist[10003];  //visited for memorized search
char  P[2000006];
const int N=1e6+3;
struct TRIE{
  int  nex[N][26],end[N],inf[N],tot; //inf for additional info
  vector<int> pos;
  int  _new(){for(int i=0; i<26; i++) nex[tot][i]=0; end[tot]=inf[tot]=0; return tot++;}
  void init(){tot=0; _new();}
  void adds(char *s,int l){
    int v=0;
    for(int i=0;s[i];i++){
      int c = tolower(s[i])-'a';
      v=nex[v][c]?nex[v][c]:(nex[v][c]=_new());
    }
    end[v]++;
    inf[v]=l;
  }
  int  solv(char *s,int l){
    int v=0;
    for(int i=l-1;i>=0;v=nex[v][s[i--]-'a']){
      if( end[v] && !vist[i+1] && solv(s,i+1)){
        pos.push_back(inf[v]);
        return 1;
      }
      if(!nex[v][s[i]-'a']){vist[l]=1;return 0;}
    }
    if(!end[v]){
      vist[l]=1;
      return 0;
    }else{
      pos.push_back(inf[v]);
      return 1;
    }
  }
}kt;

int main(){
  int tl,pc;
  scanf("%d",&tl); scanf("%s",text);
  scanf("%d",&pc);
  kt.init();
  for(int i=0; pc--; i+=strlen(P+i)+1){
    scanf("%s",P+i);
    kt.adds(P+i,i);
  }
  for(int i=0;i<=tl;++i) vist[i]=0;
  kt.solv(text,tl);
  for(int p:kt.pos) printf("%s ",P+p);
  printf("\n");
}
