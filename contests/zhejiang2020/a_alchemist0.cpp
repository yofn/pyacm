#include <bits/stdc++.h>

/*
 * prefix sum..
 *
 */

using namespace std;

int           y[10005][13][32];
array<int,3>  p[10005][13][32];

bool leap(int x){
  return x%400==0 || (x%4==0 && x%100);
}

void pre(){
  int pi=1999,pj=12,pk=32;
  for(int i=2000;i<=9999;i++){
    for(int j=1;j<=12;j++){
      int up=31;
      if(j==2){
        up = 28 + leap(i);
      }else if(j==4|j==6|j==9|j==11){
        up = 30;
      }
      for(int k=1;k<=up;k++){
        y[i][j][k]=y[pi][pj][pk];
        if(i/10==202||i%1000==202||(i%10==2&&j==2)||(j%10==2&&k==2)){
          y[i][j][k]++;
        }
        p[i][j][k] = {pi,pj,pk};
        pi=i, pj=j, pk=k;
      }
    }
  }
}

int read(){
  string s;
  cin >> s;
  int x=0;
  for(auto c:s){
    x=x*10+(c-'0');
  }
}

int solve(){
  int y1=read(), m1=read(), d1=read(), y2=read(), m2=read(), d2=read();
  cout << y[y2][m2][d2]-y[p[y1][m1][d1][0]][p[y1][m1][d1][1]][p[y1][m1][d1][2]] << '\n';
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  pre();
  int _; cin >> _;
  while(_--) solve();
  return 0;
}
