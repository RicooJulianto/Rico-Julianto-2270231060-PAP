pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    Selamat Datang di Ricc Coffe
    List Menu Minuman Kopi 
 
    ==============================
    1. Espresso : Rp 18.000
    2. Latte : Rp 17.000
    3. Hot Tea : Rp 15.000
    4. Ice Americano : Rp 10.000
    5. Hot Chocolate : Rp 20.000
    ==============================
    """)
    namapelanggan=str(input("Masukkan Nama Anda ="))
    alamat=str(input("Masukkan Alamat Anda ="))
    notelepon=str(input("Masukkan No Telepon Anda ="))
    tanggal=str(input("Masukkan Tanggal Pembelian ="))
    pesan=str(input("Masukkan List Abjad Menu Kopi ="))
    jumlahpesan=int(input("Masukkan Jumlah Pesanan ="))
    if pesan == "1":
        listnama= "Espresso"
        harga=(18000)
        totalharga = int(harga*jumlahpesan)
    elif pesan == "2":
        listnama= "Latte"
        harga = (17000)
        totalharga = int(harga*jumlahpesan)
    elif pesan == "3":
        listnama= "Hot Tea"
        harga = (150000)
        totalharga = int(harga*jumlahpesan)
    elif pesan == "4":
        listnama= "Ice Americano"
        harga = (10000)
        totalharga = int(harga*jumlahpesan)
    elif pesan == "5":
        listnama= "Hot Chocolate"
        harga = (20000)
        totalharga = int(harga*jumlahpesan)
    else:
        namapelanggan = "-"
        alamat = "-"
        notelepon = "-"
        tanggal = "-"
        listnama = "-"
        harga = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("Ricc Coffe")
    print("--------------------------")
    print("Nama Pelanggan :",namapelanggan)
    print("Alamat :",alamat)
    print("No Telepon :",notelepon)
    print("Tanggal :",tanggal)
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")