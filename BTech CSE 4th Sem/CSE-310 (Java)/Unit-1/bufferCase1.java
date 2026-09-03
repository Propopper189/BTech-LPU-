// Write a program to accept the age and name of a person
import java.util.*;
class bufferCase1
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.printf("Enter the age of the Person : ");
        int age = sc.nextInt();
        System.out.printf("Enter the name of the Person : ");
        sc.nextLine(); // Adding a buffer when accepting int then string; else not necessary (case 1)
        String name = sc.nextLine();
        System.out.println(age);
        System.out.println(name);
    }
}