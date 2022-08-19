from tkinter import * 
from tkinter import messagebox
from random import *

def save():
    website =web.get()
    email =eml.get()
    password =pas.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("pas_data.txt" ,'a') as data:
                data.write(f"{website} | {email} | {password}\n")
            web.delete(0,END)
            pas.delete(0,END)

def password():
    pas.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  

    password=password_letters+password_numbers+password_symbols
    shuffle(password)
    new_pass=''.join(password)
    pas.insert(0,new_pass)

if __name__ == "__main__":
    windows = Tk() 
    windows.title("My Personal Password Manager...")
    windows.config(padx=20,pady=20)
    
    canvas =Canvas(height=200,width=200)
    logo=PhotoImage(file="logo.png")
    canvas.create_image(100,100,image=logo)
    canvas.grid(row=0,column=1)
    
    web_lab=Label(text="Website/Service : ")
    web_lab.grid(row=1,column=0)
    email_lab=Label(text="Email : ")
    email_lab.grid(row=2,column=0)
    password_lab=Label(text="Password : ")
    password_lab.grid(row=3,column=0)
    
    
    web=Entry(width=40)
    web.grid(column=1,row=1,columnspan=2)
    web.focus()
    eml=Entry(width=40)
    eml.grid(column=1,row=2,columnspan=2)
    eml.insert(0,"your@gamil.com")
    pas=Entry(width=21)
    pas.grid(column=1,row=3)
    
    btn_gen=Button(text="Generator Password",command=password)
    btn_gen.grid(row=3,column=2)
    
    btn_add=Button(text="Add Your Password Now",width=36,command=save)
    btn_add.grid(row=4,column=1,columnspan=2)
    windows.mainloop()
