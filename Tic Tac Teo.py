import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy


sign = 0


global board
board = [[" " for x in range(3)] for y in range(3)]



def winner(b, l):
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or
			(b[0][2] == l and b[1][1] == l and b[2][0] == l))

def isfree(i, j):
	return board[i][j] == " "



def isfull():
	flag = True
	for i in board:
		if(i.count(' ') > 0):
			flag = False
	return flag


def pc():
	possiblemove = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				possiblemove.append([i, j])
	move = []
	if possiblemove == []:
		return
	else:
		for let in ['O', 'X']:
			for i in possiblemove:
				boardcopy = deepcopy(board)
				boardcopy[i[0]][i[1]] = let
				if winner(boardcopy, let):
					return i
		corner = []
		for i in possiblemove:
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
				corner.append(i)
		if len(corner) > 0:
			move = random.randint(0, len(corner)-1)
			return corner[move]
		edge = []
		for i in possiblemove:
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
				edge.append(i)
		if len(edge) > 0:
			move = random.randint(0, len(edge)-1)
			return edge[move]




def get_text_pc(i, j, gb, l1, l2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			l1.config(state=DISABLED)
			l2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			button[i][j].config(state=ACTIVE)
			l2.config(state=DISABLED)
			l1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])
	x = True
	if winner(board, "X"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Player won the match")
	elif winner(board, "O"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Computer won the match")
	elif(isfull()):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Tie Game", "Tie Game")
	if(x):
		if sign % 2 != 0:
			move = pc()
			button[move[0]][move[1]].config(state=DISABLED)
			get_text_pc(move[0], move[1], gb, l1, l2)



def gameboard_pc(game_board, l1, l2):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text_pc, i, j, game_board, l1, l2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	



def withpc(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toc")
	l1 = Button(game_board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text="Computer : O",
				width=10, state=DISABLED)

	l2.grid(row=2, column=1)
	gameboard_pc(game_board, l1, l2)


def play():
	menu = Tk()
	menu.geometry("250x250")
	menu.title("Tic Tac Toe")
	wpc = partial(withpc, menu)
	B1 = Button(menu, text="Single Player", command=wpc,
				activeforeground='purple',
				activebackground="blue", bg="purple",
				fg="yellow", width=500, font='summer', bd=5)

	B1.pack(side='top')
	menu.mainloop()


# Call main function
if __name__ == '__main__':
	play()
