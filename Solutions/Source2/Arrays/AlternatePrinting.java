/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1
 */
import java.util.Scanner;
import java.util.Arrays;

public class AlternatePrinting{

  /*
  Name: getArray
  Purpose: Get the length and values of an array from the user
    In: N/A
    In/Out: N/A
    Out: int[] array
  */
  public static int[] getArray(){

    int lengthOfArray = -1;
    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter the length of the array: ");
    lengthOfArray = userInput.nextInt();

    int[] array = new int[lengthOfArray];

    for (int i = 0; i < lengthOfArray; i++){
      System.out.print("Enter value " + (i + 1) + " of the array: ");
      array[i] = userInput.nextInt();
    }

    return array;
  }

  /*
  Name: altPrint
  Purpose: Alternate way of printing out the array
    In: int[] arr
    In/Out: N/A
    Out: N/A
  */
  public static void altPrint(int[] arr){

    System.out.print("The alternate printing of " + Arrays.toString(arr) + " is: ");

    for (int i = 0; i < arr.length; i += 2){
      System.out.print(arr[i] + " ");
    }

    System.out.println();
  }

  public static void main(String[] args){
    altPrint(getArray());
  }
}
