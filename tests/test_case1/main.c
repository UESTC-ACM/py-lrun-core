#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
  int a, b;

  pid_t pid = fork();
  if (pid == 0) {
    scanf("%d%d", &a, &b);
    printf("%d\n", a + b);
  } else {
    wait(0);
  }

  return 0;
}
