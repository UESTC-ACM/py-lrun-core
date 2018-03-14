#include <stdio.h>

int n , a[662];

int main() {
  scanf( "%d" , & n );
  for(int i = 1 ; i <= n ; ++ i)
    scanf( "%d" , a + i );
  int sum = 0;
  for(int i = 1 ; i <= n ; ++ i)
    sum += a[i];
  printf( "%d\n" , sum );
  return 0;
}
