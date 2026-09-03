class operators4
{
    public static void main(String args[])
    {
        // Increment & Decrement
        // a++ => a = a + 1; (first assign then increment).
        // ++a => (first increment then assign).
        // a-- => a = a - 1;
        // 6 + 7 - 7 + 5 + 5 + 7;
        int a = 5;
        int b = a++;
        System.out.println(a);
        System.out.println(b);

    }
}