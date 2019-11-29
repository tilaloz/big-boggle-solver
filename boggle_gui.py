# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:20:23 2019

@author: vaa7199
"""

import tkinter as tk
import boggle as bg


def update_board(a,b,c):
    # This should be done with a constructor to boggle once it is a class
    bg.board = [[sv[i][j].get() for i in range(5)] for j in range(5)]

def solve():

    answer = tk.Tk()
    answer.title('Boggle Solutions')

    words = bg.solve()
    lengths = [len(word) for word in words]
    mx = max(lengths)
    mn = min(lengths)
    listboxes=[]
    scrollbars=[]
    for i in range(mn,mx+1):
        scrollbars.append(tk.Scrollbar(answer))
        listboxes.append(tk.Listbox(answer,width = i +1,
                                    font="Helvetica 20 bold",
                                    yscrollcommand=scrollbars[-1].set))
#        listboxes[-1].grid(column=2*(i-mn), row=0)
#        scrollbars[-1].grid(column=2*(i-mn)+1,row = 0)
        listboxes[-1].pack(side=tk.LEFT,fill=tk.Y)
        scrollbars[-1].pack(side=tk.LEFT,fill=tk.Y)

 
        scrollbars[-1].config(command=listboxes[-1].yview)
        for word in words:
            if len(word) == i:
                listboxes[-1].insert(tk.END,word)
    answer.lift()
    

root = tk.Tk()
root.title('Boggle')



T = []
sv = []
for i in range(5):
    T.append([])
    sv.append([])
    for j in range(5):
        sv[i].append(tk.StringVar())
        sv[i][j].set(bg.board[i][j])
        sv[i][j].trace_add("write",update_board)
        T[i].append(tk.Entry(root, width=4, justify=tk.CENTER,
         font = "Helvetica 60 bold", textvariable=sv[i][j]))
        T[i][j].grid(row = i, column = j)

solve_button = tk.Button(root, text = "Solve", command=solve, height=2, 
                        font = "Helvetica 20 bold")
solve_button.grid(row =5, column=2, pady = 20 )

tk.mainloop()