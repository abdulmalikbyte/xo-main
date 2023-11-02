from tkinter import *
from tkinter import messagebox
import random as random

def button(frame):          
    choice=Button(frame,padx=1,bg="white",width=3,text="   ",
             font=('arial',60,'bold'),relief="sunken",bd=10)
    return choice

def change_a():            
    global player
    for i in ['O','X']:
        if not(i==player):
            player=i
            break

def reset():                
    global player
    for i in range(3):
        for j in range(3):
                choice[i][j]["text"]=" "
                choice[i][j]["state"]=NORMAL
    player=random.choice(['O','X'])
    
def check():                
    for i in range(3):
            if(choice[i][0]["text"] == choice[i][1]["text"] == choice[i][2]["text"] == player
               or choice[0][i]["text"] == choice[1][i]["text"] == choice[2][i]["text"] == player):
                    messagebox.showinfo("Congrats!!","'"+player+"' has won")
                    reset()
    if(choice[0][0]["text"] == choice[1][1]["text"] == choice[2][2]["text"] == player
       or choice[0][2]["text"] == choice[1][1]["text"] == choice[2][0]["text"] == player):
        messagebox.showinfo("Congrats!!","'"+player+"' has won")
        reset()   
    elif(choice[0][0]["state"] == choice[0][1]["state"] == choice[0][2]["state"]
         == choice[1][0]["state"] == choice[1][1]["state"] == choice[1][2]["state"]
         == choice[2][0]["state"] == choice[2][1]["state"] == choice[2][2]["state"] == DISABLED):
        messagebox.showinfo("Tied!!","The match ended in player draw")
        reset()
        
def click(row,col):
        choice[row][col].config(text=player,state=DISABLED,disabledforeground=colour[player])
        check()
        change_a()
        label.config(text=player+"'s Chance")

root=Tk()
                   
root.title("Tic-Tac-Toe")
   
player=random.choice(['O','X'])     
  
colour={
    'O':"deep sky blue",
    'X':"lawn green"}

choice=[[],[],[]]

for i in range(3):
        for j in range(3):
                choice[i].append(button(root))
                choice[i][j].config(command= lambda row=i,col=j:click(row,col))
                choice[i][j].grid(row=i,column=j)
                
label=Label(text=player+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)

root.mainloop()