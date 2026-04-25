import java.awt.*;
class A extends Frame
{
    A()
    {
        setVisible(true);
        setSize(800, 600);
        setLayout(null);
        Label l1 = new Label("Name : ");
        Label l2 = new Label("Roll : ");
        TextField tf1 = new TextField();
        TextField tf2 = new TextField();
        Button b1 = new Button();
        l1.setBounds(70, 40, 80, 30); add(l1);
        tf1.setBounds(200, 40, 150, 30); add(tf1);
        l2.setBounds(70, 80, 80, 30); add(l2);
        tf2.setBounds(200, 80, 150, 30); add(tf2);
    }
}
class Frame1 
{
    // Write a program to design a frame
    public static void main(String args[])
    {
        A obj = new A();

    }
}
