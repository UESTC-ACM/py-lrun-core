import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
  static int a[] = new int[222];
  public static void main(String[] args) throws FileNotFoundException {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    for(int i = 0 ; i < n ; ++ i)
      a[i] = scanner.nextInt();
    int sum = 0;
    for(int i = 0 ; i < n ; ++ i)
      sum += a[i];
    System.out.println( sum );
    scanner.close();
  }
}