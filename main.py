import json
import tkinter
from tkinter import *
import cryptography
from cryptography.fernet import Fernet
from tkinter import messagebox

window = Tk()
window.title("Secret Notes")
window.minsize(width= 300, height=500)

#notes dosyasına yazma


def new_dos():
    key = Fernet.generate_key()
    chip = Fernet(key)

    with open("filekey.key", "wb") as filekey:
        filekey.write(key)

    masterkey = key_entry.get()

    with open("masterk.key", "w") as maskey:
        maskey.write(masterkey)
    key_entry.delete(0,END)

    wr1 = enter_entry.get()
    note1 = secret_entry.get("1.0",END)
    message = note1.encode()
    encrypt_mes = chip.encrypt(message).decode()

    dosya = open("myNotes.txt", "w")
    dosya.write(wr1)
    enter_entry.delete(0, END)
    dosya.write(":\n")
    dosya.write(str(encrypt_mes))
    secret_entry.delete("1.0", END)



#kiptoyu çözme

def krp_coz():
    with open("filekey.key", "rb") as filekey:
        deckey = filekey.read()
    fernet = Fernet(deckey)

    with open("masterk.key", "r") as masterkk:
        maskey = masterkk.read()
    if key_entry.get() == maskey:
        note2 = secret_entry.get("1.0",END)
        messag2 = note2.encode()
        decr_mes = fernet.decrypt(messag2).decode()
        secret_entry.delete("1.0", END)
        secret_entry.insert("end",decr_mes)
    else:
        messagebox.showerror("error!", "enter the correct key")



#top secret logo
imge = PhotoImage(file = "topsec.png")

main_label = Label(text= "label1", image= imge,width=100)
main_label.pack()

enter_label = tkinter.Label(text="Enter your title", width=20, font=("Arial",10,"bold"))
enter_label.pack(padx= 5, pady= 5)

enter_entry = tkinter.Entry(width=35)
enter_entry.pack(padx= 5, pady= 0)

secret_label = tkinter.Label(text="Enter your secret", width=20, font=("Arial",10,"bold"))
secret_label.pack()

secret_entry = tkinter.Text(width=30, height=10)
secret_entry.pack()

key_label = tkinter.Label(text="Enter master key", width=13, font=("Arial",10,"bold"))
key_label.pack(padx= 5, pady= 5)

key_entry = tkinter.Entry(width=35)
key_entry.pack(padx= 5, pady= 0)

save_but = tkinter.Button(text="Save & Encrypto", font=("Arial",8,"bold"), command=new_dos)
save_but.pack(padx= 5, pady= 0)

dec_but = tkinter.Button(text="Decrypt", font=("Arial",8,"bold"), command=krp_coz)
dec_but.pack(padx= 5, pady= 0)




window.mainloop()