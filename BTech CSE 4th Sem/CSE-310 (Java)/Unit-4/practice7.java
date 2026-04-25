// Accept 2 names from the user and check if both the names are same (ignore the cases and the spaces)
class practice7
{
    String name;
    practice7(String name)
    {
        this.name = name;
    }
    @Override
    public boolean equals(Object obj)
    {
        this.name = this.name.replace(" ", "");
        this.name = this.name.toLowerCase();
        practice7 ob = (practice7)obj;
        ob.name = ob.name.toLowerCase();
        ob.name = ob.name.replace(" ", "");
        if(this.name.equals(ob.name))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public static void main(String args[])
    {
        practice7 obj1 = new practice7("R a mesh");
        practice7 obj2 = new practice7("ra me sh");
        System.out.println(obj1.equals(obj2));
    }
}