import java.util.Scanner;

public class GreetingPt {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a time (0-24): ");
        int time = scanner.nextInt();

        System.out.print("Enter your name: ");
        String name = scanner.next();

        System.out.println((time < 12 ? "Good Morning, " : "Good Afternoon, ") + name + "!");
        
        scanner.close();
    }
}
