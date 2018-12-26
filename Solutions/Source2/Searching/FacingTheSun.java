/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/facing-the-sun/0
 */

import java.util.Scanner;
import java.util.Arrays;

public class FacingTheSun{

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
  Name: facingTheSun
  Purpose: Calculate the amount of buildings facing the sun
    In: int[] buildingHeights
    In/Out: N/A
    Out: int buildingsFacingSun
  */
  public static int facingTheSun(int[] buildingHeights){

    if (buildingHeights.length == 0){
      return -1;
    }

    int buildingsFacingSun = 1;
    int lastHeight = buildingHeights[0];

    for (int i = 1; i < buildingHeights.length; i++){

      if (buildingHeights[i] > lastHeight){

        buildingsFacingSun++;
        lastHeight = buildingHeights[i];
      }
    }

    return buildingsFacingSun;
  }

  public static void main(String[] args) {

    int[] userArray = getArray();
    int numOfBuildingsFacingSun = facingTheSun(userArray);

    if (numOfBuildingsFacingSun == -1){
      System.out.println("Empty array was entered");
    } else {
      System.out.println("The array is: " + Arrays.toString(userArray));
      System.out.println("There are " + numOfBuildingsFacingSun + " buildings receiving sunlight.");
    }
  }
}
