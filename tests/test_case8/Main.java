import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
  static int s[] = new int[10000000];
  public static void main(String[] args) throws FileNotFoundException {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt() , b = scanner.nextInt();
    for(int i = 0 ; i < 10000000 ; ++ i)
      s[i] = 772002 + i * i * i * i * i;
    int sum = 0;
    for(int i = 0 ; i < 10000000 ; ++ i)
      sum += s[i];
    System.out.println( a + b + sum );
  }
}