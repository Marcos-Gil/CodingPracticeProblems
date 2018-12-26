/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/closest-number/0
 */
import java.util.Scanner;

public class ClosestNumber{

  /*
  Name: closestNum
  Purpose: Find number closest to N divisible by M
    In: int[] nums
    In/Out: N/A
    Out: int[] nums
  */
  public static int[] closestNum(int[] nums){

    // If N is negative, we will go down as per specification until we find a factor of M
    if (nums[0] < 0){

      for (int closest = nums[0] -1;; closest--){
        if (closest % nums[1] == 0){
          nums[2] = closest;
          return nums;
        }
      }
    } else {

      for (int closest = nums[0] -1; closest > 0; closest--){
        if (closest % nums[1] == 0){
          nums[2] = closest;
          return nums;
        }
      }
    }

    // If nothing found
    nums[2] = -99999;

    return nums;
  }

  /*
  Name: getUserValues
  Purpose: Get values for N and M from the user
    In: N/A
    In/Out: N/A
    Out: int[] userNums
  */
  public static int[] getUserValues(){

    int[] userNums = new int[3];
    Scanner userInput = new Scanner(System.in);
    System.out.print("Please enter the value of N: ");
    userNums[0] = userInput.nextInt();
    System.out.print("Please enter the value of M: ");
    userNums[1] = userInput.nextInt();

    return userNums;
  }

  /*
  Name: printAnswer
  Purpose: Printing answer to question
    In: N/A
    In/Out: N/A
    Out: N/A
  */
  public static void printAnswer(int[] answer){

    if (answer[2] == -99999){
      System.out.println("Not found!");
    } else {
      System.out.println("The closest number to " + answer[0] + " divisible by " + answer[1] + " is " + answer[2]);
    }
  }

  public static void main(String[] args){

    printAnswer(closestNum(getUserValues()));
  }
}
