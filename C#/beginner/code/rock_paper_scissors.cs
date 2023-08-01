using System;

class Code{

    static void Main(string[] args){

        Random random = new Random();
        bool PlayAgain = true;
        string PlayAgainString;
        string player;
        string computer;

        while (PlayAgain){

            player = "";
            computer = "";

            while (player != "rock" && player != "paper" && player != "scissors"){

                Console.Write("Enter rock, paper or scissors: ");
                player = Console.ReadLine();
            }
            
            Console.WriteLine("Player: " + player);

            switch (random.Next(1, 4)){

                case 1:
                    computer = "rock";
                    break;
                
                case 2:
                    computer = "paper";
                    break;
                
                case 3:
                    computer = "scissors";
                    break;
            }

            Console.WriteLine("Computer: " + computer);

            switch (computer){

                case "rock":
                    if (player == "rock"){
                        Console.WriteLine("Its a draw");
                    }
                    else if (player == "paper"){
                        Console.WriteLine("You won!");
                    }
                    else if (player == "scissors"){
                        Console.WriteLine("You lost!");
                    }
                    break;
                
                case "paper":
                    if (player == "paper"){
                        Console.WriteLine("Its a draw");
                    }
                    else if (player == "scissors"){
                        Console.WriteLine("You won!");
                    }
                    else if (player == "rock"){
                        Console.WriteLine("You lost!");
                    }
                    break;
                
                case "scissors":
                    if (player == "scissors"){
                        Console.WriteLine("Its a draw");
                    }
                    else if (player == "rock"){
                        Console.WriteLine("You won!");
                    }
                    else if (player == "paper"){
                        Console.WriteLine("You lost!");
                    }
                    break;
            }

            Console.Write("Would you like to play again? (y/n)>> ");
            PlayAgainString = Console.ReadLine();

            if (PlayAgainString == "y"){

                PlayAgain = true;
            }

            else{

                PlayAgain = false;
            }


        }
    }
}