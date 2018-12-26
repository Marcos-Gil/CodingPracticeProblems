/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/print-table/0
 */
import java.util.Scanner;

public class PrintTable{

  /*
  Name: printTable
  Purpose: Print table of N up to 10
    In: int num
    In/Out: N/A
    Out: N/A
  */
  public static void printTable(int num){

    for (int i = 1; i < 11; i++){
      System.out.print(num * i + " ");
    }
  }

  /*
  Name: getUserValue
  Purpose: Get value for N from the user
    In: N/A
    In/Out: N/A
    Out: int userNum
  */
  public static int getUserValue(){

    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter the value to create table from: ");
    int userNum = userInput.nextInt();

    return userNum;
  }

  public static void main(String[] args){

    int userNum = getUserValue();
    printTable(userNum);
  }
}
