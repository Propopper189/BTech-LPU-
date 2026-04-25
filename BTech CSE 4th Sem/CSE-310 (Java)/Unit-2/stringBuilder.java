class stringBuilder
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.nextLine();

        // How to convert String to StringBuilder
        StringBuilder sb = new StringBuilder(s);

        // Reverse string builder
        sb.reverse();

        // How to convert StringBuilder to String
        String s1 = sb.toString();
        System.out.println(s1);

        StringBuilder sb1 = new StringBuilder("HelloWorld");
        sb1.insert(5, " ");
        System.out.println(sb1);

        StringBuilder sb2 = new StringBuilder("Hello World");
        sb2.delete(4, 8); // 4th index to 7th index
        System.out.println(sb2);
    }
}