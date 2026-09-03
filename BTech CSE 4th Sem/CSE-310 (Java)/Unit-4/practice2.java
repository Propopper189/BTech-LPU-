// Find the area of the circle using Lambda Expression ??
interface a
{
    void area(double r);
}
class practice2
{
    public static void main(String[] args) 
    {
        a obj = (r)->
        {
            System.out.printf("Area of the circle : %.2f", 3.141*r*r);
        };
        java.util.Scanner sc = new java.util.Scanner(System.in);
        System.out.println("Enter The Radius : ");
        double r = sc.nextDouble();
        obj.area(r);
    }
}