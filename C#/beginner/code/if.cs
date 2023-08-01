using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter your age >> ");
        int age = Convert.ToInt32(Console.ReadLine());

        if(age >= 18)
        {
            Console.WriteLine("Good");
            Console.Write("Enter your name >> ");
            string name = Console.ReadLine();
            if(name == "")
            {
                Console.WriteLine("You must enter a name!");
            }
            
            else if(name == "sus")
            {
                Console.WriteLine("You need to get out ASAP");
            }

            else
            {
                Console.WriteLine("Hello " + name);
            }
        }

        else
        {
            Console.WriteLine("Get out!");
        }
    }
}