#Dictionary untuk menyimpan semua data user
users = {}

#1. Validasi Awal

# Mengecek apakah input hanya huruf alfabet
def only_alpha(text):
    return text.isalpha()

#Mengecek apakah input hanya angka aja
def only_int(text):
    return text.isdigit()

#Mengecek apakah input bisa dikonversi menjadi float
def only_float(text):
    try:
        float (text)
        return True
    except:
        return False

#2. Validasi Email
def validate_email(email):
    #Email harus punya satu @ 
    if email.count("@") != 1:
        return False
    
    #Pisahkan username dan domain
    user, domain = email.split("@")

    #Username tidak boleh kosong dan domain harus punya titik
    if user == "" or "." not in domain:
        return False
    
    #Karakter pertama username harus huruf/angka
    if not user[0].isalnum():
        return False
    
    #Username hanya boleh huruf, angka, . dan _
    for c in user:
        if not (c.isalnum() or c in"._"):
            return False
    
    return True

#3. Validasi User ID
def validate_userid(uid):
    # tidak boleh ada spasi di awal / akhir
    if uid != uid.strip():
        return False

    if len(uid) < 6 or len(uid) > 20:
        return False

    has_letter = False
    has_digit = False

    for c in uid:
        # huruf, angka, dan spasi diperbolehkan
        if not (c.isalnum() or c == " "):
            return False

        if c.isalpha():
            has_letter = True
        if c.isdigit():
            has_digit = True

    # harus kombinasi huruf dan angka
    if not (has_letter and has_digit):
        return False

    # tidak boleh duplikat
    if uid in users:
        return False

    return True


#4. Validasi Password
def validate_password(pw):
    #Panjang password minimal 8 karakter
    if len(pw) < 8:
        return False

    #Karakter spesial boleh dipakai di password
    special = "/.,@#$%" 

    #Harus ada huruf kapital, kecil, special karakter,dan angka
    up = low = digit = spec = False

    #Cek isi password
    for c in pw:
        if c.isupper():
            up = True
        if c.islower():
            low = True
        if c.isdigit():
            digit = True
        if c in special:
            spec = True
    
    #Jika semua syarat terpenuhi
    return up and low and digit and spec 

# 5. Registrasi User
def register():
    print ("\n Selamat Datang New Member, Silakan Registrasi")
    print ("Masukkan Data Diri Anda:")

    # *UserId*
    while True:
        uid = input ("UserID:")
        if validate_userid(uid):
            break
        print ("UserId salah / sudah ada")
        print ("Masukkan user id kembali")

    #*Password*
    while True:
        pw= input ("Password:")
        if validate_password(pw):
            break
        print ("Password tidak memenuhi Syarat")
        print ("Masukkan password kembali")
    
    #*Email*
    while True:
        email = input ("Email:")
        if validate_email(email):
            break
        print ("Format Email Salah ")
        print ("Masukkan Email kembali")

    #*Nama*
    while True:
        nama = input ("Nama:")
        if nama.strip() != "" and all(c.isalpha() or c == " " for c in nama):
            break
        print("Nama hanya boleh alfabet")
        print ("Masukkan Nama kembali")
    
    #*Gender*
    while True:
        gender = input ("Gender (Pria/Wanita):")
        if gender.lower() in ["pria", "wanita"]:
            break
        print("Masukan Pria/ Wanita")
        print ("Masukkan Gender kembali")
    
    #*Usia*
    while True:
        usia = input ("Usia:")
        if only_int(usia):
            usia = int(usia)
            if 17 <= usia <= 80: 
                break
        print("Usia harus 17 - 80")
        print ("Masukkan Usia kembali")

    #Pekerjaan
    while True:
        job = input ("Pekerjaan:")
        if only_alpha(job): 
            break
        print("Pekerjaan hanya boleh alphabet")
        print ("Masukkan Pekerjaan kembali")
    
    #Hobi
    while True:
        hobby = input ("Hobi (masukkan lebih dari satu):")
        hobby_kata = hobby.split()

        #Cek apakah sudah lebih dari satu alfabet
        if len(hobby_kata) > 1 and all(w.isalpha() for w in hobby_kata):
            break
        print("Hobi minimal dua kata alfabet")
        print("Masukkan Hobi kembali")

    #Alamat
    print("\nAlamat")

    while True:
        kota = input ("Nama Kota:")
        if only_alpha(kota):
            break
        print("Nama kota harus alfabet")

    while True:
        rt = input ("RT:")
        if only_int(rt):
            break
        print("Format RT harus angka")

    while True:
        rw= input ("RW:")
        if only_int(rw):
            break
        print("Format RW harus angka")

    while True:
        zipcode= input ("Zip Code:")
        if only_int(zipcode) and len (zipcode) == 5:
            break
        print("Format ZIP harus angka dan 5 digit")

    #titik kordinat
    print ("\nGeo")

    while True:
        lat = input ("Lat:")
        if only_float(lat):
            break
        print("Format latitude salah")
    
    while True:
        longtitude = input ("Longitude:")
        if only_float(longtitude):
            break
        print ("Format Longtitude salah")
    
    #Nomor HP
    while True: 
        hp = input ("No Hp:")
        if only_int (hp) and 11 <= len(hp) <= 13: 
            break
        print ("Nomor Hp harus 11 - 13 angka")

    #Simpan Data User
    print("\n Akun Registrasi")
    confim = input ("Simpan data (Y/N):")

    if confim.lower() == "y":
        #Simpan ke dictionary users
        users[uid] = {
            "password": pw,
            "name": nama,
            "email": email,
            "gender": gender,
            "usia": usia,
            "pekerjaan": job,
            "hobi": hobby,
            "alamat": {
                "kota":kota,
                "rt": rt,
                "rw": rw,
                "zip": zipcode,
                "lat": lat,
                "long": longtitude,
            },
            "nomor_hp": hp, 
        }
        print ("Data tersimpan")
    else:
        print ("Data tidak tersimpan")

# 6. Login
def login():
    print("\n====== Login ======")

    percobaan = 0

    #Maksimal 5 kali percobaan
    while percobaan < 5:
        uid = input ("Masukkan Userid:")
        pw = input("Masukkan Password:")

        #Jika ID tidak ditemukan
        if uid not in users:
            print ("ID Tidak Terdaftar")
            percobaan +=1
            print (f"percobaan ({percobaan}/5)")
            continue
        
        #Jika Password salah
        if users[uid] ["password"] != pw:
            print ("Password anda Salah")
            percobaan += 1
            print (f"percobaan ({percobaan}/5)")
            continue

        #Jika Login berhasil
        print ("Login Berhasil")
        return uid
    
    print ("login gagal 5x anda tidak dapat login sementara")
    return None

# 7. Profil User
def profile(uid):
    u = users [uid]

    print("\nData Anda")
    print("Nama :", u["name"])
    print("Email :", u["email"])
    print("Gender :", u["gender"])
    print("Usia :", u["usia"])
    print("Pekerjaan :", u["pekerjaan"])
    print("Hobi :", u["hobi"])

    print("\nAlamat")
    print("Kota :", u["alamat"]["kota"])
    print("RT :", u["alamat"]["rt"])
    print("RW :", u["alamat"]["rw"])
    print("Zip :", u["alamat"]["zip"])

    print("\nGeo")
    print("Lat :", u["alamat"]["lat"])
    print("Longitude :", u["alamat"]["long"])

    print("No HP :", u["nomor_hp"])

#8. Menu Utama auth

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    pilih = input("Pilih: ")

    if pilih == "1":
        register()

    elif pilih == "2":
        user = login()
        if user:
            profile(user)

    elif pilih == "3":
        break

    else:
        print("Pilihan salah")


