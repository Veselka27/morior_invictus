using System;

class Code
{
    static void Main(string[] args)
    {
        int first = 1;
        int last = 100;

        int count = 1;
        Random random = new Random();
        int correct_number = random.Next(first, last + 1);

        Console.Write("Try to guess a number between " + first + " and " + last + "\n>> ");
        int guess = Convert.ToInt32(Console.ReadLine());

        while (correct_number != guess)
        {
            if (correct_number < guess)
            {
                Console.Write("Lower\n>> ");
                guess = Convert.ToInt32(Console.ReadLine());
                count++;
            }

            else if (correct_number > guess)
            {
                Console.Write("Higher\n>> ");
                guess = Convert.ToInt32(Console.ReadLine());
                count++;
            }
        }

        Console.WriteLine("Correct! You won and got it in " + count + " tries!");
    }
}