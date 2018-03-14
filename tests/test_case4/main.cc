#include <bits/stdc++.h>

int n , a[555];

int main() {
  scanf( "%d" , & n );
  for(int i = 1 ; i <= n ; ++ i)
    scanf( "%d" , a + i );
  int sum = 0;
  printf( "%d\n" , std::accumulate( a + 1 , a + n + 1 , 0 ) );
  return 0;
}
