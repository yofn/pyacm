#include <bits/stdc++.h>
#define bug(x) cout<<#x<<" is "<<x<<endl

using namespace std;
const int N=1e6+2;
char a[N],s[N*2];
int  p[N*2],ans,cnt=0,n;
//OOT:out of template
char o[N];
int  hp,tp,oi,on;

void rebuild(){
  s[0]='$';s[1]='#';
  n=strlen(a);
  for(int i=0;i<n;++i)
    s[2*i+2]=a[i],s[2*i+3]='#';
  s[n=n*2+2]=0;
}
int Manacher(){
  int mx=0,ml,i;
  int ans=1;
  hp=tp=1; //OOT
  for(i=0;i<n;++i){
    p[i]=(mx<=i)?1:min(p[mx-i+ml],mx-i);
    while(s[i-p[i]]==s[i+p[i]])p[i]++;
    if(i+p[i]>mx)mx=i+p[i],ml=i-p[i];
    ans=max(ans,p[i]-1);
    if(ml==0) hp=max(hp,p[i]-1);//OOT
    if(mx==n) tp=max(tp,p[i]-1);//OOT
  }
  return ans;
}
int bitrim(){
  int i=0; 
  int j=on-1;
  while(i<j && o[i]==o[j]){i++;j--;}
  strcpy(a,o+i);
  a[j+1-i]=0;
  oi=i;
}

//OOT
int s2h(){
  int il=oi+hp;       //[l,r)
  int ir=il+oi;
  int j =on-ir;
  for(int i=il;i<ir;++i) o[i]=o[i+j];
  o[ir]=0;
  return 0;
}
int s2t(){
  int ir=on-oi-tp;  //[l,r)
  int il=ir-oi;
  int j =il;
  for(int i=ir-1;i>=il;--i) o[i]=o[i-j];
  return max(j,0);
}

int main(){
  int i;
  cin >> i;
  while(scanf("%s",o)!=EOF){
    on = strlen(o); //OOT
    bitrim();       //OOT
    if(!strlen(a)){puts(o);continue;}
    rebuild();
    Manacher();//printf("%d\n",Manacher());
    puts(o+(hp>tp?s2h():s2t())); //OOT
  }
}
