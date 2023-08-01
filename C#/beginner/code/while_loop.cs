using System;

class Code
{
    static void Main(string[] args)
    {
        string name = "";

        while(name == "")
        {
            Console.Write("Enter your name: ");
            name = Console.ReadLine();
        }

        Console.WriteLine("Hello " + name);
    }
}