#include <bits/stdc++.h>
using namespace std;

#define LOCAL

#define templ template <
#define tempr >
#define typet typename T
#define typeu typename U
#define types typename... Ts
#define tempt templ typet tempr
#define tempu templ typeu tempr
#define final constexpr const
tempt struct range {
  T b, e;
  range(T _b, T _e): b(_b), e(_e) {}
  T begin() const {return b;}
  T end()   const {return e;}
};
tempt range<T> make_range(T b, T e) {return range<T>(b,e);}
tempt struct is_cont {static final bool value = false;};
tempt struct is_cont<range<T>> {static final bool value = true;};
templ types tempr struct is_cont<std::vector<Ts...>> {static final bool value = true;};
templ typet, typeu tempr std::ostream& operator<<(std::ostream& os, const std::pair<T, U>& p){
  return os << '<' << p.ff << ',' << p.ss << '>';
}
tempt std::enable_if_t<is_cont<T>::value, std::ostream>& operator<<(std::ostream& os, const T& c) {
  if (c.begin() == c.end()) return os << "{}";
  auto it = c.begin();
  os << '{' << *it;
  while (++it != c.end()) os << ',' << *it;
  return os << '}';
}
void dbg() { std::cerr << std::endl; }
templ typet , types tempr void
dbg(T arg, Ts... args) { std::cerr << ' ' << arg; dbg(args...); }
#ifdef LOCAL
#define debug(...) std::cerr << "["#__VA_ARGS__"] :", dbg(__VA_ARGS__)
#else
#define debug(...) 0
#endif

const int N = 2002;     vector<int> e[N]; bool match[N]; int sta[N],top; char name[N][4];
const int M = 30;       char S[M];
const int L = 26*26*26; vector<int> f[L]; vector<int> s[L];
#define bug(x) cout<<#x<<" is "<<x<<endl

bool dfs(int x){
  if(match[x])    return true;
  if(match[x^1])  return false;
  sta[top++]=x;
  match[x]=true;
  for(auto &y:e[x]) if(!dfs(y)) return false;
  return true;
}

bool solve(){
  int n,m;
  scanf("%d",&n);  m=n+1;
  for(int i=0;i<2*m;++i)  e[i].clear();
  for(int i=0;i<L;++i)    f[i].clear();
  for(int i=0;i<L;++i)    s[i].clear();
  for(int i=2;i<2*m;i+=2){
    scanf("%s",S);
    int j=((S[0]-'A')*26+(S[1]-'A'))*26;
    f[j+(S[2]-'A')].push_back(i);
    name[i  ][0]=S[0];  name[i  ][1]=S[1]; name[i  ][2]=S[2]; name[i  ][3]=0;
    name[i^1][0]=S[0];  name[i^1][1]=S[1];
    scanf("%s",S);
    s[j+(S[0]-'A')].push_back(i^1);
    name[i^1][2]=S[0];  name[i^1][3]=0;
  }
  memset(match,false,sizeof(match));
  for(int i=0;i<L;++i){
    int x=f[i].size();
    if(x==0) continue;
    if(x>1) for(auto j:f[i]) e[     0 ].push_back(j^1); //0 represent OKAY!
    else    for(auto j:s[i]) e[f[i][0]].push_back(j^1);
  }
  for(int i=0;i<L;++i)
    if(s[i].size()>1)
      for(auto &j:s[i]) for(auto &k:s[i]) if(j!=k)
        e[j].push_back(k^1);
  //for(int i=0;i<2*m;i++) debug(e[i]);
  //for(int i=0;i<2*m;i++) debug(match[i]);
  for(int i=0;i<2*m;i+=2) if(!match[i] && !match[i^1]){
    top = 0;
    if(!dfs(i)){
      for(int j=0;j<top;++j)match[sta[j]]=false;
      if(!dfs(i^1)) return false;
    }
  }
  if(!match[0]) return false;
  cout << "YES" << endl;
  for(int i=2;i<2*m;i+=2)
    cout << (match[i]?name[i]:name[i^1]) << endl;
  return true;
}

int main(){
  if(!solve()) cout << "NO" << endl;
}
