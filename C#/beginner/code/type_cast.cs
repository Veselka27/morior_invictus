using System;

class Program
{
    static void Main(string[] args)
    {
        double a = 3.14;
        int b = Convert.ToInt32(a);
        
        Console.WriteLine(b);
        Console.WriteLine(a.GetType());

        int d = 300;
        double f = Convert.ToDouble(d) + 0.1;
        
        Console.WriteLine(f);

        int i = 20;
        string s = Convert.ToString(i) + " lol";

        Console.WriteLine(s);

        string y = "true";
        bool x = Convert.ToBoolean(y);

        Console.WriteLine(x);
    }
}