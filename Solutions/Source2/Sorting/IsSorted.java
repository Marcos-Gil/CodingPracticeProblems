/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted/0
 */
import java.util.Scanner;
import java.util.Arrays;

public class IsSorted{

  /*
  Name: checkIfSorted
  Purpose: Check if an array is sorted
    In: int[] array
    In/Out: N/A
    Out: N/A
  */
  public static boolean checkIfSorted(int[] array){

    // Stop 1 index short of end so when we do i + 1, we compare with last index and don't go out of bounds
    for (int i = 0; i < array.length - 1; i++){
      if (array[i] > array[i + 1]){ // If current value is larger than the next value, the array is not sorted
        return false;
      }
    }

    // If we go through entire array and integers are in order
    return true;
  }

  /*
  Name: getArrayFromUser
  Purpose: Get the values for the array to check from the user
    In: N/A
    In/Out: N/A
    Out: int[] userArrayAsInteger
  */
  public static int[] getArrayFromUser(){

    Scanner userInput = new Scanner(System.in);

    System.out.print("Enter integer values, each seperated by a space: ");
    String userArrayAsString = userInput.nextLine();

    // Splitting the array at each space
    String[] splitUserArrayOnSpace = userArrayAsString.split(" ");
    int[] userArrayAsInteger = new int[splitUserArrayOnSpace.length];

    // Converting each string value to an integer and storing it in an int array
    for (int i = 0; i < splitUserArrayOnSpace.length; i++){
      userArrayAsInteger[i] = Integer.parseInt(splitUserArrayOnSpace[i]);
    }

    return userArrayAsInteger;
  }

  /*
  Name: printResult
  Purpose: Tell the user if the array they entered was sorted or not
    In: boolean result, int[] array
    In/Out: N/A
    Out: N/A
  */
  public static void printResult(boolean result, int[] array){

    if (result == true){
      System.out.println("The array: " + Arrays.toString(array) + " is sorted in ascending order.");
    } else {
      System.out.println("The array: " + Arrays.toString(array) + " is sorted not in ascending order.");
    }
  }

  public static void main(String[] args) {

    int[] userArray = getArrayFromUser();
    boolean isSorted = checkIfSorted(userArray);
    printResult(isSorted, userArray);
  }
}
