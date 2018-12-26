/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/armstrong-numbers/0
 */
import java.util.Scanner;
import java.lang.Math;

public class ArmstrongNumbers{

  /*
  Name: checkArmstrong
  Purpose: Check if the use provided number is an armstrong number
    In: int num
    In/Out: N/A
    Out: N/A
  */
  public static void checkArmstrong(int num){

    int initalValue = num;
    int[] digitValues = new int[3];
    int i = 0;

    // Getting the individual digits
    while (num > 0){
      digitValues[i] = num % 10;
      i++;
      num = num/10;
    }

    double sumOfCubes = 0;

    for (int j = 0; j < digitValues.length; j++){

      sumOfCubes = sumOfCubes + Math.pow(digitValues[j], 3);
    }

    if (sumOfCubes == initalValue){
      System.out.println(initalValue + " is an Armstrong Number!");
    } else {
      System.out.println(initalValue + " is not an Armstrong Number!");
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
    System.out.print("Please enter the potential 3-digit Armstrong Number: ");
    int userNum = userInput.nextInt();

    return userNum;
  }

  public static void main(String[] args){

    checkArmstrong(getUserValue());
  }
}
