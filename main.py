def main_menu():
    while True:
        print ("n=== RestoApps ===")
        print ("1. Kelola Menu")
        print ("2. Buat Pesanan")
        print ("3. Logout")

        pilih = input ("Pilih menu: ")

        if pilih == "1":
            menu_management() # penamaan function sementara
        elif pilih == "2": 
            order_menu() #penamaan function order menu
        elif pilih == "3": 
            break
        else: 
            print("Pilihan anda tidak ada")

def start_app():
    while True: 
        print("\n === Selamat datang di RestoApps===")
        print ("1. Register")
        print ("2. Login")
        print ("3. Exit")

        pilih = input("Pilih: ")

        if pilih == "1":
            register() # penamaan function sementara
        elif pilih == "2":
            user = login()# penamaan function sementara
            if user: 
                main_menu()# penamaan function sementara
            elif pilih == "3":
                print ("Program selesai")
                break
            else:
                print("Pilihan salah")

#menentukan apakah file main dipanggil atau tidak
if __name__ == "__main__":
    start_app()
