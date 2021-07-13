#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
#define N 1000010
int v[N];
char s[N];
int n;
struct AC
{
  int next[N][26];
  int last[N],f[N];
  int len[N];
  int tot;
  void init()
  {
    tot=−1;
    newnode();
  }
  int newnode()
  {
    ++tot;
    for(int i=0; i<26; i++) next[tot][i]=0;
    len[tot]=0;
    f[tot]=last[tot]=0;
    return tot;
  }
  void insert(char *s)
  {
    int now=0;
    for(int i=0; s[i] ; i++)
    {
      142
        字符串算法
        15
        if(!next[now][s[i]−'a']) next[now][s[i]−'a']=newnode();
      now=next[now][s[i]−'a'];
    }
    len[now]=strlen(s);
  }
  void work(int i,int now)
  {
    while(now)
    {
      v[i+1]++;
      v[i−len[now]+1]−−;
      now=last[now];
    }
  }
  void find(char *s)
  {
    int now=0;
    for(int i=0; s[i] ; i++)
    {
      if(!isalpha(s[i]))
      {
        now=0;
        continue;
      }
      int x=tolower(s[i])−'a';
      now=next[now][x];
      work(i,now);
    }
  }
  void get_fail()
  {
    queue<int> q;
    int x,y;
    for(int i=0; i<26; i++)
      if(x=next[0][i])
        q.push(x);
    while(!q.empty())
    {
      x=q.front();
      q.pop();
      for(int i=0; i<26; i++)
        if(y=next[x][i])
        {
          q.push(y);
          f[y]=next[f[x]][i];
          last[y]=len[f[y]]?f[y]:last[f[y]];
        }
        else next[x][i]=next[f[x]][i];
    }
  }
} ac;
int main()
{
  int sk;
  scanf("%d",&sk);
  while(sk−−)
  {
    ac.init();
    scanf("%d",&n);
    for(int i=1; i<=n; i++)
    {
      scanf("%s",s);
      ac.insert(s);
    }
    ac.get_fail();
    getchar();
    gets(s);
    for(int i=0; s[i]; i++) v[i]=0;
    ac.find(s);
    long long ans=0;
    for(int i=0; s[i]; i++)
    {
      ans+=v[i];
      if(ans<0) printf("*");
      else printf("%c",s[i]);
    }
    puts("");
  }2
  字符串算法
}
