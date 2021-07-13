#include <bits/stdc++.h>
using namespace std;

const int N = 100004;
char S[N];
char W[N];
int pa[N<<1]; int find(int x){return pa[x]==x?x:pa[x]=find(pa[x]);}

void solve(){
  int n,x,p,q,nn,ii;
  scanf("%s", S); n = strlen(S); nn = (n<<1)+1;
  scanf("%d",&x);
  for(int i=0;i<=nn;++i) pa[i]=i;
  p=-x-x+1;q=x+x+1;
  for(int i=0;S[i];++i,p+=2,q+=2){
    if(S[i]=='0'){
      if(p>0)   pa[p]=0; // p => w[i-x]
      if(q<nn)  pa[q]=0; // q => w[i+x]
    }else{  //S[i]=1 case: one of p=1,p=1 hold.
      //p is half-processed, q is clear
      if(q<nn)               pa[q+1]=(p>0) ?find(p):0;
      if(p>0 && find(p+1)>0) pa[p+1]=(q<nn)?q:0; //NOT reach TRUE previously, thus settle with q0!
    }
  }
  for(int i=0,ii=0;i<n;++i){
    int p0 = find(++ii);
    int p1 = find(++ii);
    if(p0==0 && p1==0){cout << -1 << endl; return;} //cout << i << ':' << pp << '|' << pq << endl;
    W[i]=(p0==0)?'0':'1';
  }
  W[n]=0;
  cout << W << endl; //printf("%s\n",W);
}

int main(){
  int Case;
  cin >> Case;
  while(Case--) solve();
}
