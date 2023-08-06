from tkinter import*
from tkinter import ttk,messagebox
from googletrans import Translator,LANGUAGES

root=Tk()
root.geometry('740x400')
root.title("Translator Project")

def show():
    v1=combo_first.get()
    v2=combo_second.get()
    first_lan.config(text=v1)
    second_lan.config(text=v2)
    root.after(1000,show)

def translate():
    trans=Translator()
    trans_lang=trans.translate(input_text.get(1.0,END),src=combo_first.get(),dest=combo_second.get())

    output_text.delete(1.0,END)
    output_text.insert(END,trans_lang.text) 
   
def clear():
    output_text.delete(1.0,END)
    input_text.delete(1.0,END)
             
def exit():
    root.destroy()



img=PhotoImage(file=r'C:\Users\Madhu\Downloads\tkinter priyat=nka\lang trans\background1.png')

lab=Label(root,image=img)
lab.pack()

convert_img=PhotoImage(file=r'C:\Users\Madhu\Downloads\tkinter priyat=nka\lang trans\convert.png')
clear_img=PhotoImage(file=r'C:\Users\Madhu\Downloads\tkinter priyat=nka\lang trans\clear3.png')
exit_img=PhotoImage(file=r'C:\Users\Madhu\Downloads\tkinter priyat=nka\lang trans\exit.png')

first_lan=Label(root,text='English',font=('Engraves','30','bold'),bg='white',fg='#5582f9')
first_lan.place(x=90,y=30)

second_lan=Label(root,text='Hindi',font=('Engraves','30','bold'),bg='white',fg='#5582f9')
second_lan.place(x=500,y=30)

language=list(LANGUAGES.values())

combo_first=ttk.Combobox(root,values=language)
combo_first.place(x=90,y=80)
combo_first.set('English')

combo_second=ttk.Combobox(root,values=language)
combo_second.place(x=500,y=80)
combo_second.set('Hindi')

input_text=Text(root,height=10,width=35)
input_text.place(x=30,y=100)

output_text=Text(root,height=10,width=35)
output_text.place(x=430,y=100)

convert=Button(root,text='converter',image=convert_img,bd=0,command=translate)
convert.place(x=43,y=300)

clear=Button(root,text='clear',image=clear_img,bd=0,command=clear)
clear.place(x=300,y=300)

ext=Button(root,text='exit',image=exit_img,bd=0,command=exit)
ext.place(x=530,y=300)

show()
mainloop()
