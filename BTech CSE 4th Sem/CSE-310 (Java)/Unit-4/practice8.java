// Write a program to override equals to check whether both student having same name and same roll number or not
class practice8
{
    String name;
    int roll;
    practice8(String n, int roll)
    {
        this.name = n;
        this.roll = roll;
    }
    @Override
    public boolean equals(Object obj)
    {
        practice8 ob = (practice8) obj;
        this.name = this.name.replace(" ", "");
        this.name = this.name.toLowerCase();
        ob.name = ob.name.replace(" ", "");
        ob.name = ob.name.toLowerCase();
        if(this.name.equals(ob.name) && this.roll == ob.roll)
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
        practice8 s1 = new practice8("Aquib", 12);
        practice8 s2 = new practice8("A q u i b", 12);
        System.out.println(s1.equals(s2));
    }
}