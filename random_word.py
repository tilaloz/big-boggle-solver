# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:17:55 2020

@author: marsh
"""
import random

dictionary_name = "Collins Scrabble Words (2015).txt"

def word_list(dictionary_name):
    # Open the dictionary file and read in the words
    with open(dictionary_name,'r') as f:
        words = f.read().upper().split('\n')
        return words
        
def main():
    dictionary = word_list(dictionary_name)
    print(random.choice(dictionary))
    
if __name__ == "__main__":
    main()