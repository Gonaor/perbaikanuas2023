# Ini adalah modul anggota

# Block Import
from datetime import date
from random import choices
from json import load, dump
from os import path, getcwd, system

# Fungsi lain-lain untuk membantu
def generate_idanggota():
    ls_ap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ls_num = "0123456789"
    return ''.join(choices(ls_num, k=5))

# Fungsi menambah anggota
def tambah_anggota(nama, alamat, telp):
    # Buka JSON 
    with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
        content = load(file)
        
    hari_ini = date.today().strftime("%Y-%m-%d")
    
    while True:
        try:
            id_baru = generate_idanggota()
            assert id_baru not in content
            break
        except AssertionError:
            continue
    
    content[id_baru] = {
            "idanggota" : id_baru,
            "nama"      : nama,
            "alamat"    : alamat,
            "tanggal"   : hari_ini,
            "telepon"   : f"+62{telp}"
    }
    
    with open("anggotas.json", "w") as file:
        dump(content, file, indent= 4)
        
    print("Add successfully")
    input("Tekan enter untuk lanjut ")

# Fungsi cari anggota
def cari_anggota_by_id(id_dicari):
    # Buka JSON 
    with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
        content = load(file)
    
    if id_dicari in content:
        return content[id_dicari]
    else:
        return {}

# Fungsi tampilkan anggota
def tampilkan_anggota(dc):
    if dc == {}:
        print("Tidak ada anggota !")
    else:
        id = dc["idanggota"]
        nama = dc["nama"]
        alamat = dc["alamat"]
        telp = dc["telepon"]
        tgl = dc["tanggal"]
        
        print(f"""ID Anggota      : {id} 
Nama            : {nama}
Alamat          : {alamat} 
Telepon         : {telp}
Tanggal Daftar  : {tgl}""")
    
    input("Tekan enter untuk lanjut ")
    
    
# Fungsi mengedit anggota
def edit_anggota():
    while True:
        # Buka JSON 
        with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
            content = load(file)
        
        # Cari anggota by id
        dicari = input("Ketik ID anggota yang akan diedit : ")
        ketemu = cari_anggota_by_id(dicari)
        
        if ketemu == {}:
            print("Data anggota tidak ditemukan !")
            
            while True:
                try:
                    ulang = input("Cari lagi (Y/y = Ya, T/t = Tidak)?")
                    assert ulang.lower() in ["y", "t"], "Input tidak valid"
                    break
                except AssertionError as er:
                    print(er)
            
            if ulang.lower() == "y":
                system("cls")
            else:
                input("Tekan enter untuk kembali ke menu utama ")
                break
        else:
            id = ketemu["idanggota"]
            nama = ketemu["nama"]
            alamat = ketemu["alamat"]
            telp = ketemu["telepon"]
            
            nama_baru = input(f"Nama : {nama} -> ")
            if nama_baru.strip() != "":
                ketemu["nama"] = nama_baru
                
            alamat_baru = input(f"Alamat : {alamat} -> ")
            if alamat_baru.strip() != "":
                ketemu["alamat"] = alamat_baru
                
            telp_baru = input(f"Telepon : {telp} -> ")
            if telp_baru.strip() != "":
                ketemu["telepon"] = f"+62{telp_baru}"
            
            content[id] = ketemu
            
            with open("anggotas.json", "w") as file:
                dump(content, file, indent= 4)
            
            break