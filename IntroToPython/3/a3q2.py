
from random import choice  # import 'choice' function from 'random' module


# main function:
def main():
    # inform user of what the program does:
    print("This program allows you to play matching pennies against a computer opponent"
          "\nThe game will last for 5 rounds"
          "\nAt the start of a round, each player picks \"heads\" or \"tails\""
          "\nIf the choices match, you win (+1 to you, -1 to computer)"
          "\nIf the choices do not match, you lose (-1 to you, +1 to computer)")

    user_score = 0  # user's score
    opponent_score = 0  # opponent's score
    choices_list = ["heads", "tails"]  # list of valid choices
    user_choice = None  # user's choice

    # loop through 5 rounds of play:
    for current_round in range(1, 6):  # give current_round value of 1-5
        print("\nBeginning round", current_round)  # print current round

        while user_choice not in choices_list:  # while user's choice isn't valid:
            user_choice = input("Enter \"heads\" or \"tails\": ")  # prompt user for choice

            if user_choice not in choices_list:  # if given choice wasn't valid:
                print("You did not enter \"heads\" or \"tails\"")  # inform user of error
            else:  # choice was valid:
                opponent_choice = choice(choices_list)  # use imported 'choice' function to pick opponent's choice
                print(f"You chose {user_choice} and the opponent chose {opponent_choice}")  # inform user of choices

                if user_choice != opponent_choice:  # if choices don't match:
                    opponent_score += 1  # increment opponent's score by 1
                    user_score -= 1  # decrement user's score by 1
                    print("You lose!")  # inform user of loss
                else:  # choices match:
                    user_score += 1  # increment user's score by 1
                    opponent_score -= 1  # decrement opponent's score by 1
                    print("You win!")  # inform user of win

                print(f"Round {current_round} over")  # inform end of current round
                user_choice = None  # clear user's choice
                break  # break from while

    # inform that all rounds are complete, and show scores:
    print(f"\nAll rounds complete \nYour score: {user_score} \nOpponent score: {opponent_score}")


# if module is run as script (i.e: name == "__main__"):
if __name__ == "__main__":
    main()  # execute main function
