from board import Board
from player import Player

class TicTacToeGame:

    def start(self):
        print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")
        print(" **** Welcome to the Game ! !**** ")
        print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True: #game loop
            
            while True: #round loop

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_tie():
                    print("Its a Tie ! Try Again")
                    break
                elif board.check_game_over(player, player_move):
                    print("You Won !!!!!!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_game_over(computer, computer_move):
                        print("Computer won ! hehhehee")
                        break
            play_again = input("Would tou like to try again ? Enter X for yes or O for no").upper()

            if play_again == "O":
                print("Ty for playing Come back soon")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("You input is not valid but i assume you wanna play again")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("New Round")
        board.reset_board()
        board.print_board()

game = TicTacToeGame()
game.start()


