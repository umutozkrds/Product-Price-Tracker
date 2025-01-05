from db import connection
from tkinter import * 
import mysql.connector

conn, mycursor = connection()


def insert(): # burada kaldık
    name = input1.get()
    try:
        old_price = int(input2.get())
        new_price = int(input3.get())
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return

    sql = "INSERT INTO products (name, eski_fiyat, yeni_fiyat) VALUES (%s, %s, %s)"
    val= (name, old_price, new_price)
    mycursor.execute(sql, val)
    
    conn.commit()
    if mycursor.rowcount > 0:
        print("Kayıt başarıyla eklendi!")
        input1.delete(0, END)
        input2.delete(0, END)
        input3.delete(0, END)
        Label(root, text='Başarılı Kayıt').grid(row=5, column=0, padx=10, pady=10)
    else:
        print("Kayıt eklenemedi.")


root = Tk(screenName=None, baseName=None, className="Tk", useTk=1)
root.geometry("400x500")

Label(root, text='Ürün adı').grid(row=0, column=0, padx=10, pady=10)
Label(root, text='Eski Fiyat').grid(row=1, column=0, padx=10, pady=10)
Label(root, text='Yeni Fiyat').grid(row=2, column=0, padx=10, pady=10)

input1 = Entry(root)
input1.grid(row=0, column=1, padx=10, pady=10)

input2 = Entry(root)
input2.grid(row=1, column=1, padx=10, pady=10)

input3 = Entry(root)
input3.grid(row=2, column=1, padx=10, pady=10)

button1 = Button(root, text="Kaydet", width=20, command=insert)
button1.grid(row=3, column=0, columnspan=2,pady=10)


root.mainloop()