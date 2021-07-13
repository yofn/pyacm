#include <bits/stdc++.h>
using namespace std;

const int N = 1001005;
char A[N];
char B[N];
const int M = 1002;
bool V[M];
#define bug(x) cout<<#x<<" is "<<x<<endl

void solve(){
  int n;
  scanf("%d",&n);
  for(int i=0,ao=0;i<n;i++,ao+=n+1) scanf("%s",A+ao);
  getchar();
  for(int i=0,ao=0;i<n;i++,ao+=n+1) scanf("%s",B+ao);
  for(int i=0;i<n;++i) V[i]=(A[i]!=B[i]); //V means flip
  for(int i=1,ao=n+1;i<n;i++,ao+=2){
    bool flip = V[0]^(A[ao]!=B[ao]);      //if 1(diff),flip=~V[0], if 0(same),flip=V[0]
    for(int j=1;j<n;j++){
      ao++;
      if((A[ao]!=B[ao])!=(V[j]^flip)){cout<<"NO"<<endl;return;}
    }
  }
  cout<<"YES"<<endl;return;
}

int main(){
  int Case;
  cin >> Case;
  while(Case--) solve();
}
