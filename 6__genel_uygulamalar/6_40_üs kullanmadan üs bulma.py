import tkinter

def hesap():
    a=int(E1.get())
    b=int(E2.get())
    c=1
    for i in (1,b,1): c=c*a
    
 
    etiket3.config(text=str(c))
root = tkinter.Tk()
etiket1 = tkinter.Label(root,text="a  giriniz")
etiket1.grid(row=1,column=0,padx=110, pady=10)

etiket2 = tkinter.Label(root,text="b giriniz")
etiket2.grid(row=2,column=0,padx=110, pady=10)

etiket3 = tkinter.Label(root,text=" c ")
etiket3.grid(row=4,column=0,padx=110, pady=10)


E1 = tkinter.Entry(root, bd =2)
E1.grid(row=2,column=1,padx=110, pady=3)

E2 = tkinter.Entry(root, bd =2)
E2.grid(row=1,column=1,padx=110,pady=3)


button1= tkinter.Button(root, text =" hesapla ",width=20,command=hesap)
button1.grid(padx=110, pady=70)

            
root.mainloop()


