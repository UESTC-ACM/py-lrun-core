#include <stdio.h>

int d[555555]; // test MLE

int main() {
  int a, b;
  int sum = 0;
  for(int k = 0 ; k < 555555 ; ++ k)
    d[k] = 772002 , sum += d[k] - k;  
  scanf("%d%d", &a, &b);
  printf("%d\n", a + b + sum );
  return 0;
}
