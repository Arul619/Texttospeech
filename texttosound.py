from tkinter import *
from gtts import gTTS
from playsound import playsound
from prettytable import PrettyTable
root=Tk()
root.title("Text To Voice")
root.geometry("600x300")
root.config(bg='black')
Frame=Frame(root,bd=7,relief=RIDGE,bg='powder blue').place(x=10,y=40,width=580,height=150)
label=Label(root,text='Type and here it in voice',font=('Calibri',20),bg='blue',fg='yellow')
label.grid(row=0,column=0)
label.place(x=150,y=50)
Msg = StringVar()
e1=Entry(root,textvariable = Msg,width=25,bd=8)
e1.grid(row=30,column=50)
e1.place(x=200,y=100)
def Play():
    text1=e1.get()
    language='en'
    obj=gTTS(text=text1,lang=language)
    obj.save("exam.mp3")
    playsound("exam.mp3")
def Exit():
    root.destroy()
def Reset():
    Msg.set("")
l=[]
def save_info():
    global l
    l.append(Msg.get())
    file = open("user.txt","w+")
    file.write("word\n")
    for i in l:
        file.write("\n")
        file.write(i)
    
    file.close()
b1=Button(root,text='Play',font='arial 15 bold',command=Play,width='4').place(x=100,y=140)
b1=Button(root,text='Reset',font='arial 15 bold',command=Reset,width='4').place(x=250,y=140)
b1=Button(root,text='Exit',font='arial 15 bold',command=Exit,width='4').place(x=400,y=140)
button = Button(root,text="Save",command=save_info,width="4").place(x=500,y=120)

