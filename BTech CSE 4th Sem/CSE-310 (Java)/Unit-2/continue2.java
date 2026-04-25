class continue2
{
    public static void main(String args[])
    {
        int i;
        for(i = 1; i <= 10; i++)
        {
            System.out.println(i++);
            if(i > 3 && i < 7)
            {
                continue;
            }
            System.out.println(i);
        }
    }
}