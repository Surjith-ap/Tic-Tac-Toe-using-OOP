
class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0 ,0],
                           [0, 0, 0],
                           [0, 0, 0]]
        
    def print_board(self):
        print("\n Positions")
        self.print_positions()

        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("  |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()


    
    def print_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")


    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("Enter at a different position")

    def check_game_over(self, player, last_move):
        return


