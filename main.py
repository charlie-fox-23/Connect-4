import pygame
import sys

rows,cols = 6,7
squaresize = 100
radius = int(squaresize/2 - 5)
width = cols*squaresize
height = (rows+1)*squaresize
size = (width,height)

#colors
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

def draw_board(board):
 for c in range(cols):
   for row in range(rows):
    pygame.draw.rect(screen,blue,(c*squaresize,row*squaresize+squaresize,squaresize,squaresize))
    pygame.draw.circle(screen,black,(int(c*squaresize+squaresize/2),int(r*squaresize+squaresize+squaresize/2)),radius)

   #Drawing the pieces
 for c in range(cols):
    for r in range(rows):
       if board[r][c] == 1 :
          pygame.draw.circle(screen,red,(int(c*squaresize+squaresize/2), height-int(r*squaresize+squaresize/2)), radius)
       elif board[r][c]= = 2 :
          pygame.draw.circle(screen,yellow,(int(c*squaresize+squaresize/2), height-int(r*squaresize+squaresize/2)), radius)
 pygame.display.update()

class Board :
   def __init__(self):
      self.grid = [[0 for _ in range(cols)]for _ in range(rows)]
   def is_vaild_location(self,col):
      return self.grid [rows-1][col]==0
   def get_next_open_row(self,col):
      for r in range(rows):
         if self.grid [r][col] ==0:
            return r
   def draw_piece(self,row,col,piece):
      self.grid [row][col] = piece