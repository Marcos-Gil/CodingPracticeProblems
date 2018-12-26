/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers/0
 * Using Euclidean GCD Algorithm
 */
import java.util.Scanner;

public class GCD{

  /*
  Name: computeGCD
  Purpose: Compute GCD of two numbers using Euclidean GCD Algorithm
    In: int num1, int num2
    In/Out: N/A
    Out: int gcd
  */
  public static int computeGCD(int num1, int num2){

    if (num2 == 0){
        return num1;
    }

    return computeGCD(num2, num1 % num2);
  }

  public static void main(String[] args){

    int num1, num2 = -1;
    Scanner userInput = new Scanner(System.in);

    System.out.println("Computing the GCD of two numbers.");
    System.out.print("Please enter the first number: ");
    num1 = userInput.nextInt();
    System.out.print("Please enter the second number: ");
    num2 = userInput.nextInt();
    System.out.println("The GCD of " + num1 + " and " + num2 + " is " + computeGCD(num1, num2));
  }
}
