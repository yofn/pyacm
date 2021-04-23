
#define tempt template<typename T>
#define tempu template<typename U>
#define final constexpr const
typedef unsigned int u32;
typedef std::vector<u32> vu;

dinic_t<int> ac;

tempt struct dinic_t {
  static final T inf = std::numeric_limits<T>::max();
  static final T eps = std::numeric_limits<T>::epsilon(); /// 此处嫌长可手写
  struct edge_t{
    u32 v;
    T   f;
    edge_t(u32 _v=0, T _f=0):v(_v),f(_f){}
  };
  std::vector<edge_t> edge; //edge array
  std::vector<vu>     adj;  //adj list
  vu  d, q;     //depth, q=bfs
  u32 n, s, t;  //node, source, target
  dinic_t() = default;  //dummy
  void init(u32 _n) {   //node size
    edge.resize(0);
    adj.resize(n = _n);
    for (u32 i = 0; i != n; ++i) adj[i].resize(0);
  }
  void _add(u32 u, u32 v, T f) {
    adj[u].push_back(edge.size());  //add edge to u's adj list
    edge.emplace_back(v, f);        //init edge as v,f
  }
  void add(u32 u, u32 v, T f) {
    _add(u, v, f);
    _add(v, u, 0);
  }
  bool bfs() {
    set_n(&d[0], -1, n);
    d[q[0] = s] = 0;
    for (u32 i = 0, j = 1; i != j; ++i) for (const auto& k : adj[q[i]]) {
      auto& e = edge[k];
      if (d[e.v] == -1u && e.f > eps) {
        d[e.v] = d[q[i]] + 1;
        if (e.v == t) return true;
        q[j++] = e.v;
      }
    }
    return false;
  }
  T dfs(u32 u, T f) {
    if (u == t || !(f > eps)) return f;
    T r = f, x;
    for (const auto& i : adj[u]) {
      auto& e = edge[i];
      if (d[u] + 1u == d[e.v] && e.f > eps) {
        if ((x = dfs(e.v, std::min(r, e.f))) > eps) {
          e.f -= x;
          edge[i ^ 1].f += x;
          if (!((r -= x) > eps)) return f;
        }
        else {
          d[e.v] = 0;
        }
      }
    }
    return f - r;
  }
  tempu U max_flow(u32 _s, u32 _t) {
    s = _s;
    t = _t;
    U f = 0;
    d.resize(n);
    q.resize(n);
    while (bfs()) f += dfs(s, inf);
    return f;
  }
};
