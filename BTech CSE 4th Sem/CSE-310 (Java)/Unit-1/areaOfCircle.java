// Write a program to accept the radius of a circle and find //its area

import java.util.*;

class areaOfCircle
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the radius of the circle");
        double r = sc.nextDouble();
        System.out.printf("The area of the circle is : %.2f", r*r*3.14);
    }
}