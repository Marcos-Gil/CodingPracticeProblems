/**
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1
 */
public class PrintThePattern {

  public static void main(String[] args) {
    int count = 5; // User input, can add scanner here and get any value n
    int temp2 = count;
    int temp3 = count;

    while (temp3 != 0){

      int temp = count;

      while(temp != 0){

        for (int i = 0; i < temp2; i++){// loop that prints out the number as many times as the current value of n is
          System.out.print(temp);
        }

        System.out.println();
        temp--;//decresing value of n for current loop iteration so we can bring 5, 4, 3, 2, 1
      }
      temp2--;//decreasing the amount of times that we will print n in the for loop
      temp3--;//variable for controlling the outer loop
    }
  }
}
