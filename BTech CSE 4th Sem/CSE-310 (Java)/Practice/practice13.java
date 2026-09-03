// Inheritance
class Animal
{
    void sound()
    {
        System.out.println("The Dog Is Making Sound");
    }
}

class Dog extends Animal
{
    void bark()
    {
        System.out.println("The Dog Is Barking");
    }
}

public class practice13 {
    public static void main(String args[])
    {
        Dog d1 = new Dog();
        d1.sound();
        d1.bark();
    }
}
