import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws FileNotFoundException {
    Scanner scanner = new Scanner(new FileInputStream("data.out"));
    String line;
    while ((line = scanner.nextLine()) != null) {
      System.out.println(line);
    }
    scanner.close();
  }
}