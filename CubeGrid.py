# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 03:41:22 2019

@author: Owner
"""

import random

# Set defaults for Big Boggle Rules
dictionary_name = "Collins Scrabble Words (2015).txt"
length_of_board = 5
minimum_word_length = 4
found = []
dice  = [
['A','A','A','F','R','S'],
['A','A','E','E','E','E'],
['A','A','F','I','R','S'],
['A','D','E','N','N','N'],
['A','E','E','E','E','M'],
['A','E','E','G','M','U'],
['A','E','G','M','N','N'],
['A','F','I','R','S','Y'],
['B','B','J','K','X','Z'],
['C','C','E','N','S','T'],
['E','I','I','L','S','T'],
['C','E','I','P','S','T'],
['D','D','H','N','O','T'],
['D','H','H','L','O','R'],
['D','H','H','N','O','W'],
['D','H','L','N','O','R'],
['E','I','I','I','T','T'],
['E','I','L','P','S','T'],
['E','M','O','T','T','T'],
['E','N','S','S','S','U'],
['Qu','In','Th','Er','He','An'],
['G','O','R','R','V','W'],
['I','P','R','S','Y','Y'],
['N','O','O','T','U','W'],
['O','O','O','T','T','U']
]

def shake_board():
    rolled_dice = [random.choice(elem) for elem in dice ]
    random.shuffle(rolled_dice)
    return np.reshape(np.array(rolled_dice),[length_of_board,length_of_board])
    
 

def iterate(stub,available,index,dictionary,board):
    available[index[0],index[1]] = False
    stub = stub + board[index[0],index[1]]
    remaining = [elem for elem in dictionary if stub == elem[0:len(stub)] ]
    # Are there still words?... maybe even a match?
    if len(remaining) > 0:
        if remaining.count(stub) > 0:
            found.append(stub)  
        neighbor_list = neighbors(index,available)
        for neighbor in neighbor_list:
            iterate(stub,available.copy(),neighbor,remaining[:],board)
    else:
        return None

def word_list(dictionary_name):
    # Open the dictionary file and read in the words
    with open(dictionary_name,'r') as f:
        words = f.read().upper().split('\n')
        words = [elem for elem in words if len(elem) >= minimum_word_length]
        return words

class CubeGrid:
    def __init__(self,n=5,m=5):
        self.n = n
        self.m = m
        self.grid = [[CubeGridXY(i+0,j+0) for j in range(m) ] for i in range(n) ]
        for i in range(n):
            for j in range(m):
                for k in range(-1,2):
                    for l in range(2):
                        x = i+k
                        y = j+l
                        if x in range(n) and y in range(m):
                            self.grid[i][j].add_neighbor(self.grid[x][y])
        

class CubeGridXY:
    def __init__(self,x=None,y=None):
        """CubeGridXY needs neighbors and a location"""
        self.neighbors = []
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)
    def __repr__(self):
        return self.__str__()
      
        
    def add_neighbor(self,neighbor):
        """Add a neighbor link to another CubeGridXY (if not already added)"""
        if self != neighbor: # No, you can't be your own neighbor
            if not neighbor in self.neighbors: # only neighbors once!
                self.neighbors.append(neighbor)
                
                
    def remove_neighbor(self,neighbor):
        """Remove the neighbor link to another CubeGridXY"""
        if neighbor in self.neighbors: 
            self.neighbors.remove(neighbor)
        # Could remove the neighbors link back to us but that makes it not a 
        # directed graph         
            

def main():
    dictionary = word_list(dictionary_name)
    cube_grid = CubeGrid()                      
    print(cube_grid.grid)
    board = shake_board()
    print(board)
    iterate("",available[:],[i,j],dictionary,board)
    unique = sorted(set(found))
    print(unique,len(unique))
    
      
         
if __name__ == "__main__":
    main()

    
    
    

                