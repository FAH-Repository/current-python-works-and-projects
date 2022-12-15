#installed pip requests
import tkinter as tk
import requests

def check_url(urlEntry):
    try:
        r = requests.get(urlEntry)
        print(r.status_code)
        if r.status_code == 200:
            L3['text'] = "It is online!"
        elif r.statuscode == 404:
            L3['text'] = "It is offline"
    except requests.exceptions.MissingSchema as e:
        L3['text'] = "non-real URL or bad formatting"
    except AttributeError:
        L3['text'] = "non-real URL or bad formatting"
    


top = tk.Tk()
top.title("Status Check")
# Code to add widgets will go here...
canvas = tk.Canvas(top, height=50, width=400)
canvas.pack()
L1 = tk.Label(top,text="Needs full format ex: https://www.websitename.com/" )
L1.pack()
L2 = tk.Label(top, text="URL to check")
L2.pack()
E1 = tk.Entry(top, bd=5, width=50)
E1.pack()
B1 = tk.Button(top, text="check URL", command=lambda: check_url(E1.get()))
B1.pack()
L3 = tk.Label(top)
L3.pack()
top.mainloop()


    

