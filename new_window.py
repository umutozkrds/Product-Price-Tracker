from tkinter import *
from db import connection
import mysql.connector

#def open_new_window(root):
#root.withdraw()
new_window = Toplevel()
new_window.title("Yeni Pencere")
new_window.geometry("400x300")

conn, mycursor = connection()

price_updates = {}

def control_data():
    pname = product_name.get()
    price = int(product_price.get())
    
    mycursor.execute("SELECT yeni_fiyat FROM products WHERE name = %s", (pname,))
    data = mycursor.fetchall()

    if data:
        old_price = data[0][0]  # Mevcut (eski) fiyatı al
        listbox.insert(END, f"Ürün adı: {pname} - Kayıtlı Fiyat: {old_price} - Yeni Fiyat: {price}")

        # Güncellenecek ürünleri sakla
        price_updates[pname] = price
        print(price_updates)
    else:
        listbox.insert(END, f"Ürün adı: {pname} - Kayıtlı değil! - Yeni Fiyat: {price}")

def update_prices():
    for pname, new_price in price_updates.items():
        mycursor.execute("UPDATE products SET yeni_fiyat = %s WHERE name = %s", (new_price, pname))
    
    conn.commit()
    listbox.insert(END, "Tüm fiyatlar güncellendi!")
    price_updates.clear()  # Güncellenen verileri sıfırla



Label(new_window, text='Ürün Adı:').grid(row=0, column=0, sticky=W, pady=5)
product_name = Entry(new_window, width=25)
product_name.grid(row=0, column=1, pady=5)

Label(new_window, text='Fiyat Kontrol:').grid(row=1, column=0, sticky=W, pady=5)
product_price = Entry(new_window, width=25)
product_price.grid(row=1, column=1, pady=5)

control_button = Button(new_window, text="Kontrol Et" ,command=control_data)
control_button.grid(row=3, column=1)

listbox = Listbox(new_window, width=50, height=10)
listbox.grid(row=4, column=0, columnspan=2, pady=10, padx=20)

update_button = Button(new_window, text="Fiyatları Güncelle", width=20, command=update_prices)
update_button.grid(row=5, column=0, columnspan=2, pady=5)

close_button = Button(new_window, text="Kapat", command=lambda: close_new_window(new_window, root))
close_button.grid(row=6,column=0, padx=10, pady=10)

def close_new_window(new_window, root):
    new_window.destroy()  # Yeni pencereyi kapat
    root.deiconify()  # Ana pencereyi geri getir

new_window.mainloop()