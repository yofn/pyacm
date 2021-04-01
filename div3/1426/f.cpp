#include <bits/stdc++.h>
using namespace std;
 
typedef unsigned long long ll;
 
ll N=1000000007;

ll solve(ll n){
  char c;
  ll _,a,ab,abc; _ = 1; a=ab=abc=0;
  //cout << n << '\n';
  getchar();
  for(ll i=1;i<=n;i++){
    c = getchar();
    switch(c){
      case 'a':
        a   += _;
        break;
      case 'b':
        ab  += a;
        break;
      case 'c':
        abc += ab;
        break;
      default:
        abc += (abc<<1)+ab;
        ab  += (ab <<1)+a ;
        a   += (a  <<1)+_ ;
        _   += (_  <<1);
    }
    //cout << c << '\t' << _ << '\t' << a << '\t' << ab << '\t' << abc << '\n';
    _   %=N;
    a   %=N;
    ab  %=N;
    abc %=N;
  }
  return abc;
}
 
int main(){
  ll n;
  scanf("%lld",&n);
  printf("%lld\n",solve(n));
}
