// Write a program to add 2 Numbers (take input from user)

import java.util.*;

class addTwoNumUserInput
{
    public static void main(String args[])
    {
        // Create an object of the Scanner class
        // className objName = new className(argument if any);
        Scanner sc = new Scanner(System.in);
        // System.in -> means i have to accept input from systems input device
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = a + b;
        System.out.println("The output is : " + c);
    }
}