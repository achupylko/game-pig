import random

max_score = 50
player_scores = []

def main():
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
        print("Invalid number of players, please try again.")

    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:
        for player_idx in range(players):
            print(f"\nPlayer {player_idx + 1} turn has just started.")
            print(f"Your total score is {player_scores[player_idx]}.\n")

            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y)? ")
                if should_roll.lower() != "y":
                    break

                roll_value = roll()
                print(f"You rolled a {roll_value}.")
                if roll_value == 1:
                    print("Turn done!")
                    current_score = 0
                    player_scores[player_idx] = 0
                    break
                else:
                    current_score += roll_value

                print(f"Your score is {current_score}.")

            player_scores[player_idx] += current_score
            print(f"Your total score is {player_scores[player_idx]}.")
    
    winning_score = max(player_scores)
    winning_idx = player_scores.index(winning_score)
    print(f"\nPlater {winning_idx + 1} is the winner with a score of {winning_score}.")


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


if __name__ == "__main__":
    main()