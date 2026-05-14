public class practice3 {
    static void display(int a, int b)
    {
        int max = (a > b) ? a : b;
        System.out.println("Max : " + max);
    }
    public static void main(String args[])
    {
        practice3.display(8, 10);

        int a = 2;
        switch(a)
        {
            case 1:
                System.out.println("Mon");
                break;
            case 2:
                System.out.println("Tues");
                break;
            default:
                System.out.println("Default");
                break;
        }
    }
}
