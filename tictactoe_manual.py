"""
    Create a tic tac toe game which allows the players play from the CLI
    
"""
#""" 
#creating a class for the game
class tictactoe:
    
    def __init__(self):
        #self.board = []
        #keeping track of positions played by eaxh player
        self.player_pos = {'X': [], 'O': []}

    #method that creates a blank board to start the game
    def create_board(self):
        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append("#")
            self.board.append(row)        
        
    
    #method to dispaly the board as the users plays
    def show_board(self):
        for i in range(3):
            #print("\n")
            print("\t    |    |")
            print("\t {}  | {}  | {} ".format(self.board[i][0], self.board[i][1], self.board[i][2]))
            print("\t____|____|____")
            
    
    def switch_players(self):
        #switching the current players by allowing them take turns playing
        if self.cur_player == player1:
            self.cur_player = player2
        else:
            self.cur_player = player1
            
    #checking if the board is filled
    def is_board_filled(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "#":
                    return False
        return True
    
    #enering the player's input
    def players_input(self, row, column, inputt):
        #keeps track of switching the players
        self.switch = True
        #checking if the position chosen is within the board
        if int(row) > 2 or int(column) > 2:
            print("Such a cell does not exist, It's range is 0 to 2")
            self.switch = False
        #ensuring the allowed players are used
        elif inputt != "X" and inputt != "O":
            print("Please review your input and input the player you represent (i.e X or O)")
            self.switch = False
        #checking if the column chosen is empty
        elif self.board[row][column] != "#":
            print("This cell is already occupied, please view the board again")
            self.switch = False
        else:
            self.board[row][column] = inputt
    
    #checking for wins
    def is_player_win(self, player):
        
        win = None
        
        #checking rows
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
            
        #checking columns
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        
        #checking diagonals
        win = True
        for i in range(3):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        
        win = True
        for i in range(3):
            if i == 1:
               if self.board[i][i] != player:
                win = False
                break
            else:
                for j in range(3):
                    if j != 1 and i != j:
                        if self.board[i][j] != player:
                            win = False
                            break
        if win:
            return win
        
        return False
        
    #method to start the game
    def start(self):

        #keeps track of the current player
        self.cur_player = player1
        #keeping track of a new game
        self.new = True
        
        while True:
            #players choice menu
            print("It is {}'s turn to choose" .format(self.cur_player))
            print("Enter X to play X.")
            print("Enter O to play O.")
            print("Enter Q to quit the game.")
            
            choice = input().upper().strip()
            
            if choice != "X" and choice != "O" and choice != "Q":
                print("Wrong Input! Please check the options again.")
                self.start()
                
            #assigning the players
            elif choice == "X" or choice == "O":
                if choice == "X":
                    self.player_choice[self.cur_player] = 'X'
                    if self.cur_player  == player1:
                        self.player_choice[player2] = 'O'
                    else:
                       self.player_choice[player1] = 'O' 
                else:
                    self.player_choice[self.cur_player ] = 'O'
                    if self.cur_player  == player1:
                        self.player_choice[player2] = 'X'
                    else:
                        self.player_choice[player1] = 'X' 
                
                print("{} is playing as {} while {} is playing as {}.".format(player1, self.player_choice[player1], player2, self.player_choice[player2]))                
            
                #creating an empty board
                self.create_board()
                
                #viewing the board
                self.show_board()
                #ensuring board is not full
                while not self.is_board_filled():
                    
                    #collecting inputs from the players
                    print("Please {} enter the position and value you're playing : ".format(self.cur_player))
                    inputs = list(input())
                    if len(inputs) != 3:
                        pass
    
                    else:
                        self.players_input(int(inputs[0]), int(inputs[1]), inputs[2].upper())
                        self.show_board()
                        
                        #checking if anyone won
                        self.result_X = self.is_player_win('X')  
                        self.result_O = self.is_player_win('O') 
                        if self.result_X:
                            if self.player_choice[player1] == 'X':
                                self.score_board[player1] += 1
                                print("{} won this round!".format(player1))
                                self.cur_player = player1
                            elif self.player_choice[player2] == 'X':
                                self.score_board[player2] += 1
                                print("{} won this round!".format(player2))
                                self.cur_player = player2                        
                            break
                        elif self.result_O:
                            if self.player_choice[player1] == 'O':
                                self.score_board[player1] += 1
                                print("{} won this round!".format(player1))
                                self.cur_player = player1
                            elif self.player_choice[player2] == 'O':
                                self.score_board[player2] += 1
                                print("{} won this round!".format(player2))
                                self.cur_player = player2
                            break
                        
                        if self.switch:
                            #switching the current players by allowing them take turns playing
                            self.switch_players()
                            
                if self.result_X == self.result_O:
                        print("DRAW! No winner")
                        #self.switch_players()
                    
                        
                #creating an empty board
                self.create_board()
                
            elif choice == "Q":
                print("Final scores!")
                self.print_scoreboard()
                break
            
    #storing the game information   
    def game_info(self):
       #keeps track of the current player
       self.cur_player = player1
       
       #stores player's choice
       self.player_choice = {player1: "", player2: ""}
       
       #keeping track of the scoreboard
       self.score_board = {player1: 0, player2: 0}
    
    #displaying the scoreboard after the players quit
    def print_scoreboard(self):
        print("                     SCOREBOARD               ")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
        print("     ", player1, "     ",self.score_board[player1])
        print("     ", player2, "     ",self.score_board[player2])
    
   

    #method to assign players
    def player_choice(self):
        pass
       
if __name__ == "__main__":
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
    print("Welcome to TicTacToe game!")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
    print("Player 1")
    player1 = input("Enter your name : ")
    #print("\n")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
    print("Player 2")
    player2 = input("Enter your name : ")
    print("\n")
        
    play = tictactoe()
    play.game_info()
    play.start()
#"""
