#set for 5 GB have only tried up to 394MB roughly, kinda freezes up on recieving end for a bit but did go through, could just be network speeds but perhaps reducing the cap from 5GB to 1GB might help as i noticed the ram usage on recieving was 2GB for 394MB
#some ui to indicate progress would be good instead of just appearing frozen
#though it does say file recieved when actually gone through
#but otherwise looking decent, for some reason default read-1 values dont work hence the 5GB
# this was tested using multiple devices on the same home network, would like to make sure it goes well outside my network

from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("File Share")
root.geometry("450x560")
root.configure(bg="#f4fdfe")
root.resizable(False,False)


def Send():
    window=Toplevel(root)
    window.attributes("-topmost", True)
    window.title("Send")
    window.geometry("450x560")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetype=(("all files", "*.*"),("file_type","*.txt")))
        selected['text'] = "File Selected"
    
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("waiting for incoming conenctions... ")
        conn, addr=s.accept()
        file=open(filename, "rb")
        file_data=file.read(5000000000)
        conn.send(file_data)
        print("Data has been transmitted succesfully")

    host=socket.gethostname()
    Label(window, text=f"Your ID is: {host}", bg="white",font=("arial", 15, "bold"), fg="black").place(x=10, y=10)
    selected = Label(window, text="No file selected", bg="white",font=("arial", 15, "bold"), fg="black")
    selected.place(x=10, y=50)

    Button(window, text="select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file).place(x=75, y=150)
    
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=sender).place(x=250, y=150)
    

    window.mainloop()

def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry("450x560")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID, port))
        file=open(filename1,"wb")
        file_data=s.recv(5000000000)
        file.write(file_data)
        file.close()
        rec_label['text']= "File has been received"
        print("File has been received")

    rec_label=Label(main, text="Waiting to recieve", font=("arial", 20),bg="#f4fdfe")
    rec_label.place(x=20,y=280)
    Label(main,text="Input Sender ID", font=("arial", 15, "bold"),bg="#f4fdfe").place(x=20,y=10)
    SenderID=Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    SenderID.place(x=20,y=50)
    SenderID.focus()

    Label(main,text="Filename of incoming file", font=("arial", 15, "bold"),bg="#f4fdfe").place(x=20,y=100)
    incoming_file=Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    incoming_file.place(x=20,y=150)

    rr= Button(main,text="Receive", compound=LEFT,width=15, bg="#39c790", font="arial 14 bold", command=receiver)
    rr.place(x=20, y= 500)
    main.mainloop()




Label(root, text="File Transferer",font=("arial", 15, "bold"), bg="#f4fdfe").place(x=150, y=30)

#Frame(root, width=400, height=2, bg="#f4fdfe").place(x=25, y=80)


send=Button(root, text="Send File",font=("arial", 15, "bold"),bg="#f4fdfe",command=Send)
send.place(x=50,y=100)
receive=Button(root,text="Receive File",font=("arial", 15, "bold"), bg="#f4fdfe", command=Receive)
receive.place(x=300,y=100)


root.mainloop()