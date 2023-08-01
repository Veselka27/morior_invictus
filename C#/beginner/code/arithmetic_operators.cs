using System;

class Program
{
    static void Main(string[] args)
    {   
        
        /* +=
         * -=
         * *=
         * /=
         * % 
         */ 


        int coockies = 5;

        //coockies = coockies + 1
        //coockies += 1
        coockies++;


        Console.WriteLine(coockies);

        int friends = 4;

        //friends = friends - 1
        // friends -= 1
        friends--;

        Console.WriteLine(friends);

        int bikes = 10;

        int remainder = bikes % 3; // deleni se zbytkem

        Console.WriteLine(remainder);
    }
}