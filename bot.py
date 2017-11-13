import pygame
import sys
from pynput.keyboard import Key, Controller
from winning.py import *
keyboard = Controller()

pygame.init()
#c1location = (1,1)
#c2location = (2,1)
#c3location = (3,1)
#c4location = (4,2)
#c5location = (5,1)
#MOUSE = pygame.USEREVENT + 1
#column1 = pygame.event.Event(MOUSE, location=c1location)
#pygame.event.post(column1)
#pygame.event.get
#done = False
#while not done:
#    for event in pygame.event.get():
#        if event.type == MOUSE:
#            print("column1")
#            done = True
#    pygame.event.pump()


# #Keyboard input for bot, to control it before completing calculations (if we want to implement this instead of mouse click). Can be completed after structure of matrix is set.
# for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_1:
#                 #place in first column of matrix, set 0 in lowest row within column to 2
#             if event.key == K_2:
#                 #place in second column of matrix, set 0 in lowest row within column to 2
#             if event.key == K_3:
#                 #place in third column of matrix, set 0 in lowest row within column to 2
#             if event.key == K_4:
#                 #place in fourth column of matrix, set 0 in lowest row within column to 2
#             if event.key == K_5:
#                 #place in fifth column of matrix, set 0 in lowest row within column to 2
def minimax(node, depth, myTurn, matrix, connect):
    """Evaluation of scores and nodes to pick the best move.
    Takes depth, boolean of myTurn, matrix of the playing field, and # to connect.
    Returns an """
    if depth == 0: # or node is terminal
        a = scoring(matrix, connect, myTurn)
    if myTurn:
        #bestValue = -10
        for child in range(node):
            #place piece in column child
            v = minimax(child, depth-1, FALSE)
            #bestValue =
        return (v, child)
    else:
        #bestValue = 10
        for child in range(node):
            #place piece in column child
            v = minimax(child, depth-1, TRUE)
            #bestValue =
        return (v, child)

a = numpy.matrix('0 0 0 0; 0 0 0 0; 0 0 0 0')
print(minimax(4, 2, True, a, 3))

def choose_option(options={3:100}):
    """choose the the highest value
    return the key (branch) of the maximum value (score)
    if no option given, choose the middle column(3)
    """
    best_option = max(options, key=options.get)
    return str(best_option)

def simulate_keypress(keypress):
    """simulates keypress"""
    keyboard.press(keypress)
    keyboard.release(keypress)

simulate_keypress(choose_option())
