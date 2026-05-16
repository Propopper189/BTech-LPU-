class Gen<T extends Number>
{
    T val;
    Gen(T v)
    {
        val = v;
    }
    void show()
    {
        System.out.println(val.doubleValue());
    }
}
public class practice46 {
    public static void main(String args[])
    {
        Gen<Integer> a1 = new Gen<>(10);
        Gen<Double> a2 = new Gen<>(10.15);
        a1.show();
        a2.show();
    }
}
