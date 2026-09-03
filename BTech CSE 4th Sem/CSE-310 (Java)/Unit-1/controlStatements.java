import java.util.*;
class controlStatements
{
    public static void main(String args[])
    {
        // Control Structure / Control Statement
        // -> Controlling the flow of execution of program body.
        
        // 4 Types of control structure
        // -------------------------------
        // 1. Sequential control structure (normal sequential execution without control)
        // 2. Selection control structure (if else)
        /*
        1.    if(condition)
            {
            }
            else
            {
            }
        2. if(condition)
            {
            }
        3. if(condition)
            {
            }
            else if(condition)
            {
            }
            else if(condition)
            {
            }
        4. if(condition)
            {
            }
            else if(condition)
            {
            }
            else
            {
            }
        5. if(condition)
            {
                if(condition)
                {
                    if(condition)
                    {
                    }
                    else
                    {
                    }
                }
            }
            else
            {
            }
        */
        // 3. Iteration control structure (loops)
        // 4. Decission contol structure (Switch Case)

        // Write a program to check whether a number is +ve or negative
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        if(a > 0)
        {
            System.out.println("Positive");
        }
        else if(a == 0)
        {
            System.out.println("Zero");
        }
        else
        {
            System.out.println("Negative");
        }
    }
}