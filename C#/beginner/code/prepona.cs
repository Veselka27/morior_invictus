using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Strana a:");
        double a = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Strana b:");
        double b = Convert.ToDouble(Console.ReadLine());
        double vysledek = Math.Sqrt((a * a) + (b * b));
        Console.WriteLine("Vysledek je: " + vysledek);
    }
}