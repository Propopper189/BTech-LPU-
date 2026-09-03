public class practice12 {
    public static void AllFunc(String s)
    {
        System.out.println(s);
        System.out.println(s.equals("Hello"));
        System.out.println(s.equalsIgnoreCase("hello"));
        System.out.println(s.contains("ello"));
        System.out.println(s.toUpperCase());
        System.out.println(s.toLowerCase());
        System.out.println(s.replace('l', 'x'));
        System.out.println(s.substring(1, 4));
    }
    public static void main(String args[])
    {
        String s = "Hello";
        AllFunc(s);
        StringBuilder sb = new StringBuilder(s);
        sb.append(" Aquib");
        System.out.println(sb);
        sb.insert(0, "Hi ");
        System.out.println(sb);
        sb.delete(0, 3);
        System.out.println(sb);
        sb.reverse();
        System.out.println(sb);
    }
}