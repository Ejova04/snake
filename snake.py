from tkinter import *
from random import *
 
def move():
    global x
    global y,pX,pY
    global Serpent
    can.delete('all')
    i=len(Serpent)-1
    j=0
    
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
        #anneaux serpent
        can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10,outline='blue', fill='white')
        i=i-1
   

    can.create_rectangle(pX, pY, pX+5, pY+5, outline='red', fill='red')
   
    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 593
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > 593:
            Serpent[0][0] = 0
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = 593
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > 593:
            Serpent[0][1] = 0
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10,outline='green', fill='blue')
    test()
    test()
   
    if flag != 0:
        fen.after(60, move)
 
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    move()
 
def left(event):
    global direction
    direction = 'gauche'
 
def right(event):
    global direction
    direction = 'droite'
 
def up(event):
    global direction
    direction = 'haut'
 
def down(event):
    global direction
    direction = 'bas'
   
def test():
    global pomme
    global x,y,pX,pY
    global Serpent
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:        
        if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
            #pomme respawn
            pX = randrange(5, 595)
            pY = randrange(5, 595)
            can.coords(pomme,pX, pY, pX+5, pY+5)
            #serpent up
            Serpent.append([0,0])
            #print(Serpent)

def pause(event):
    global flag
    if flag:
        flag=0
    else:
        flag=1
        move()
       
x = 245
y = 24        
dx, dy = 10, 10
flag = 0
direction = 'haut'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]

pX = randrange(5, 595)
pY = randrange(5, 595)

fen = Tk()
can = Canvas(fen, width=600, height=600, bg='black')
can.pack(side=TOP, padx=5, pady=5)
#tete
oval1=can.create_oval(Serpent[1][0], Serpent[1][1], Serpent[1][0] +10, Serpent[1][1]+10, outline='blue', fill='blue')
#corps
oval = can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, outline='blue', fill='white')
#pomme
pomme = can.create_rectangle(pX, pY, pX+5, pY+5, outline='red', fill='red')

b1 = Button(fen, text='Lancer', command=newGame, bg='grey' , fg='blue')
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(fen, text='Quitter', command=fen.destroy, bg='grey' , fg='blue')
b2.pack(side=RIGHT, padx=5, pady =5)

#tex1 = Label(fen, text="Cliquez sur 'Lancer' pour commencer le jeu.", bg='grey' , fg='blue')
#tex1.pack(padx=0, pady=11)

fen.title('Jeu Snake')
fen.bind('<z>' , up)
fen.bind('<q>', left)
fen.bind('<s>', down)
fen.bind('<d>', right)

fen.mainloop()

