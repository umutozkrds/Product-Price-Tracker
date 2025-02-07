from db import connection
from tkinter import *
import mysql.connector
from new_window import open_new_window

conn, mycursor = connection()

def insert():
    name = input1.get()
    try:
        old_price = 0
        price = int(input2.get())
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return

    sql = "INSERT INTO products (name, eski_fiyat, yeni_fiyat) VALUES (%s, %s, %s)"
    val = (name, old_price, price)
    mycursor.execute(sql, val)
    
    conn.commit()
    if mycursor.rowcount > 0:
        print("Kayıt başarıyla eklendi!")
        input1.delete(0, END)
        input2.delete(0, END)
        success_label.config(text="Başarılı Kayıt!", fg="green")
    else:
        print("Kayıt eklenemedi.")

def fetch_data():
    mycursor.execute("SELECT name, eski_fiyat, yeni_fiyat FROM products")
    data = mycursor.fetchall()
    listbox.delete(0, END)
    for row in data:
        listbox.insert(END, f"{row[0]} - {row[1]} - {row[2]}")

def clear_list():
    listbox.delete(0, END)



root = Tk()
root.title("Ürün Otomasyonu")
root.geometry("500x500")
root.resizable(True, True)

# Ana Frame
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

# Giriş Alanı
Label(main_frame, text='Ürün Adı:').grid(row=0, column=0, sticky=W, pady=5)
input1 = Entry(main_frame, width=25)
input1.grid(row=0, column=1, pady=5)

Label(main_frame, text='Fiyat:').grid(row=1, column=0, sticky=W, pady=5)
input2 = Entry(main_frame, width=25)
input2.grid(row=1, column=1, pady=5)

# Butonlar
button1 = Button(main_frame, text="Kaydet", width=20, command=insert)
button1.grid(row=2, column=0, columnspan=2, pady=10)

fetch_button = Button(main_frame, text="Verileri Getir", width=20, command=fetch_data)
fetch_button.grid(row=3, column=0, columnspan=2, pady=5)

clear_button = Button(main_frame, text="Verileri Temizle", width=20, command=clear_list)
clear_button.grid(row=4, column=0, columnspan=2, pady=5)

new_window_button = Button(main_frame, text="Yeni Pencere Aç", width=20, command=lambda: open_new_window(root))
new_window_button.grid(row=5, column=0, columnspan=2, pady=5)

# Başarı / Hata Mesajı
success_label = Label(main_frame, text="", fg="red")
success_label.grid(row=6, column=0, columnspan=2, pady=5)

# Listbox Alanı
listbox = Listbox(main_frame, width=50, height=10)
listbox.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
