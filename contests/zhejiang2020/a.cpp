#include<cstdio>
int  f[10000][13][32];  //prefix sum..
int is[10000][13][32];
int i,j,lim,k,sum,A,B,C,D,E,F,ans,Case;

inline int mdays(int y, int m){
  if(m==2)  return 28 + (y%400==0 || (y%4==0 && y%100));
  if(m==4||m==6||m==9||m==11)  return 30;
  return 31;
}

void pre(){
  sum = 0;
  for(i=2000;i<=9999;i++) for(j=1;j<=12;j++){
    lim = mdays(i,j);
    for(int k=1;k<=lim;k++){
      if(i/10==202||i%1000==202||(i%10==2&&j==2)||(j%10==2&&k==2)){
        is[i][j][k]=1;
        sum++;
      }
      f[i][j][k] = sum;
    }
  }
}

int main(){
  pre();
  scanf("%d",&Case);
  while(Case--){
    scanf("%d%d%d%d%d%d",&A,&B,&C,&D,&E,&F);
    ans = f[D][E][F]-f[A][B][C]+is[A][B][C];
    printf("%d\n",ans);
  }
}

