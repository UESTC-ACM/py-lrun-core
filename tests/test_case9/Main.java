import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws Exception {
    Scanner scanner = new Scanner( System.in );
    int a = scanner.nextInt() , b = scanner.nextInt();
    System.out.println( a + b );
    long sum = 0;
    for(int i = 1 ; i <= 10000000000000L ; ++ i){
      sum = sum + ( 1L * i * i % 10000000 * i % 10000000 * i % 10000000 );
      if( sum >= 10000000 ) sum -= 10000000;
    }
    System.out.println( sum );
  }
}