import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox as m_box
from winsound import *
from tkinter import Toplevel
num=random.randint(1,100)
win=tk.Tk()
win.title('Number Guessing Game')
win.geometry('+241+152')
win.config(bg='light yellow')
win.resizable(False,False)

num_label=tk.Label(win,bg='light yellow',text='Guess a number between 1 to 100 :',
                   font=('Helvetica',20),fg='blue')
num_label.grid(row=0,column=0,sticky='w')

wish_label=tk.Label(win,text='All the best !',fg='blue',font=('Helvetica',20),bg='light yellow')
wish_label.grid(row =1,columnspan=4)

entry_num_var=tk.IntVar()
entry_num=tk.Entry(win,width=4,fg='red',textvariable=entry_num_var,font=('Helvetica',20),borderwidth=5)
entry_num.grid(row=2,columnspan=1)
entry_num.focus()


def again():
    global num
    num=random.randint(1,100)
  
global nm
nm=1
def guess(*
          event):
    global nm
    try:
        if num==entry_num_var.get():
            PlaySound('nice-work.wav', SND_FILENAME )
            won=Toplevel()
            won.title('Congratulation !')
            won.geometry('+310+250')
            won.resizable(False,False)
            won.grab_set()
            won.focus()
            again()
            entry_num.delete(0,tk.END)
            sorry_label=tk.Label(won,text='Amazing you won !'+'\n'+f'You guessed number in {nm} times',
                                 font=('times new roman',20),fg='red',bg='gold2')
            sorry_label.grid(row=0,columnspan=5)
            nm=1
            entry_num.delete(0,tk.END)
            gues_again=tk.Button(won,text='Guess Again',command=won.destroy,font=('helvetica',15),
                                   width=12,bg='light green',fg='blue')
            gues_again.grid(row=3,column=2)
            
        else:
            if 100<entry_num_var.get():
                MessageBeep(type=10)
                nm+=1
                msg='Enter number beween 1-100'
            elif (num-entry_num_var.get())<=5 and  (num-entry_num_var.get())>=0:
                MessageBeep(type=10)
                nm+=1
                msg="You are close to this !"+'\n'+'Increase Your Number '
            elif abs(num-entry_num_var.get())<=5:
                MessageBeep(type=10)
                nm+=1
                msg="You are close to this !"+'\n'+'Decrease Your Number '
            elif (num-entry_num_var.get())<=10 and  (num-entry_num_var.get())>=0:
                MessageBeep(type=10)
                nm+=1
                msg="Sorry number is low !"+'\n'+'Increase Your Number '
            elif abs(num-entry_num_var.get())<=10 and  (num-entry_num_var.get())>=0:
                MessageBeep(type=10)
                nm+=1
                msg="Sorry number is high !"+'\n'+'Increase Your Number '
            elif num < entry_num_var.get():
                MessageBeep(type=10)
                msg='Sorry number is too high !'
                nm+=1
            else:
                MessageBeep(type=0)
                nm+=1
                msg='Sorry number is too low !'
            won=Toplevel()
            won.grab_set()
            won.focus()
            won.title('OOP\'s !')
            won.geometry('+350+250')
            won.config(bg='gold2')
            won.resizable(False,False)
            sorry_label=tk.Label(won,text=msg,font=('times new roman',20),fg='red',
                                 bg='light yellow',anchor='center')
            sorry_label.pack()
            guess_again=tk.Button(won,text='Guess Again',command=won.destroy,font=('helvetica',15),
                                   width=12,bg='light green',fg='blue')
            guess_again.pack(pady=20)
            guess_again.focus()
            entry_num.delete(0,tk.END)
    except :
            m_box.showerror('Wrong Input','Type only numbers !')
            entry_num.delete(0,tk.END)
entry_num.delete(0,tk.END)         

submit_btn=tk.Button(win,text='Guess',command=guess,fg='blue',bg='light green',
                     font=('new times roman',18),width=6)
submit_btn.grid(row=3,columnspan=2,pady=10)
win.bind('<Return>',guess)
def on_button():
    m_box.showinfo(message="Good-bye!")
    win.destroy()


submit_btn=tk.Button(win,text='Exit',command=on_button,fg='blue',
                     bg='light green',font=('new times roman',10),width=4)
submit_btn.grid(row=4,columnspan=2)

win.mainloop()


