class string1
{
    public static void main(String args[])
    {
        // String : immutable in nature (can't be modified)
        String s1 = "lpu";
        // String s2 = new String("lpu");
        
        s1 = s1.concat(" university"); // forcefully modfying
        // s1.concat(" university"); (wont work)
        System.out.println(s1);

        String s2 = "I am from LPU";
        System.out.println("s2 size : " + s2.length());
        System.out.println("s2[2] : " + s2.charAt(2)); // a
        System.out.println("Index of 'f' : " + s2.indexOf('f'));
        System.out.println("Substring from 3rd Index : " + s2.substring(3));
        System.out.println("Substring from 3 to 7 : " + s2.substring(3, 8)); // print 3rd to 7th index
        s2 = s2.replace("am", "was"); 
        System.out.println("After forcefully replacing string : " + s2);    
        // Write a program to split the number of words in a string
        String s3 = "i am from lpu";
        String words [] = s3.split(" ");
        System.out.println("Number of words : " + words.length);
        // StringBuilder : mutable (can be modified)
        StringBuilder sb = new StringBuilder("LPU");
        sb.append(" University");
        System.out.println(sb);
    }
}