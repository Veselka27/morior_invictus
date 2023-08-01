using System;

class Code
{
    static void Main(string[] args)
    {
        string FullName = "Filip Vesely";

        //FullName = FullName.ToUpper();
        FullName = FullName.ToLower();
        string UserName = FullName.Replace(" ", "_").Insert(0, "@");

        Console.WriteLine(UserName);
        Console.WriteLine(UserName.Length);

        string FirstName = FullName.Substring(0, 5);
        string LastName = FullName.Substring(6, 6);

        Console.WriteLine(FirstName);
        Console.WriteLine(LastName);
    }
}