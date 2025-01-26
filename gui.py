from db import connection
from tkinter import * 
import mysql.connector

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
    val= (name, old_price, price)
    mycursor.execute(sql, val)
    
    conn.commit()
    if mycursor.rowcount > 0:
        print("Kayıt başarıyla eklendi!")
        input1.delete(0, END)
        input2.delete(0, END)
        Label(root, text='Başarılı Kayıt').grid(row=5, column=0, padx=10, pady=10)
    else:
        print("Kayıt eklenemedi.")

def fetch_data():
    mycursor.execute("SELECT name, eski_fiyat, yeni_fiyat FROM products")
    data = mycursor.fetchall()
    size = listbox.size()
    if size == 0:
        for row in data:
            listbox.insert(END, f"{row[0]} - {row[1]} - {row[2]}")
    elif len(data) > size:
        listbox.delete(0, END)
        for row in data:
            listbox.insert(END, f"{row[0]} - {row[1]} - {row[2]}")
    else:
        pass

def clear_list():
    listbox.delete(0,END)




root = Tk(screenName=None, baseName=None, className="Tk", useTk=1)
root.geometry("1000x500")

Label(root, text='Ürün adı').grid(row=0, column=0, padx=10, pady=10)
Label(root, text='Fiyat').grid(row=1, column=0, padx=10, pady=10)


input1 = Entry(root)
input1.grid(row=0, column=1, padx=10, pady=10)

input2 = Entry(root)
input2.grid(row=1, column=1, padx=10, pady=10)

button1 = Button(root, text="Kaydet", width=20, command=insert)
button1.grid(row=3, column=0, columnspan=2,pady=10)

listbox = Listbox(root, width=50, height=15)
listbox.grid(column=1 , pady=20)

fetch_button = Button(root, text="Verileri Getir", command=fetch_data)
fetch_button.grid(column=1)

clear_button = Button(root, text="Verileri Temizle", command=clear_list)
clear_button.grid(row=7 ,column=1)

root.mainloop()