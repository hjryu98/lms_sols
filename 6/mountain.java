import java.util.Scanner;
public class mountain{
  static int a;
  
  public static void recur(int n){
    if(n <= 1){
      System.out.print(n);
      return;
    }
    recur(n - 1);
    System.out.print(n);
    recur(n - 1);
  }
  
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    a = sc.nextInt();
    
    recur(a);
    sc.close();
  }
}
