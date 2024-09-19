import tkinter as tk

from tkinter import messagebox


class TicTacToe:

   def __init__(self, master):

       self.master = master

       self.master.title("Крестики Нолики")

       self.master.resizable(False, False)

       self.player = "X"

       self.board = [["" for i in range(3)] for j in range(3)]

       self.buttons = [[tk.Button(self.master, width=8, height=4, font=("Helvetica", 20), command=lambda row=row, col=col: self.mark(row, col)) for col in range(3)] for row in range(3)]

       for row in range(3):

           for col in range(3):

               self.buttons[row][col].grid(row=row, column=col)

               

   def mark(self, row, col):

       if self.board[row][col] == "":

           self.board[row][col] = self.player

           self.buttons[row][col].configure(text=self.player)

           if self.is_winner():

               messagebox.showinfo("Крестики Нолики", f"{self.player} победили!")

               self.reset()

           elif self.is_tie():

               messagebox.showinfo("Tic Tac Toe", "It's a tie!")

               self.reset()

           else:

               self.player = "O" if self.player == "X" else "X"

               

   def is_winner(self):

       for i in range(3):

           if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":

               return True

           if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":

               return True

       if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":

           return True

       if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":

           return True

       return False

   

   def is_tie(self):

       for row in self.board:

           for cell in row:

               if cell == "":

                   return False

       return True

   

   def reset(self):

       self.player = "X"

       self.board = [["" for i in range(3)] for j in range(3)]

       for row in range(3):

           for col in range(3):

               self.buttons[row][col].configure(text="")

   

if __name__ == "__main__":

   root = tk.Tk()

   TicTacToe(root)

   root.mainloop()