// Object class
/*
    Object class is father of all classes including user defined classes
    3 Important methods in Object Class
    toString();
    equals();
    hashCode();
*/

class a
{
    int marks = 10;
    String name = "Aquib";

    a()
    {

    }
    a(String name, int marks)
    {
        this.name = name;
        this.marks = marks;
    }
    @Override
    public String toString()
    {
        return marks + " " + name;
    }

    public boolean equals(Object o)
    {
        if(o instanceof a)
        {
            a s = (a)o;
            if(name.equals(s.name) && marks == s.marks)
            {
                return true;
            }
        }
        return false;
    }
}
public class practice16 {
    public static void main(String args[])
    {
        a obj1 = new a();
        a obj2 = new a("Jawaid", 20);
        System.out.println(obj1);
        System.out.println(obj2);
        System.out.println(obj1.equals(obj2));
        System.out.println(obj1 instanceof a);
    }
}
