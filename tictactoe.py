import sys
import pygame
import numpy as np
import random
import copy
from constants import *

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS,COLS) )
        self.empty_sqrs = self.squares # [squares]
        self.marked_sqrs = 0

    def final_state(self):
        '''
            @return 0 if there is no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
        '''
        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]
        
        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]
        
        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        
        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]
        
        # no win yet
        return 0
    
    def mark_sqr(self,row,col,player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self,row,col):
        return self.squares[row][col] == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row,col):
                    empty_sqrs.append((row,col))
        return empty_sqrs
    
    def isfull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0

class AI:
    def __init__(self,level = 1,player = 2):
        self.level = level
        self.player = player

    def rnd(self,board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0,len(empty_sqrs))

        return empty_sqrs[idx] # (row,col)

    def minimax(self,board,maximizing):
        # terminal case
        case = board.final_state()

        # player 1 wins
        if case == 1:
            return 1,None # eval,move
        
        # player 2 wins
        if case == 2:
            return -1,None # eval,move
        
        # draw
        elif board.isfull():
            return 0,None # eval,move
        
        if maximizing:
            pass

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row,col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row,col,self.player)
                eval = self.minimax(temp_board,True)[0]

    def eval(self,main_board):
        if self.level == 0:
            # random choice
            move = self.rnd(main_board)
        else:
            # minimax algo choice
            self.minimax(main_board,False)

        return move # row,col

class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1 # 1-cross 2-circle
        self.gamemode = 'ai' # pvp or ai
        self.running = True
        self.show_lines()

    def show_lines(self):
        # vertical
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(WIDTH - SQSIZE,0),(WIDTH - SQSIZE,HEIGHT),LINE_WIDTH)
        
        # horizontal
        pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(0,HEIGHT - SQSIZE),(WIDTH,HEIGHT - SQSIZE),LINE_WIDTH)

    def draw_fig(self,row,col):
        if self.player == 1:
            # draw cross
            # desc line
            start_desc = (col*SQSIZE + OFFSET, row*SQSIZE + OFFSET)
            end_desc = (col*SQSIZE + SQSIZE - OFFSET, row*SQSIZE + SQSIZE -OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_desc,end_desc,CROSS_WIDTH)
            # asc line
            start_asc = (col*SQSIZE + OFFSET, row*SQSIZE + SQSIZE - OFFSET)
            end_asc = (col*SQSIZE + SQSIZE - OFFSET, row*SQSIZE  + OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_asc,end_asc,CROSS_WIDTH)

        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE //2,row * SQSIZE + SQSIZE//2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS,CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

def main():

    # object
    game = Game()
    board = game.board
    ai = game.ai

    # mainloop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_sqr(row,col):
                    board.mark_sqr(row,col,game.player)
                    game.draw_fig(row,col)
                    game.next_turn()

        if game.gamemode == 'ai' and game.player == ai.player:
            # update the screen
            pygame.display.update()

            # ai methods
            row,col = ai.eval(board)

            board.mark_sqr(row,col,ai.player)
            game.draw_fig(row,col)
            game.next_turn()
            
                    
        pygame.display.update()

main()
