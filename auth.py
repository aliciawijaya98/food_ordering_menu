#Dictionary untuk menyimpan semua data user
users = {}

#============Bagian Validator =============
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

#============ Validasi Email =============
def validate_email(email):
    #Email harus punya satu @ 
    if email.count("@") != 1:
        return False
    
    #Pisahkan username dan domain
    user, domain = email.split("@")

    #Username tidak boleh kosong dan domain harus punya titik
    if user == ""or "." not in domain:
        return False
    
    #Karakter pertama username harus huruf/angka
    if not user[0].isalnum():
        return False
    
    #Username hanya boleh huruf, angka, . dan _
    for c in user:
        if not (c.isalnum() or c in"._"):
            return False
    
    return True

#============ Validasi Email =============
def validate_userid(uid):
    #Panjgan minimal dan maksimal
    if len(uid) < 6 or len(uid) > 20:
        return False

    has_letter = False
    has_digit = False
    
     