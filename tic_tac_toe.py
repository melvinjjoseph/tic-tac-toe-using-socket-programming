"""
Tic Tac Toe
"""

class TicTacToe():

    def __init__(self, player_symbol):
        self.symbol_list = []
        self.score = 0
        for i in range(9):
            self.symbol_list.append(" ") 
        self.player_symbol = player_symbol

    def restart(self):
        for i in range(9):
            self.symbol_list[i] = " "


    def draw_grid(self):
        print("\n       A   B   C\n")
        row_one = "   1   " + self.symbol_list[0]
        row_one += " | " + self.symbol_list[1]
        row_one += " | " + self.symbol_list[2]
        print(row_one)

        print("      ---+---+---")

        row_two = "   2   " + self.symbol_list[3]
        row_two += " | " + self.symbol_list[4]
        row_two += " | " + self.symbol_list[5]
        print(row_two)

        print("      ---+---+---")

        row_three = "   3   " + self.symbol_list[6]
        row_three += " | " + self.symbol_list[7]
        row_three += " | " + self.symbol_list[8]
        print(row_three, "\n")


    def edit_square(self, grid_coord):
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]
        col = grid_coord[0].capitalize()
        row = grid_coord[1]
        grid_index = 0

        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8

        if self.symbol_list[grid_index] == " ":
            self.symbol_list[grid_index] = self.player_symbol

    def update_symbol_list(self, new_symbol_list):
        for i in range(9):
            self.symbol_list[i] = new_symbol_list[i]

    def did_win(self, player_symbol):
        g = []
        for i in range(9):
            g.append(self.symbol_list[i])
        sym = player_symbol

        if g[0] == sym and g[1] == sym and g[2] == sym:
            return True

        elif g[3] == sym and g[4] == sym and g[5] == sym:
            return True
                
        elif g[6] == sym and g[7] == sym and g[8] == sym:
            return True 

        elif g[0] == sym and g[3] == sym and g[6] == sym:
            return True 

        elif g[1] == sym and g[4] == sym and g[7] == sym:
            return True 

        elif g[2] == sym and g[5] == sym and g[8] == sym:
            return True

        elif g[2] == sym and g[4] == sym and g[6] == sym:
            return True 

        elif g[0] == sym and g[4] == sym and g[8] == sym:
            return True         
        
        return False

    def is_draw(self):
        num_blanks = 0
        for i in range(9):
                if self.symbol_list[i] == " ":
                    num_blanks += 1
        if self.did_win(self.player_symbol) == False and num_blanks == 0:
            return True
        else:
            return False
