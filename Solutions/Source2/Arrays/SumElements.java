/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/sum-of-array-elements/0
 */
import java.util.Scanner;

public class SumElements{

  /*
  Name: getArray
  Purpose: Get the length and values of the array that is to be summed
    In: N/A
    In/Out: N/A
    Out: int[] arrayToSum
  */
  public static int[] getArray(){

    int lengthOfArray = -1;
    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter the length of the array: ");
    lengthOfArray = userInput.nextInt();

    int[] arrayToSum = new int[lengthOfArray];

    for (int i = 0; i < lengthOfArray; i++){
      System.out.print("Enter value " + (i + 1) + " of the array: ");
      arrayToSum[i] = userInput.nextInt();
    }

    return arrayToSum;
  }

  /*
  Name: sumArray
  Purpose: Sum the values of the array
    In: int[] array
    In/Out: N/A
    Out: int totalSum
  */
  public static int sumArray(int[] array){

    int totalSum = 0;

    for (int i = 0; i < array.length; i++){
      totalSum = totalSum + array[i];
    }

    return totalSum;
  }

  /*
  Name: printResult
  Purpose: Print the result of the sum
    In: int result
    In/Out: N/A
    Out: N/A
  */
  public static void printResult(int result){

    System.out.println("The total sum of the array elements is " + result);
  }

  public static void main(String[] args){

    printResult(sumArray(getArray()));
  }
}
