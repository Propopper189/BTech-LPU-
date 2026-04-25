/*
Functional interface - interface class with single abstract method

We can override the interface abstract class without child class using lambda expression,

lambda expression is only used in functional interface 

interface A
{
    void lpu(int a, int b);
}
class B
{
    public static void main(String args[])
    {
        // Lambda Expresion
        // A obj = (a, b)->System.out.println(a + b);
        // obj.lpu(5, 6);

        Also : 

        A obj = (a, b)->
        {
            int result = a + b;
            System.out.println(result);
        };
        obj.lpu(5, 6);

        // Also

        interface A
        {
            int add(int a, int b);
        }
        class B
        {
            public static void main(String args[])
            {
                A obj = (a, b)->
                {
                    int result = a + b;
                    return result;
                };
                System.out.println(obj.add(5, 2));
            }
        }
    }
}
*/