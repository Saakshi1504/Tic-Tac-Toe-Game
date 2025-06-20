from tkinter import*
import tkinter.messagebox
tboard={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
count=0
loss=0
turn='X'
def checkforwin(player):
    global count,loss
    if((tboard[1]==tboard[2]==tboard[3] and (tboard[1]!=' 'or tboard[2]!=' 'or tboard[3]!=' ')) or (tboard[4]==tboard[5]==tboard[6]and( tboard[4]!=' 'or tboard[5]!=' 'or tboard[6]!=' ')) or (tboard[7]==tboard[8]==tboard[9]and( tboard[7]!=' 'or tboard[8]!=' 'or tboard[9]!=' ')) or (tboard[1]==tboard[4]==tboard[7]and( tboard[1]!=' 'or tboard[4]!=' 'or tboard[7]!=' ')) or (tboard[2]==tboard[5]==tboard[8]and( tboard[2]!=' 'or tboard[5]!=' 'or tboard[8]!=' ')) or (tboard[3]==tboard[6]==tboard[9]and ( tboard[3]!=' 'or tboard[6]!=' 'or tboard[9]!=' ')) or (tboard[1]==tboard[5]==tboard[9]and ( tboard[1]!=' 'or tboard[5]!=' 'or tboard[9]!=' ')) or (tboard[3]==tboard[5]==tboard[7]and ( tboard[3]!=' 'or tboard[5]!=' 'or tboard[7]!=' '))):
        count+=1
    else:
        loss+=1
def play(event):
    global turn,count,loss,tboard
    button=event.widget
    buttontext=str(button)
    clicked=buttontext[-1]
    if clicked=='n':
        clicked=1
    else:
        clicked=int(clicked)
    if button["text"]=='':
        button["text"]=turn
        if turn=='X':
            tboard[clicked]=turn
            turn='O'
        else:
            tboard[clicked]=turn
            turn='X'
    checkforwin(turn)
    if count==1:
        if turn=='X':
            turn='O'
        else:
            turn='X'
        tkinter.messagebox.showinfo("RESULT","Player "+turn+" won the match!CONGRATULATIONS!!")
        response=tkinter.messagebox.askquestion("Do you wish to Play Again?")
        if response=='no':
            tkinter.messagebox.showinfo('Thanks',"Thank you for playing.")
            root.destroy()
        else:
            tboard={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
            count=0
            loss=0
            turn='X'
            root.destroy()
            start()      
    elif loss==9:
        tkinter.messagebox.showinfo("RESULT","The match was a draw")
        response=tkinter.messagebox.askquestion("Do you wish to Play Again?")
        if response=='no':
            tkinter.messagebox.showinfo('Thanks',"Thank you for playing.")
            root.destroy()
        else:
            tboard={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
            count=0
            loss=0
            turn='X'
            root.destroy()
            start()   
def start():
    global root
    root=Tk()
    root.title("TIC-TAC-TOE")
    label=Label(root,text="TIC-TAC-TOE",font=('Arial',32))
    label.grid()
    label1=Label(root,text='Think on your feet but also be careful.',font=('Arial',12))
    label1.grid(row=2)
    label3=Label(root,text='The first player who places three of their marks in a horizontal, vertical or diagonal row wins the game!',font=('Arial',12))
    label3.grid(row=3)
    frame=Frame(root,highlightthickness=1,highlightbackground="black")
    frame.grid()
    button1=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button1.bind("<Button-1>",play)
    button1.grid(row=1,column=1,padx=5,pady=5)
    button2=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button2.bind("<Button-1>",play)
    button2.grid(row=1,column=2,padx=5,pady=5)
    button3=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button3.bind("<Button-1>",play)
    button3.grid(row=1,column=3,padx=5,pady=5)
    button4=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button4.bind("<Button-1>",play)
    button4.grid(row=2,column=1,padx=5,pady=5)
    button5=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button5.bind("<Button-1>",play)
    button5.grid(row=2,column=2,padx=5,pady=5)
    button6=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button6.bind("<Button-1>",play)
    button6.grid(row=2,column=3,padx=5,pady=5)
    button7=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button7.bind("<Button-1>",play)
    button7.grid(row=3,column=1,padx=5,pady=5)
    button8=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button8.bind("<Button-1>",play)
    button8.grid(row=3,column=2,padx=5,pady=5)
    button9=Button(frame,text='',width=5,height=2,font=('Arial',30))
    button9.bind("<Button-1>",play)
    button9.grid(row=3,column=3,padx=5,pady=5)
    root.mainloop()
start()