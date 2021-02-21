import time
import random
import sys
from positions import *
from displayMessages import *



class SnakeAndLadder:
    def __init__(self):
        pass

    def welcome_msg(self):
        print("\n")
        print("#" * 25, "WELCOME TO SNAKE AND LADDER", "#"*25)
        print("\n")
        print("#" * 30, "MAIN MENU", "#"*30)
        print("""
    Rules:
        >>> Initally both the players are at starting position i.e. 0 .
            Take it in turns to roll the dice.
            Move forward the number of spaces shown on the dice.
        >>> If you lands at the bottom of a ladder,
            you can move up to the top of the ladder.
        >>> If you lands on the head of a snake,
            you must slide down to the bottom of the snake.
        >>> The first player to get to the FINAL position is the winner.
        >>> Hit enter to roll the dice.
    """)

    def get_player_names(self):
        while True:
            self.play = input("Enter 'S' to start game, Enter 'N' to quit the game: ")
            if self.play == "S" or self.play == "s":
                print("Choose your mode (Single player/Multiplayer)")
                self.mode = input("Enter \"S\" for sigle player and \"M\" for multiplayer: ")

                if self.mode == "S" or self.mode == "s":
                    self.player2 = "Computer"
                    self.num_players = 2
                else:
                    self.num_players = int(input("Enter number of players lessthan 5: "))
                self.player1 = input("Enter player 1 name: ")

                if (self.mode == "m" or self.mode == "m") and 5 > self.num_players > 1:
                    self.player2 = input("Enter player 2 name: ")
                if 5 > self.num_players > 2:
                    self.player3 = input("Enter player 3 name: ")
                if 5 > self.num_players > 3:
                    self.player4 = input("Enter player 4 name: ")
                    print()

                print("Good Luck!")
                self.player1_score = 0
                self.player2_score = 0
                self.player3_score = 0
                self.player4_score = 0
                while True:
                    if 5 > self.num_players > 1:
                        self.start_1 = input("\n" + self.player1 + ":" + random.choice(player_turn_text) + " Hit the 'ENTER' to roll the dice (or) type 'NO' to quit the game: ")
                        if self.start_1 == "":
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player1 + " Rolling dice...")
                            self.dice_value = self.get_dice_value()
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player1 + " moving....")
                            self.player1_score = self.snake_ladder(self.player1, self.player1_score, self.dice_value)
                            self.check_win(self.player1, self.player1_score)
                        else:
                            break
                            quit
                        self.start_2 = input("\n" + self.player2 + ":" + random.choice(player_turn_text) + " Hit the 'ENTER' to roll the dice (or) type 'NO' to quit the game: ")
                        if self.start_2 == "":
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player2 + " Rolling dice...")
                            self.dice_value = self.get_dice_value()
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player2 + " moving....")
                            self.player2_score = self.snake_ladder(self.player2, self.player2_score, self.dice_value)
                            self.check_win(self.player2, self.player2_score)
                        else:
                            break
                            quit
                    if 5 > self.num_players > 2:
                        self.start_3 = input("\n" + self.player3 + ":" + random.choice(player_turn_text) + " Hit the 'ENTER' to roll the dice (or) type 'NO' to quit the game: ")
                        if self.start_3 == "":
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player3 + " Rolling dice...")
                            self.dice_value = self.get_dice_value()
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player3 + " moving....")
                            self.player3_score = self.snake_ladder(self.player3, self.player3_score, self.dice_value)
                            self.check_win(self.player3, self.player3_score)
                        else:
                            break
                            quit
                    if 5 > self.num_players > 3:
                        self.start_4 = input("\n" + self.player4 + ":" + random.choice(player_turn_text) + " Hit the 'ENTER' to roll the dice (or) type 'NO' to quit the game: ")
                        if self.start_4 == "":
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player4 + " Rolling dice...")
                            self.dice_value = self.get_dice_value()
                            time.sleep(SLEEP_BETWEEN_ACTIONS)
                            print(self.player4 + " moving....")
                            self.player4_score = self.snake_ladder(self.player4, self.player4_score, self.dice_value)
                            self.check_win(self.player4, self.player4_score)
                        else:
                            break
                            quit

                    print("________________________________________________________________")

            elif self.play == "N" or self.play == "n":
                break
                quit
            else:
                sys.exit(1)

    def get_dice_value(self):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        self.dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(self.dice_value))
        return self.dice_value

    def got_snake_bite(self, old_value, current_value, player_name):
        print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

    def got_ladder_jump(self, old_value, current_value, player_name):
        print("\n" + random.choice(ladder_jump).upper() + " ########")
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

    def snake_ladder(self, player_name, current_value, dice_value):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value
        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value
        print(player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            self.got_snake_bite(current_value, final_value, player_name)
        elif current_value in ladders:
            final_value = ladders.get(current_value)
            self.got_ladder_jump(current_value, final_value, player_name)
        else:
            final_value = current_value
        return final_value

    def check_win(self, player_name, position):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            print("\nThank you for playing the game.\n\n")
            sys.exit(1)

    def start(self):
        self.welcome_msg()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        self.get_player_names()