import datetime

# Function for input item to the dictItem (Shopping List)
"""
Program ini merupakan sistem kasir self-service.
Cutomer dapat menginput sendiri item yang ingin ditambahkan dalam list belanjanya.
Customer akan menginput nama item, jumlah item, harga item persatuan.
Setelah itu sistem akan menampilkan sub total, diskon, dan total bayar.
Menu yang terdapat dalam sistem ini adalah menginput item, mengubah nama, jumlah, dan harga item,
menghapus item, me-reset transaksi.
Hasil akhir dari program ini adalah struk pembelanjaan yang berisi rincian item yang ada dalam
keranjang belanja, diskon, dan total harga yang harus dibayar customer.

"""


def input_item(key):
    '''
    Fungsi input_item digunakan untuk menginput item kedalam list belanja (dict_item).
    dict_item(dictionary) merupakan sebuah dictionary yang berisi index/key sebagai key 
    dan dictionary atribut barang sebagai value.
    Fungsi ini memiliki parameter berupa key(int).
    Input yang di terima fungsi ini berupa
    1. nama barang (string)
    2. jumlah barang (int)
    3. harga barang (int)
    Untuk mengisi dict_item menggunakan perulangan while.
    Perulangan akan terus berjalan selama menerima inputan angka 1 (ingin menambah item)
    dan akan berhenti jika menerima input-an angka 2 (tidak ingin menambah item).
    Output dari fungsi ini adalah mengembalikan nilai dict_item.

    '''
    
    index = key # variabel for save the index of item in dictionary
    
    repeat = 1 # variabel for repeat the looping
    while repeat == 1:
        item_name = input("Nama Barang = ").title()
        item_quantity = int(input('Jumlah Barang = '))
        item_price = int(input('Harga Barang = '))
        total_price = item_quantity*item_price # variabel for save value item_quantity*item_price
        dict_item.update({index: {'name': item_name, 'quantity': item_quantity,
                                  'price': item_price, 'total_price': total_price}})
        repeat = int(input("Apakah ingin menambah item? \n1. Ya\n2. Tidak\n"))
        index += 1
    
    return dict_item


# Function for show values dictItem (shopping list) and check is get discount
def show_shopping_list(dict_item):
    '''
    Fungsi show_shopping_list digunakan untuk menampilkan isi dari list belanja (dict_item)
    Parameter fungsi ini adalah dict_item(dictionary).
    Variabel yang akan ditampilkan adalah 
    1. id_transaksi(stirng)
    2. nama_customer(string)
    3. hari dan tanggal transaksi (datetime)
    4. nama_item(string)
    5. jumlah_item (int)
    6. harga_item(int)
    7. total_harga_per_item(int)
    8. sub_total_belanja(int)
    9. diskon (int)
    10.total belanja(int)
    Variabel total_harga_per_item adalah hasil kali harga_item dan jumlah_item.
    Variabel sub_total_belanja merupakan hasil penjumlahan semua total_harga_per_item yang ada didalam list belanja.
    variabel diskon adalah potongan harga yang didapatkan jika memenuhi syarat untuk mendapatkan diskon.
    Variabel total_belanja merupakan pengurangan antara sub_total_belanja dengan diskon.
    Didalam fungsi ini terdapat program untuk mengecek dan menghitung berapa diskon yang didapatkan berdasarkan jumlah sub_total_belanja.
    Output dari fungsi ini adalah menampilkan list belanja, diskon, dan total_bayar.

    '''

    print("\n-----List Belanja -----")
    print(f"ID Transaksi\t= {id_transaction}") # print id transaction
    print(f"Nama Customer\t= {customer_name}") # print customer name
    print(f'{date.strftime("%A")}, {date.strftime("%x")}') # print transaction day
    print(('-')*40) # print line

    sub_total = 0 # variabel for save value of total totalPrice
    for item in dict_item:
        print(f"{dict_item[item]['name']}\t{dict_item[item]['quantity']}\
              {(dict_item[item]['price']):,}\t{(dict_item[item]['total_price']):,}")
        sub_total = sub_total + dict_item[item]['total_price']
    
    print(("-")*40) # print line
    print(f"Sub Total\t\t\t{sub_total:,}")
    
    # check is get discount
    if sub_total >= 200000 and sub_total < 300000:
        discount = int(sub_total*(5/100))
    elif sub_total >= 300000 and sub_total < 500000:
        discount= int(sub_total*(8/100))
    elif sub_total >= 500000:
        discount= int(sub_total*(10/100))
    else:
        discount = 0
   
    total = sub_total - discount # variabel for save total pay

    # print discount and total pay
    print(f"Discount \t\t\t{discount:,}")
    print(f"Total \t\t\t\t{total:,}")
    print("----- Thank You -----")


# Function for found item index in dictItem
def found_index(dict_item, name):
    '''
    Fungsi found_index digunakan untuk mencari index sebuah item didalam dict_item.
    Parameter dari fungsi ini adalah dict_item(dictionary) dan name(string).
    Program menggunakan perintah for untuk melakukan pengulangan untuk mengakses setiap index dalam dict_item
    dan menggunakan perintah if untuk menentukan kondisi saat isi dict_item sama dengan name.
    Output dari fungsi ini adalah mengembalikan nilai index dari dict_item.

    '''

    global index
    for key in dict_item:
        if name == dict_item[key]['name']:
            index = key
    
    return index


# Function for upDate item
def update_item(dict_item, name, action):
    '''
    Fungsi update_item digunakan untuk meng-update nama, jumlah, dan harga item.
    Parameter fungsi ini adalah dict_item (dictionary), name (string), dan action (int).
    Variabel name merupakan nama barang yang ingin di-update.
    Variabel action merupapakan action yang akan dilakukan berdasarkan inputan yang diterima.
    Pilihan yang disediakan fungsi ini terdiri dari mengubah nama, mengubah jumlah, atau mengubah harga.
    Dalam fungsi ini juga memanggil fungsi found_index untuk menemukan index dari item yang akan di-update.
    Output dari fungsi ini adalah mengubah isi dict_item berdasarkan inputan dan perintah yang diterima.
    
    '''

    found_index(dict_item, name) # function for get index item
    global index
    
    if index != None :
        if action == 1:
            new_name = input("Masukkan nama item baru = ").title()
            dict_item[index]['name'] = new_name
        elif action == 2:
            new_quantity = int(input("Masukkan jumlah item baru = "))
            dict_item[index]['quantity'] = new_quantity
            dict_item[index]['total_price'] = new_quantity*dict_item[index]['price']
        else:
            new_price = int(input("Masukkan harga item baru = "))
            dict_item[index]['price'] = new_price
            dict_item[index]['total_price'] = dict_item[index]['quantity']* new_price
        
    else:
        print("Nama Barang tidak ditemukan")


# Function for delete item
def delete_item(dict_item, name):
    '''
    Fungsi delete_item digunakan untuk menghapus item berdasarkan inputan berupa nama item di dalam dict_list.
    Parameter fungsi ini adalah dict_list (dictionary) dan name(string).

    '''

    found_index(dict_item, name) # function for get index item
    global index
    
    if index != None :
        dict_item.pop(index)
    else:
        print("Nama Barang tidak ditemukan")


# Function for clear Shopping List
def clear_transaction(dict_item):
    '''
    Fungsi clear_transaction digunakan untuk mereset atau menghapus semua isi dict_item.
    Parameter yang digunakan dalam fungsi ini adalah dict_item(dictionary)

    '''

    dict_item.clear()


# Function for check shopping list is true
def check_shopping_list():
    '''
    Fungsi check_shopping_list digunakan untuk mengecek apakah customer ingin mengubah list belanja (isi dict_item).
    Fungsi ini menggunakan if-else untuk menerima inputan apakah customer ingin mengubah list belanja.
    Di dalam if terdapat fungsi if-elif yang digunakan untuk memanggil perintah lain sesuai dengan action yang customer harapkan.
    Jika cutomer salah meng-input pilihan maka akan ada pemberitahuan bahwa customer salah meng-input. 
    Fungsi ini akan kembali memanggil dirinya setelah menjalankan semua program/perintah,
    sehingga memungkinkan cutomer untuk melakukan update list item berkali-kali.
    Fungsi ini akan selesai jika menerima inputan bahwa customer sudah tidak ingin mengubah list belanja.

    '''
    print("\nApakah ingin mengubah list belanja?\n1. Ya\n2. Tidak")
    check_list = int(input("Masukkan pilihan anda = "))
    
    
    if check_list == 1: # if customer wants update the shopping list
        print("\nPilihan Perintah Untuk Mengupdate List Belanja")
        print("1. Ubah Nama Barang\n2. Ubah Jumlah Barang\
              \n3. Ubah Harga Barang\n4. Hapus Barang\
              \n5. Hapus List Transaksi\n6. Input Barang Baru")
        action = int(input("Masukkan pilihan anda = "))
        if action == 1: # customer wants to update item name
            name = input("Masukkan nama barang yang akan diubah = ").title()
            update_item(dict_item, name, action)
            show_shopping_list(dict_item)
            check_shopping_list()
        elif action == 2: # customer wants to update item quantity
            name = input("Masukkan nama barang yang akan diubah jumlahnya = ").title()
            update_item(dict_item, name, action)
            show_shopping_list(dict_item)
            check_shopping_list()
        elif action == 3: # customer wants to update item price
            name = input("Masukkan nama barang yang akan diubah harganya = ").title()
            update_item(dict_item, name, action)
            show_shopping_list(dict_item)
            check_shopping_list()
        elif action == 4: # customer wants to delete an item
            name = input("Masukkan nama barang yang akan dihapus = ").title()
            delete_item(dict_item, name)
            show_shopping_list(dict_item)
            check_shopping_list()
        elif action == 5: # customer wants to restart shopping list
            clear_transaction(dict_item)
            show_shopping_list(dict_item)
            check_shopping_list()
        elif action == 6: # customer wants to input new item
            print("Silahkan Input Barang Baru")
            key = 1 + len(dict_item)
            input_item(key)
            show_shopping_list(dict_item)
            check_shopping_list()
        else:
            print("Anda salah memasukkan kode")
            check_shopping_list()
    else:
        print("-----Transaksi anda selesai-----")


#Main Program
print("Halo Selamat Datang\nSilahkan Input Barang Belanjaan Anda")
id_transaction = input("Input ID Transaksi = ")
customer_name = input("Input nama anda = ").title()
date = datetime.datetime.now()
dict_item = {}
index = None

input_item(1)
show_shopping_list(dict_item)
check_shopping_list()
show_shopping_list(dict_item)