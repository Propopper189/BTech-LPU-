// use of instanceOf
class a
{

}
class instanceOf1 extends a
{
    public static void main(String args[])
    {
        instanceOf1 obj = new instanceOf1();
        System.out.println(obj instanceof instanceOf1);
        System.out.println(obj instanceof a);
    }
}