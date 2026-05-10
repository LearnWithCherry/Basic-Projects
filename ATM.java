import java.util.Scanner;
public class ATM {
   private double balance;
   public ATM() {
       this.balance = 0.0;
   }
   public void checkBalance() {
       System.out.println("Your current balance is: $" + balance);
   }
   public void deposit(double amount) {
       if (amount > 0) {
           balance += amount;
           System.out.println("Successfully deposited: $" + amount);
       } else {
           System.out.println("Invalid deposit amount.");
       }
   }
   public void withdraw(double amount) {
       if (amount > 0 && amount <= balance) {
           balance -= amount;
           System.out.println("Successfully withdrew: $" + amount);
       } else {
           System.out.println("Insufficient balance or invalid amount.");
       }
   }
   public static void main(String[] args) {
       ATM atm = new ATM();
       Scanner scanner = new Scanner(System.in);
       int choice;
       do {
           System.out.println("\nATM Menu:");
           System.out.println("1. Check Balance");
           System.out.println("2. Deposit Money");
           System.out.println("3. Withdraw Money");
           System.out.println("4. Exit");
           System.out.print("Enter your choice: ");
           choice = scanner.nextInt();
           switch (choice) {
               case 1:
                   atm.checkBalance();
                   break;
               case 2:
                   System.out.print("Enter deposit amount: ");
                   double depositAmount = scanner.nextDouble();
                   atm.deposit(depositAmount);
                   break;
               case 3:
                   System.out.print("Enter withdrawal amount: ");
                   double withdrawAmount = scanner.nextDouble();
                   atm.withdraw(withdrawAmount);
                   break;
               case 4:
                   System.out.println("Thank you for using the ATM!");
                   break;
               default:
                   System.out.println("Invalid choice. Please try again.");
           }
       } while (choice != 4);
       scanner.close();
   }
}