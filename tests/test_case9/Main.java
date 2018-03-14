import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws Exception {
    Scanner scanner = new Scanner( System.in );
    int a = scanner.nextInt() , b = scanner.nextInt();
    System.out.println( a + b );
    int sum = 0;
    for(int i = 1 ; i <= 10000000000000L ; ++ i)
      sum = sum + i * i * i * i;
    System.out.println( sum );
  }
}