using System;

class Code
{
    static void Main(string[] args)
    {
        int counter = 1;

        while (counter <= 100)
        {   
            if (counter == 100)
            {
                Console.Write(counter);
                break;
            }

            else
            {
                Console.Write(counter + "_");
                counter++;
            }
        }
    }
}