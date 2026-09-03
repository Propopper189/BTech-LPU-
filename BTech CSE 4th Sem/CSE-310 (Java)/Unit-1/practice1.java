
import java.util.*;

// Write a program to accept 2 student's marks and name and print the name who is having the highest marks
class practice1
{
    public static void main(String args[])
    {
        int m1;
        int m2;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the name for first student : ");
        String name1 = sc.nextLine();
        System.out.println("Enter the name for second student : ");
        String name2 = sc.nextLine();
        System.out.println("Enter the marks for first student : ");
        m1 = sc.nextInt();
        System.out.println("Enter the marks for second student : ");
        m2 = sc.nextInt();
        if(m1 > m2)
        {
            System.out.print(name1 + " is having higher score : " + m1);
        }
        else
        {
            System.out.print(name2 + " is having higher score : " + m2);
        }
    }
}