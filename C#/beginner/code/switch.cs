using System;

class Code
{
    static void Main(string[] args)
    {
        // efficient alternative to many else if statements
        
        Console.Write("Enter a day >> ");
        string day = Console.ReadLine().ToLower();
        string answer = "Its " + day + "!";

        switch(day)
        {
            case "monday":
                Console.WriteLine(answer);
                break;
            
            case "tuesday":
                Console.WriteLine(answer);
                break;
            
            case "wednesday":
                Console.WriteLine(answer);
                break;
            
            default:
                Console.WriteLine(day + " is not a day!");
                break;
            
            
        }
    }
}