class equals1
{
    int roll = 5;
    String name = "Ramesh";
    @Override
    public boolean equals(Object obj)
    {
        equals1 s = (equals1) obj;
        if(this.roll == s.roll && this.name.equals(s.name))
        {
            return true;
        }
        return false;
    }
    public static void main(String args[])
    {
        equals1 s1 = new equals1();
        equals1 s2 = new equals1();
        System.out.println(s1.equals(s2));
    }   
}