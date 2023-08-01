using System;

class Program
{
    static void Main()
    {
        int x; //declaration
        x = 5; //initialization

        int y = 10; //combined

        Console.WriteLine("The value y is: " + y + "\nAnd the value x is: " + x);

        int age = 23;
        string name = "Filip";

        Console.WriteLine(name + " is " + age + " years old");

        int k = x + y;
        Console.WriteLine("x + y = " +k);

        int i = y / x;
        Console.WriteLine("y / x = " + i);

        int o = y * x;
        Console.WriteLine("y * x = " + o);

        double height = 172.5; // decimal\
        Console.WriteLine("height: " + height);

    }
}