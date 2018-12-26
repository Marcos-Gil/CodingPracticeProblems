/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/reverse-an-array/0
 */
import java.util.Scanner;
import java.util.Arrays;

public class Reverse{

  /*
  Name: getArray
  Purpose: Get the length and values of the array that is to be reversed
    In: N/A
    In/Out: N/A
    Out: int[] arrayToReverse
  */
  public static int[] getArray(){

    int lengthOfArray = -1;
    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter the length of the array: ");
    lengthOfArray = userInput.nextInt();

    int[] arrayToReverse = new int[lengthOfArray];

    for (int i = 0; i < lengthOfArray; i++){
      System.out.print("Enter value " + (i + 1) + " of the array: ");
      arrayToReverse[i] = userInput.nextInt();
    }

    return arrayToReverse;
  }

  /*
  Name: printReverse
  Purpose: Printing the given array in reverse order
    In: int[] array
    In/Out: N/A
    Out: N/A
  */
  public static void printReverse(int[] array){

    // We could use Collections API and reverse the array and print that but question wants us to just print reverse without modifying order
    if (array.length < 1){
      System.out.println("There is nothing to reverse!");
    } else if (array.length == 1){
      System.out.println("Original: " + Arrays.toString(array));
      System.out.println("Reversed: [" + array[0] + "]");
    } else {
      System.out.println("Original: " + Arrays.toString(array));
      System.out.print("Reversed: ");
      System.out.print("[");

      for (int i = array.length - 1; i > 0; i--){
        System.out.print(array[i] + ", ");
      }

      System.out.println(array[0] + "]");
    }
  }

  public static void main(String[] args){

    int[] userArray = getArray();
    printReverse(userArray);
  }
}
