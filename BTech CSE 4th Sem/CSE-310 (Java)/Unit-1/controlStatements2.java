import java.util.*;
class controlStatements2
{
    public static void main(String args[])
    {
        // Write a program to accept a character and check whether it is a digit or alphabet.
        Scanner sc = new Scanner(System.in);
        char a = sc.next().charAt(0);
        // isDigit(a)
        if((a >= 'A' && a <= 'Z') || (a >= 'a' && a <= 'z'))
        {
            System.out.println("Alphabet");
        }
        else if(a >= '0' && a <= '9')
        {
            System.out.println("Number");
        }
    }   
}