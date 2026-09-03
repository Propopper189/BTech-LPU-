class practice9 // Outer class
{
    int x = 5; // Global variable inside outer class 
    class inner
    {
        int x = 7;
        void lpu()
        {
            System.out.println("LPU");
            System.out.println(x + practice9.this.x);  // Ans : 12 // to access outer class variable outer_class.this.variableName;
        }
    }
    public static void main(String[] args) 
    {
        practice9 obj = new practice9(); // Object of outer class
        practice9.inner ob = obj.new inner(); // Object of inner class
        ob.lpu();
    }
}