#include <stdio.h>

int main() {
  for(int i = 1 ; i <= 20000000 ; ++ i){
    int x = rand();
    while( x ) putchar( x % 10 ) , x /= 10;
  }
  return 0;
}
