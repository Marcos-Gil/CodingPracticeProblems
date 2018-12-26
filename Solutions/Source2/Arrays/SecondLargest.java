/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/second-largest/0
 */
import java.util.Scanner;
import java.util.Arrays;

public class SecondLargest{

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
  Name: secondLargest
  Purpose: Find second largest value in the array
    In: int[] arr
    In/Out: N/A
    Out: int secondLargest
  */
  public static int secondLargest(int[] arr){

    int largest = Integer.MIN_VALUE;
    int secondLargest = Integer.MIN_VALUE;

    for (int i = 0; i < arr.length; i++){
      if (arr[i] > largest){
        secondLargest = largest;
        largest = arr[i];
      } else if (arr[i] > secondLargest && arr[i] != largest){
        secondLargest = arr[i];
      }
    }

    return secondLargest;
  }

  /*
  Name: printResult
  Purpose: Print second largest value
    In: int[] arr,
        int answer
    In/Out: N/A
    Out: N/A
  */
  public static void printResult(int answer, int[] arr){

    if (arr.length < 2){
      System.out.println("Less than two values entered.");
    } else {
      System.out.println("The second largest number in the array " + Arrays.toString(arr) + " is: " + answer);
    }
  }

  public static void main(String[] args){

    int[] values = getArray();
    printResult(secondLargest(values),values);
  }
}
