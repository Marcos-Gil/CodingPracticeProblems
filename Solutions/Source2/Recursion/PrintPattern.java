/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/print-pattern/0
 */
 import java.util.Scanner;

 public class PrintPattern{

   /*
   Name: getUserInput
   Purpose: Get the number that pattern will be based off of from the user
     In: N/A
     In/Out: N/A
     Out: int userChoice
  */
   public static int getUserInput(){

     Scanner userInput = new Scanner(System.in);
     System.out.print("Please enter a number to generate pattern from: ");
     int userChoice = userInput.nextInt();

     return userChoice;
   }

   /*
   Name: printPatternRecursively
   Purpose: Print the pattern based on user input using recursion
     In: int n
     In/Out: N/A
     Out: N/A
  */
   public static void printPatternRecursively(int n){

     if (n <= 0){
       System.out.print(n + " ");
     } else {
       System.out.print(n + " ");
       printPatternRecursively(n - 5);
       System.out.print(n + " ");
     }
   }

   public static void main(String[] args) {

     int userNum = getUserInput();
     printPatternRecursively(userNum);
     System.out.println();// start a new line for terminal
   }
 }
