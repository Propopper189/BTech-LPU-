class A
{
    void lpu1()
    {
        System.out.println("LPU 1");
    }
}

class inheritance3 extends A
{
    void lpu2()
    {
        System.out.println("LPU 2");
    }
    public static void main(String args[])
    {
        inheritance3 ObjInh3 = new inheritance3();
        ObjInh3.lpu1();
        ObjInh3.lpu2();
    }
}