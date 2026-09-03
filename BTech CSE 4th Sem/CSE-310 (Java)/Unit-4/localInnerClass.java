/* 
Local Inner Class 
    Note : if the inner class is present inside a method of outer class, 
           then that is called as local inner class
*/
class outer
{
    void display()
    {
        class inner // Local Inner Class
        {   
            void lpu()
            {
                System.out.println("I am from LPU");
            }
        }
        inner obj = new inner();
        obj.lpu();
    }
}
class localInnerClass
{
    public static void main(String args[])
    {
        outer obj = new outer();
        obj.display();
    }
}