/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/searching-a-number/0
 */
import java.util.Scanner;
import java.util.Arrays;

public class LinearSearch{

  /*
  Name: getArray
  Purpose: Get the array to search
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
  Name: searchArray
  Purpose: Search array for value
    In: int[] array, int value
    In/Out: N/A
    Out: int index
  */
  public static int searchArray(int[] array, int value){

    // Iterate through array, if found it will return the first index value was found at. If never found we will return -1
    for (int i = 0; i < array.length; i++){
      if (array[i] == value){
        return i;
      }
    }

    return -1;
  }

  /*
  Name: getValue
  Purpose: Get value to search for in the array
    In: N/A
    In/Out: N/A
    Out: int value
  */
  public static int getValue(){

    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter the value to search for in the array: ");
    int value = userInput.nextInt();

    return value;
  }

  public static void main(String[] args) {

    int[] userArray = getArray();
    int valueToFind = getValue();
    int result = searchArray(userArray, valueToFind);

    if (result == -1){
      System.out.println("Sorry, " + valueToFind + " is not in the array " + Arrays.toString(userArray));
    } else {
      System.out.println(valueToFind + " is located at index " + result + " in the array " + Arrays.toString(userArray));
    }
  }
}
