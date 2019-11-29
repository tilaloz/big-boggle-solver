# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 06:59:29 2018
An attempt to learn python (again) and write a big boggle board solver

@author: vaa7199
"""

import numpy as np

# Set defaults for Big Boggle Rules
dictionary_name = "Collins Scrabble Words (2015).txt"

minimum_word_length = 4
found = [] 

board =          [["t","n","a","a","r"],
                  ["t","e","l","o","e"],
                  ["s","O","e","qu","o"],
                  ["e","x","g","e","y"],
                  ["t","c","d","i","h"]]

board = [[letter.lower() for letter in row] for row in board]

length_of_board = len(board)

def neighbors(index,available):
    vert = np.array([0,1])
    horz = np.array([1,0])
    indices = [index-vert,index+vert,
               index-vert+horz,index+vert+horz,
               index-vert-horz,index+vert-horz,
               index-horz,index+horz]
    indices = [elem for elem in indices 
               if elem[0] >= 0 and elem[0] < length_of_board and
                  elem[1] >= 0 and elem[1] < length_of_board and
                  available[elem[0],elem[1]]]        
    return indices
    

def iterate(stub,available,index,dictionary):
    available[index[0],index[1]] = False
    stub = stub + board[index[0]][index[1]]
    remaining = [elem for elem in dictionary if stub == elem[0:len(stub)] ]
    # Are there still words?... maybe even a match?
    if len(remaining) > 0:
        if remaining.count(stub) > 0:
            found.append(stub)  
        neighbor_list = neighbors(index,available)
        for neighbor in neighbor_list:
            iterate(stub,available.copy(),neighbor,remaining[:])
    else:
        return None

def word_list(dictionary_name):
    # Open the dictionary file and read in the words
    with open(dictionary_name,'r') as f:
        words = f.read().lower().split('\n')
        words = [elem for elem in words if len(elem) >= minimum_word_length]
        return words
        
def solve():
    #TODO: Gracefully degrade if boards has empties
    available = np.full((length_of_board, length_of_board), True)
    dictionary = word_list(dictionary_name)
    for i in range(length_of_board):
        for j in range(length_of_board):
            iterate("",available.copy(),[i,j],dictionary)
    unique = sorted(sorted(set(found)),key=len)
    return unique
    
   

def main():
    unique = solve()
    print(unique,len(unique))
    
def find_digraphs(words):
    n = 2
    digraphs = []
    for line in words:
        for i in range(0,len(line)-(n-1)):
            if not line[i:i+n] in digraphs:
                digraphs.append(line[i:i+n])
    return digraphs
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    
    

    







