#include <bits/stdc++.h>

typedef unsigned int u32;
typedef std::vector<u32>  vu;
#define set_n(x, y, n) std::memset(x,y,sizeof(decltype(*(x)))*(n))

template<u32 maxn, u32 maxc = 26u>struct acam_t{
  u32 trie[maxn][maxc], fail[maxn], cnt[maxn], size;
  acam_t() = default;
  u32  new_node() {set_n(trie[size],0,maxc); fail[size]=cnt[size]=0; return size++;}
  void init()     {size=0; new_node();}
  void insert(const char* s, u32 n){
    u32 p = 0;
    for (u32 i=0; i<n; ++i) p=trie[p][s[i]-'a'] ? trie[p][s[i]-'a'] : (trie[p][s[i]-'a']=new_node());
    ++cnt[p]; // #string ended at p!
  }
  void build() {
    vu q;
    for (u32 i = 0; i != maxc; ++i) if (trie[0][i]) q.push_back(trie[0][i]);
    for (u32 i = 0; i != q.size(); ++i) {
      u32 p = q[i];
      for (u32 j = 0; j != maxc; ++j) {
        if (trie[p][j]) {
          fail[trie[p][j]] = trie[fail[p]][j];
          q.push_back(trie[p][j]);
        }
        else {
          trie[p][j] = trie[fail[p]][j];
        }
      }
    }
  }
};
