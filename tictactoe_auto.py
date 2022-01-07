"""
    Create an auto tic tac toe game 
    
"""
import random
import numpy as np
from time import sleep

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
            
    #checking for empty spaces on the board
    def is_empty(self):
        empty_cells = []
        
        for i in range(len(self.board)):
            for j in range(len(self.board)):     
                if self.board[i][j] == "#":
                    empty_cells.append((i, j))
        return empty_cells
    
    #selecting a random position for the player
    def random(self, player):
        empty_cells = self.is_empty()
        current_play = random.choice(empty_cells)
        self.board[current_play[0]][ current_play[1]] = player 
        
            
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
            j = len(self.board) - 1 - i
            if self.board[i][j] != player:
               win = False
               break
        return win
   
    #checking if the board is filled
    def is_board_filled(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "#":
                    return False
        return True
    
    def switch_players(self, player):
        #switching the current players by allowing them take turns playing
        if player == "X":
            self.cur_player = "O"
        else:
            self.cur_player = "X" 
    
        
    def start(self):
        
        while True:   
            #creating an empty board
            self.create_board()
            
            #viewing the board
            self.show_board()
            
            #ensuring board is not full
            while not self.is_board_filled():
                
                print("Player {} is to play". format(self.cur_player))
                self.random(self.cur_player)
                self.switch_players(self.cur_player)
                sleep(3)
                
                #viewing the board
                self.show_board()
                
                #checking if anyone won
                self.result_X = self.is_player_win('X')  
                self.result_O = self.is_player_win('O') 
                
                if self.result_X:
                    self.score_board["X"] += 1
                    print("Player {} won this round!".format("X"))
                    self.cur_player = "O"
                    break
                
                elif self.result_O:
                    self.score_board["O"] += 1
                    print("Player {} won this round!".format("O"))
                    self.cur_player = "X"
                    break
            
            if self.result_X == self.result_O:
                print("DRAW! No winner")
            
            #To continue or end game
            print("\n")
            print("Do you want the game to continue?")
            print("Enter Y to continue and Q to quit")
            
            choice = input().upper().strip()
            
            if choice == "Q":
                print("Final scores!")
                self.print_scoreboard()
                break
            elif choice == "Y":
                self.new = True

    #storing the game information   
    def game_info(self):
       #keeps track of the current player
       self.cur_player = "X"
       
       #keeping track of the scoreboard
       self.score_board = {"X": 0, "O": 0}
       
    
    #displaying the scoreboard after the players quit
    def print_scoreboard(self):
        print("                     SCOREBOARD               ")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
        print("     ", "X", "     ",self.score_board["X"])
        print("     ", "O", "     ",self.score_board["O"])
    
   
if __name__ == "__main__":
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
    print("Welcome to TicTacToe game!")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")    
        
    play = tictactoe()
    play.game_info()
    play.start()           