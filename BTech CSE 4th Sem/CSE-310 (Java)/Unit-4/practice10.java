class outer
{
    void lpu()
    {
        System.out.println("Outer Class");
    }
    class inner
    {
        void lpu()
        {
            outer.this.lpu();
            System.out.println("Inner Class");
        }
    }
}
class practice10
{
    public static void main(String[] args) 
    {
        outer obj = new outer();
        outer.inner ob = obj.new inner();
        ob.lpu();
    }
}