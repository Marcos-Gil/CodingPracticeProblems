/*
 * By: Marcos Gil
 * Solution for this practice problem
 * https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1
 * based on this functionality https://docs.oracle.com/javase/7/docs/api/java/util/Stack.html
 */
import java.util.Scanner;
import java.util.Arrays;

public class StackWithArray{

  private static int numOfElements = 0;
  private static int MAX_SIZE = 5;

  /*
  Name: createStack
  Purpose: Make an array that will be used to simulate the stack
    In: N/A
    In/Out: N/A
    Out: int[] array
  */
  public static int[] createStack(){
    int[] array = new int[MAX_SIZE];
    System.out.println("A new stack has been created with a max capacity of " + MAX_SIZE);
    return array;
  }

  /*
  Name: isEmpty
  Purpose: Check if stack is empty
    In: N/A
    In/Out: N/A
    Out: boolean
  */
  public static boolean isEmpty(){

    if (numOfElements == 0){
      return true;
    } else {
      return false;
    }
  }

  /*
  Name: pop
  Purpose: Pop element at the top of the stack
    In: int[] stack
    In/Out: N/A
    Out: int poppedItem
  */
  public static int pop(int[] stack){

    if (numOfElements == 0){
      return -1;
    } else {
      int poppedItem = stack[numOfElements - 1];
      numOfElements--;
      return poppedItem;
    }
  }

  /*
  Name: push
  Purpose: Check if an array is sorted
    In: int[] stack, int n
    In/Out: N/A
    Out: N/A
  */
  public static void push(int[] stack, int n){

    if (numOfElements == MAX_SIZE){
      System.out.println("Sorry, the stack is full! Cannot push another item.");
      return;
    } else {
      stack[numOfElements] = n;
      numOfElements++;
    }
  }

  /*
  Name: peek
  Purpose: Peek element at the top of the stack
    In: int[] stack
    In/Out: N/A
    Out: N/A
  */
  public static void peek(int[] stack){
    if (numOfElements == 0){
      System.out.println("There is nothing to peek!");
    } else {
      System.out.println("The top of the stack is currently " + stack[numOfElements - 1]);
    }
  }

  /*
  Name: printStack
  Purpose: Print out the stack
    In: int[] stack
    In/Out: N/A
    Out: N/A
  */
  public static void printStack(int[] stack){

    if (numOfElements == 0){
      System.out.println("[]");
    } else if (numOfElements == 1){
      System.out.println("["+ stack[0] +"]");
    } else {

      System.out.print("[");

      for (int i = 0; i < numOfElements - 1; i++){
        System.out.print(stack[i] +", ");
      }

      System.out.println(stack[numOfElements - 1] + "]");
    }
  }

  /*
  Name: search
  Purpose: Check if element is in the stack
    In: int[] stack, int n
    In/Out: N/A
    Out: N/A
  */
  public static void search(int[] stack, int n){

    boolean found = false;

    for (int i = 0; i < numOfElements; i++){

      if (n == stack[i]){ // if item is found

        found = true;

        if (i == numOfElements - 1){ // if it was found at the top or somewhere else
          System.out.println("Found! " + n + " is at the top of stack.");
        } else {
          System.out.println("Found! " + n + " is " + (numOfElements - i - 1) + " position(s) away from the top of the stack.");
        }
      }
    }

    if (!found){
      System.out.println(n + " is not in the stack.");
    }
  }

  /*
  Name: stackTests
  Purpose: Testing all the methods on the stack
    In: int[] stack
    In/Out: N/A
    Out: N/A
  */
  public static void stackTests(int[] stack){

    /* TESTS for empty, peek, pop, push, search*/
    System.out.print("Testing empty() on: ");
    printStack(stack);
    System.out.println(isEmpty());
    System.out.println("Testing pop()");
    int pop = pop(stack);
    if (pop == -1){
      System.out.println("There is nothing to pop! Stack is currently");
    } else {
      System.out.println("Popped "+ pop + " from the stack. The stack now is: ");
    }
    printStack(stack);
    System.out.println("Testing peek()");
    peek(stack);
    System.out.println("Testing push(1)");
    push(stack, 1);
    printStack(stack);
    System.out.println("Testing push(3)");
    push(stack, 3);
    printStack(stack);
    System.out.println("Testing push(6)");
    push(stack, 6);
    printStack(stack);
    System.out.println("Testing pop()");
    pop = pop(stack);
    if (pop == -1){
      System.out.println("There is nothing to pop! Stack is currently");
    } else {
      System.out.println("Popped "+ pop + " from the stack. The stack now is: ");
    }
    printStack(stack);
    System.out.println("Testing pop()");
    pop = pop(stack);
    if (pop == -1){
      System.out.println("There is nothing to pop! Stack is currently");
    } else {
      System.out.println("Popped "+ pop + " from the stack. The stack now is: ");
    }
    printStack(stack);
    System.out.println("Testing push(6)");
    push(stack, 6);
    printStack(stack);
    System.out.println("Testing push(7)");
    push(stack, 7);
    printStack(stack);
    System.out.println("Testing push(2)");
    push(stack, 2);
    printStack(stack);
    System.out.println("Testing peek()");
    peek(stack);
    System.out.println("Testing search(2)");
    search(stack, 2);
    printStack(stack);
    System.out.println("Testing search(7)");
    search(stack, 7);
    printStack(stack);
    System.out.println("Testing search(6)");
    search(stack, 6);
    printStack(stack);
    System.out.println("Testing push(8)");
    push(stack, 8);
    printStack(stack);
    System.out.println("Testing push(9)");
    push(stack, 9);
    printStack(stack);
  }

  public static void main(String[] args){

    int[] stack = createStack();
    stackTests(stack);
  }
}
