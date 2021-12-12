from random import choice


def main():

    user_score = 0
    opp_score = 0
    choices_list = ["heads", "tails"]
    user_choice = None

    for current_round in range(1, 6):  # ++++++++++FIVE rounds of play
        print("current round:", current_round)

        while user_choice not in choices_list:
            user_choice = input("Enter heads or tails: ")

            if user_choice not in choices_list:
                print("error, enter heads or tails")
            else:
                opp_choice = choice(choices_list)  # ++++++++++CHOICE
                print("you chose: ", user_choice, " op chose: ", opp_choice)

                if user_choice != opp_choice:
                    opp_score +=1
                    user_score -=1
                    print("you lose")
                else:
                    user_score +=1
                    opp_score -=1
                    print("you win")

            print(f"Round {current_round} over")
            user_choice = None  # ++++++++++++++RESET CHOICE
            break

    print(f"All rounds complete. your score: {user_score}. opp score: {opp_score}")


if __name__ == "__main__":
    main()