using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("What is your name?");
        string name = Console.ReadLine();
        Console.WriteLine("What is your age?");
        string age = Console.ReadLine();
        Console.WriteLine("Hello " + name + " you are " + age + " years old");
    }
}