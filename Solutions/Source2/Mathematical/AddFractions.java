/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/add-two-fractions/1
 */
import java.util.Scanner;

public class AddFractions{

  /*
  Name: addFraction
  Purpose: Print out final fraction
    In: int[] fractionArray
    In/Out: N/A
    Out: int[] finalFraction
  */
  public static int[] addFraction(int[] fractionArray){

    int[] finalFraction = new int[2]; //[0] = numerator, [1] = denominator

    System.out.println("Adding fractions:");
    System.out.println(fractionArray[0] + "   " + fractionArray[2]);
    System.out.println("- + -");
    System.out.println(fractionArray[1] + "   " + fractionArray[3]);

    // if the denominators are the same, add numerators and keep 1 denominator
    if (fractionArray[1] == fractionArray[3]){
      finalFraction[0] = fractionArray[0] + fractionArray[2];
      finalFraction[1] = fractionArray[1];
      return finalFraction;
    } else { // denominators not the same
      finalFraction[0] = (fractionArray[0] * fractionArray[3]) + (fractionArray[2] * fractionArray[1]);
      finalFraction[1] = fractionArray[1] * fractionArray[3];
      return finalFraction;
    }
  }

  /*
  Name: getFractions
  Purpose: Get the fractions from user that they want to add
    In: N/A
    In/Out: N/A
    Out: int[] fractionValues
  */
  public static int[] getFractions(){

    int[] fractionValues = new int[4];

    // Could use ArrayList here and do fractionValues.add instead of hard coding indices
    Scanner userInput = new Scanner(System.in);
    System.out.println("Please enter numerator of first fraction");
    fractionValues[0] = userInput.nextInt();
    System.out.println("Please enter denominator of first fraction");
    fractionValues[1] = userInput.nextInt();
    System.out.println("Please enter numerator of second fraction");
    fractionValues[2] = userInput.nextInt();
    System.out.println("Please enter denominator of second fraction");
    fractionValues[3] = userInput.nextInt();

    return fractionValues;
  }

  /*
  Name: printFraction
  Purpose: Print out final fraction
    In: int[] finalFraction
    In/Out: N/A
    Out: N/A
  */
  public static void printFraction(int[] finalFraction){

    System.out.println("The solution is:");
    System.out.println(finalFraction[0]);
    System.out.println("-");
    System.out.println(finalFraction[1]);
  }

  public static void main(String[] args){

    printFraction(addFraction(getFractions()));
  }
}
