class objectClass
{
    // it is the child class of the object class (every class is a child of object class)
    // toString() -> present in object class
    // equals() -> present in object class

    int roll = 5;
    String name = "Aquib";

    @Override // the compiler will know that this method is parent's method, so compiler will take less time to execute the overriden line.
    public String toString()
    {
        return "Roll : " + roll + " | Name : " + name;
    }
    public static void main(String args[])
    {
        objectClass obj1 = new objectClass();
        System.out.println(obj1); // same as printing obj.toString()
        objectClass obj2 = new objectClass();
        System.out.println(obj2);
    }
}