from tkinter import *
from tkinter import messagebox
import random as random

def button(frame):          
    choice=Button(frame,padx=1,bg="white",width=3,text="   ",
             font=('arial',60,'bold'),relief="sunken",bd=10)
    return choice

def playerChoice():            
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
    # horizontal and vertical check                
    for i in range(3):
        if(choice[i][0]["text"] == choice[i][1]["text"] == choice[i][2]["text"] == player
        or choice[0][i]["text"] == choice[1][i]["text"] == choice[2][i]["text"] == player):
            messagebox.showinfo("Congrats!!","'"+player+"' has won")
            reset()

    # diagonal check
    if(choice[0][0]["text"] == choice[1][1]["text"] == choice[2][2]["text"] == player
       or choice[0][2]["text"] == choice[1][1]["text"] == choice[2][0]["text"] == player):
        messagebox.showinfo("Congrats!!","'"+player+"' has wonn!")
        reset() 

    # draw check
    elif(choice[0][0]["state"] == choice[0][1]["state"] == choice[0][2]["state"]
         == choice[1][0]["state"] == choice[1][1]["state"] == choice[1][2]["state"]
         == choice[2][0]["state"] == choice[2][1]["state"] == choice[2][2]["state"] == DISABLED):
        messagebox.showinfo("Tied!!","The match ended in player draw")
        reset()
        
def click(row,col):
        choice[row][col].config(text=player,state=DISABLED,disabledforeground=colour[player])
        check()
        playerChoice()
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



# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

root.mainloop()