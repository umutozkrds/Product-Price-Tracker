from tkinter import *
from db import connection
import mysql.connector

#def open_new_window(root):
#root.withdraw()
new_window = Toplevel()
new_window.title("Yeni Pencere")
new_window.geometry("400x300")

conn, mycursor = connection()

Label(new_window, text='Ürün Adı:').grid(row=0, column=0, sticky=W, pady=5)
product_name = Entry(new_window, width=25)
product_name.grid(row=0, column=1, pady=5)

Label(new_window, text='Fiyat Kontrol:').grid(row=1, column=0, sticky=W, pady=5)
price = Entry(new_window, width=25)
price.grid(row=1, column=1, pady=5)

control_button = Button(new_window, text="Kontrol Et")
control_button.grid(row=3, column=1)

close_button = Button(new_window, text="Kapat", command=lambda: close_new_window(new_window, root))
close_button.grid(row=5,column=0, padx=10, pady=10)

def close_new_window(new_window, root):
    new_window.destroy()  # Yeni pencereyi kapat
    root.deiconify()  # Ana pencereyi geri getir

new_window.mainloop()