from tkinter import *
import os

root = Tk()
root.title("BurakYvs XoX Game v0.5")
root.resizable(width=False, height=False)

#--------------------------------------------------Functions

turn = 'X'
gameover = 0
labels = [0,1,2,3,4,5,6,7,8]
labels_x = [0,1,2,3,4,5,6,7,8]
buttons = [0,1,2,3,4,5,6,7,8,9]

def play(i, j, k):
          global turn,gameover
          labels[k] = Label(root,text="" + turn + "", fg="red", bg="white", font="Verdana 50 bold",width=2,relief=RAISED)
          labels[k].grid(row=i,column=j)
          labels_x[k] = turn
          if labels_x[0] == labels_x[1] == labels_x[2]:
             labels[0].config(fg="green")
             labels[1].config(fg="green")
             labels[2].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[0] == labels_x[4] == labels_x[8]:
             labels[0].config(fg="green")
             labels[4].config(fg="green")
             labels[8].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[0] == labels_x[3] == labels_x[6]:
             labels[0].config(fg="green")
             labels[3].config(fg="green")
             labels[6].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[3] == labels_x[4] == labels_x[5]:
             labels[3].config(fg="green")
             labels[4].config(fg="green")
             labels[5].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[6] == labels_x[7] == labels_x[8]:
             labels[6].config(fg="green")
             labels[7].config(fg="green")
             labels[8].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[1] == labels_x[4] == labels_x[7]:
             labels[1].config(fg="green")
             labels[4].config(fg="green")
             labels[7].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[2] == labels_x[5] == labels_x[8]:
             labels[2].config(fg="green")
             labels[5].config(fg="green")
             labels[8].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          elif labels_x[2] == labels_x[4] == labels_x[6]:
             labels[2].config(fg="green")
             labels[4].config(fg="green")
             labels[6].config(fg="green")
             label5.config(text="" + turn + " Wins!!!")
             buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
             buttons[9].grid(row=3, column=2)
             for i in range(0,9):
                  buttons[i].config(cursor="arrow")
                  buttons[i].config(state=DISABLED, bg="grey")
             gameover = 1
          else:
               if labels[0] != 0 and labels[1] != 1 and labels[2] != 2 and labels[3] != 3 and labels[4] != 4 and  labels[5] != 5 and labels[6] != 6 and labels[7] != 7 and labels[8] != 8:
                       label5.config(text="Draw.")
                       buttons[9] = Button(root, text='Play Again', command=restart_program, bg="white", cursor="hand2")
                       buttons[9].grid(row=3, column=2)
               else:
                    if turn == 'X' and gameover == 0:
                           turn = 'O'
                           label5.config(text="It is " + turn + "'s turn.")
                           for i in range(0,9):
                                buttons[i].config(cursor="circle")
                    elif turn == 'O' and gameover == 0:
                           turn = 'X'
                           label5.config(text="It is " + turn + "'s turn.")
                           for i in range(0,9):
                                buttons[i].config(cursor="X_cursor")


def restart_program():
    global gameover,turn,labels,labels_x
    turn = 'X'
    gameover = 0
    for i in range(0,9):
        buttons[i].config(cursor="X_cursor")
        buttons[i].config(state=NORMAL, bg="white")
        if isinstance(labels[i],int) == False:
            labels[i].destroy()
    buttons[9].destroy()
    labels = [0,1,2,3,4,5,6,7,8]
    labels_x = [0,1,2,3,4,5,6,7,8]
    label5.config(text="It is " + turn + "'s turn.")


#--------------------------------------------------Buttons

#TOP

buttons[0] = Button(root, text='', command=lambda row=0, column=0, sira=0: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[0].grid(row=0, column=0, ipadx=45, ipady=30)
buttons[1] = Button(root, text='', command=lambda row=0, column=1, sira=1: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[1].grid(row=0, column=1, ipadx=45, ipady=30)
buttons[2] = Button(root, text='', command=lambda row=0, column=2, sira=2: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[2].grid(row=0, column=2, ipadx=45, ipady=30)

#Mid

buttons[3] = Button(root, text='', command=lambda row=1, column=0, sira=3: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[3].grid(row=1, column=0, ipadx=45, ipady=30)
buttons[4] = Button(root, text='', command=lambda row=1, column=1, sira=4: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[4].grid(row=1, column=1, ipadx=45, ipady=30)
buttons[5] = Button(root, text='', command=lambda row=1, column=2, sira=5: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[5].grid(row=1, column=2, ipadx=45, ipady=30)

#Low

buttons[6] = Button(root, text='', command=lambda row=2, column=0, sira=6: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[6].grid(row=2, column=0, ipadx=45, ipady=30)
buttons[7] = Button(root, text='', command=lambda row=2, column=1, sira=7: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[7].grid(row=2, column=1, ipadx=45, ipady=30)
buttons[8] = Button(root, text='', command=lambda row=2, column=2, sira=8: play(row, column, sira), bg="white", cursor="X_cursor")
buttons[8].grid(row=2, column=2, ipadx=45, ipady=30)


#----------------------------------------------------Labels

label5 = Label(root,text="It is " + turn + "'s turn.", fg="white", bg="orange", font="Verdana 10 bold")
label5.grid(row=3,column=1,sticky=W)

root.mainloop()
