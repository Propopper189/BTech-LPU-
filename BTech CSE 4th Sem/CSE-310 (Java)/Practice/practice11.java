class InitBlock
{
    {
        System.out.println("Executing before constructor of : " + getClass());
    }
    InitBlock()
    {
        System.out.println("Constructor Called!");
    }
}
public class practice11 
{
    public static void main(String args[])
    {
        new InitBlock();
        System.out.println("Main Function");
        new InitBlock();
    }
    static
    {
        System.out.println("Static Initializer Block");
    }
}
