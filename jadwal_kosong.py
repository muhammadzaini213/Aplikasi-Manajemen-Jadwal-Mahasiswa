prodi_itk = ["Fisika", "Matematika", "Teknik Mesin", "Teknik Elektro", "Teknik Kimia", "Teknik Material dan Metalurgi", "Teknik Sipil", "Perencanaan Wilayah dan Kota", "Teknik Perkapalan", "Sistem Informasi", "Informatika", "Teknik Industri", "Teknik Lingkungan", "Teknik Kelautan", "Arsitektur", "Statistika", "Ilmu Aktuaria", "Rekayasa Keselamatan", "Teknologi Pangan", "Bisnis Digital", "Teknik Logistik", "Desain Komunikasi Visual"] 
sesi_itk = ["Senin, Sesi 1","Senin, Sesi 2", "Senin, Sesi 3", "Senin, Sesi 4", "Selasa, Sesi 1", "Selasa, Sesi 2", "Selasa, Sesi 3", "Selasa, Sesi 4", "Rabu, Sesi 1","Rabu, Sesi 2","Rabu, Sesi 3", "Rabu, Sesi 4", "Kamis, Sesi 1", "Kamis, Sesi 2", "Kamis, Sesi 3", "Kamis, Sesi 4", "Jumat, Sesi 1", "Jumat, Sesi 2", "Jumat, Sesi 3","Jumat, Sesi 4"]

def fixFormat(path):
    dataMahasiswa = open(path, "r")
    data = dataMahasiswa.read()

    with open (path, 'w') as file:
        file.write(data.replace("'", ""))    

def listMatkul(line):
    listMatkul = line[0]
    listMatkul = listMatkul.replace("\t\t", "\t")
    listMatkul = listMatkul.split("\t")
    listMatkul = listMatkul[:-1]
    return listMatkul

def sorting(listSesi):
    listSesiSorted = []
    hari_order = ["Senin", "Selasa","Rabu","Kamis","Jumat"]
    sesi_order = ["1", "2", "3", "4"]
    for i in range (0, len(hari_order)):
        for j in range (0, len(sesi_order)):
            for k in range(0, len(listSesi)):
                if(listSesi[k].startswith(f"{hari_order[i]}, Sesi {sesi_order[j]}") or listSesi[k].startswith(f"{hari_order[i]} Sesi {sesi_order[j]}")):
                    listSesiSorted.append(listSesi[k])

    return listSesiSorted

def jadwalNIM(listJadwal, text):
    found = False
    listDitemukan=""
    for i in range (0, len(listJadwal), 2):
        if (text.lower() in listJadwal[i].lower()):
            listDitemukan = f"\n{listDitemukan}{listJadwal[i]}\n"
            for j in range (0, len(listJadwal[i+1])):
                if(listJadwal[i+1][j]):
                    print(listJadwal[i+1][j])
                    listDitemukan = f"{listDitemukan}{listJadwal[i+1][j]}\n"
                    found = True
    if(found == False):
        return "Tidak ditemukan."
    else:
        return(listDitemukan)

def jadwalKosong(listJadwal): 
    listJadwalKosong = []
    for kolom in range(1, len(listJadwal),2):
        order = sesi_itk
        for i in listJadwal[kolom]:
            for j in order:
                if j in i:
                    order.remove(j)
        listJadwalKosong.append(listJadwal[kolom-1])
        listJadwalKosong.append(order)

    return listJadwalKosong

def jadwalKosongNIM(jadwalKosong, find):
    found = False
    jadwalKosongDitemukan = ""
    for i in range (0, len(jadwalKosong), 2):
        if (find.lower() in jadwalKosong[i].lower()):
            jadwalKosongDitemukan = f"{jadwalKosongDitemukan}{jadwalKosong[i]}\n"
            for j in range (0, len(jadwalKosong[i+1])):
                if(jadwalKosong[i+1][j]):
                    jadwalKosongDitemukan = f"{jadwalKosongDitemukan}{jadwalKosong[i+1][j]}\n"
                    found = True
    if(found == False):
        return "Tidak ditemukan"
    else:
        return jadwalKosongDitemukan

def jadwalKosongProdi(jadwalKosong):
    jadwalKosongProdiDitemukan = ""
    count = []
    for i in range(0,20):
        count.append(0)

    for i in range(0, len(sesi_itk)):
        for j in range(1, len(jadwalKosong),2):
            for k in jadwalKosong[j]:
                # print(jadwalKosong[j])
                if(sesi_itk[i] in k):
                    count[i] = count[i] + 1

    for list in range(0,20):
        jadwalKosongProdiDitemukan = f"{jadwalKosongProdiDitemukan}{sesi_itk[list]}: {count[list]} mahasiswa kosong\n"

    return jadwalKosongProdiDitemukan
    
def jadwalKosongSesi(jadwalKosong, sesi):
    jadwalKosongSesiDitemukan = ""
    for i in range(1, len(jadwalKosong), 2):
        if(sesi in jadwalKosong[i]):
            jadwalKosongSesiDitemukan = f"{jadwalKosongSesiDitemukan}{jadwalKosong[i-1]}\n"
    if(jadwalKosongSesiDitemukan == ""):
        return f"Tidak ada mahasiswa kosong saat {sesi}"
    else:
        return jadwalKosongSesiDitemukan



listJadwal = []

def openData(path):
    fixFormat(path)

    with open(path, 'r') as file:
        line = file.read().split("\n")
        matkul = listMatkul(line)

        listJadwal.clear()
        for mahasiswa in range (1, len(line)):
            column = line[mahasiswa].split("\t")
            nim = column[0]
            nama = column[1]
            
            matkulDanKelas = []
            listSesi = []

            for sesi in range(3, len(column), 2):
                listSesi.append(column[sesi])

            for mataKuliah in range (0, len(listSesi)):
                listSesi[mataKuliah] = f"{listSesi[mataKuliah]} {matkul[mataKuliah][:-10]}"

            listKelas = []

            for kelas in range (2, len(column), 2):
                listKelas.append(column[kelas])
            
            
            for matkulKelas in range (0, len(listSesi)):
                matkulDanKelas.append(f"{listSesi[matkulKelas]}{listKelas[matkulKelas]}")

            matkulDanKelas = sorting(matkulDanKelas)
            listJadwal.append(f"{nama} - {nim}")
            listJadwal.append(matkulDanKelas)

openData("mahasiswa/fisika.txt")

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Manajemen Jadwal")
root.state('zoomed') 

button_font = ("Helvetica", 18)
label_font = ("Helvetica", 16)

frame_menu_awal = tk.Frame(root)
frame_menu_awal.pack(expand=True)

def back_to_menu():
    frame_lihat_jadwal.pack_forget()
    frame_jadwal_kosong_opsi.pack_forget()  
    frame_cek_list.pack_forget()
    frame_menu_awal.pack(expand=True)  

# Menu Awal
def menu_lihat_jadwal():
    frame_menu_awal.pack_forget()  
    frame_lihat_jadwal.pack(expand=True)  
    input_lihat_jadwal.bind("<KeyRelease>", search_input_jadwal_NIM)

def menu_jadwal_kosong():
    frame_menu_awal.pack_forget()  
    frame_jadwal_kosong_opsi.pack(expand=True)  

def menu_cek_list():
    frame_menu_awal.pack_forget()  
    frame_cek_list.pack(expand=True) 
    input_cek_list.bind("<KeyRelease>", cek_nim_dalam_list)


lihat_jadwal_btn = tk.Button(frame_menu_awal, text="Lihat Jadwal", font=button_font, command=menu_lihat_jadwal)
lihat_jadwal_btn.pack(fill=tk.X, pady=10, padx=50)
jadwal_kosong_btn = tk.Button(frame_menu_awal, text="Jadwal Kosong", font=button_font, command=menu_jadwal_kosong)
jadwal_kosong_btn.pack(fill=tk.X, pady=10, padx=50)
edit_jadwal_btn = tk.Button(frame_menu_awal, text="Edit Jadwal", font=button_font, command=lambda: print("Edit Jadwal"))
edit_jadwal_btn.pack(fill=tk.X, pady=10, padx=50)
cek_list_btn = tk.Button(frame_menu_awal, text="Cek List", font=button_font, command=menu_cek_list)
cek_list_btn.pack(fill=tk.X, pady=10, padx=50)
# Menu Awal

# Lihat Jadwal
def ubah_prodi_lihat_jadwal(event):
    prodi_dipilih = lihat_jadwal_prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")

def search_input_jadwal_NIM(event):
    input_value = input_lihat_jadwal.get()
    label_hasil_pencarian_lihat_jadwal.config(text=jadwalNIM(listJadwal, input_value))

frame_lihat_jadwal = tk.Frame(root)
label_lihat_jadwal = tk.Label(frame_lihat_jadwal, text="Masukkan Nama/NIM untuk mencari jadwal matkul", font=label_font)
label_lihat_jadwal.pack(pady=(20, 10))
frame_dropdown_prodi = tk.Frame(frame_lihat_jadwal)
frame_dropdown_prodi.pack(pady=(0, 20), padx=50, fill=tk.X)
lihat_jadwal_prodi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
lihat_jadwal_prodi_combobox['values'] = prodi_itk 
lihat_jadwal_prodi_combobox.set("Pilih Prodi")
lihat_jadwal_prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))
lihat_jadwal_prodi_combobox.bind("<<ComboboxSelected>>", ubah_prodi_lihat_jadwal)
input_lihat_jadwal = tk.Entry(frame_lihat_jadwal, font=label_font)
input_lihat_jadwal.pack(pady=(0, 20), padx=50, fill=tk.X)
label_hasil_pencarian_lihat_jadwal = tk.Label(frame_lihat_jadwal, text="Hasil pencarian akan ditampilkan di sini", font=label_font)
label_hasil_pencarian_lihat_jadwal.pack(pady=10)
frame_tombol_kembali = tk.Frame(frame_lihat_jadwal)
frame_tombol_kembali.pack(pady=(20, 10))
kembali_btn = tk.Button(frame_tombol_kembali, text="Kembali", font=button_font, command=back_to_menu)
kembali_btn.pack(side=tk.LEFT, padx=(0, 10))
# Lihat Jadwal


# Jadwal Kosong Opsi
def cari_jadwal_kosong_individu(event):
    input_value = input_jadwal_kosong_individu.get()
    label_hasil_pencarian_jadwal_kosong_individu.config(text=jadwalKosongNIM(jadwalKosong(listJadwal), input_value))

def show_jadwal_kosong_individu():
    frame_jadwal_kosong_individu.pack(expand=True)  
    frame_jadwal_kosong_opsi.pack_forget() 
    input_jadwal_kosong_individu.bind("<KeyRelease>", cari_jadwal_kosong_individu)

def show_jadwal_kosong_prodi():
    frame_jadwal_kosong_prodi.pack(expand=True)
    frame_jadwal_kosong_opsi.pack_forget() 

def show_jadwal_kosong_sesi():
    frame_jadwal_kosong_opsi.pack_forget() 
    frame_jadwal_kosong_sesi.pack(expand=True)

frame_jadwal_kosong_opsi = tk.Frame(root)
jadwal_kosong_individu_btn = tk.Button(frame_jadwal_kosong_opsi, text="Jadwal Kosong Individu", font=button_font, command=show_jadwal_kosong_individu)
jadwal_kosong_individu_btn.pack(fill=tk.X, pady=10, padx=50)
jadwal_kosong_prodi_btn = tk.Button(frame_jadwal_kosong_opsi, text="Jadwal Kosong Prodi", font=button_font, command=show_jadwal_kosong_prodi)
jadwal_kosong_prodi_btn.pack(fill=tk.X, pady=10, padx=50)
jadwal_kosong_sesi_btn = tk.Button(frame_jadwal_kosong_opsi, text="Jadwal Kosong Sesi", font=button_font, command=show_jadwal_kosong_sesi)
jadwal_kosong_sesi_btn.pack(fill=tk.X, pady=10, padx=50)
kembali_btn = tk.Button(frame_jadwal_kosong_opsi, text="Kembali", font=button_font, command=back_to_menu)
kembali_btn.pack(side=tk.LEFT, padx=(0, 10), pady=20)
# Jadwal Kosong Opsi


def kembali_ke_menu_jadwal_kosong():
    frame_jadwal_kosong_opsi.pack(expand=True)  
    frame_jadwal_kosong_individu.pack_forget()
    frame_jadwal_kosong_prodi.pack_forget()
    frame_jadwal_kosong_sesi.pack_forget()

# Jadwal Kosong Individu
def ubah_prodi_jadwal_kosong_individu(event):
    prodi_dipilih = jadwal_kosong_individu_prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")
frame_jadwal_kosong_individu = tk.Frame(root)
label_jadwal_kosong_individu = tk.Label(frame_jadwal_kosong_individu, text="Masukkan Nama/NIM untuk mencari jadwal kosong", font=label_font)
label_jadwal_kosong_individu.pack(pady=(20, 10))
frame_dropdown_prodi = tk.Frame(frame_jadwal_kosong_individu)
frame_dropdown_prodi.pack(pady=(0, 20), padx=50, fill=tk.X)
jadwal_kosong_individu_prodi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
jadwal_kosong_individu_prodi_combobox['values'] = prodi_itk 
jadwal_kosong_individu_prodi_combobox.set("Pilih Prodi")
jadwal_kosong_individu_prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))
jadwal_kosong_individu_prodi_combobox.bind("<<ComboboxSelected>>", ubah_prodi_jadwal_kosong_individu)
input_jadwal_kosong_individu = tk.Entry(frame_jadwal_kosong_individu, font=label_font)
input_jadwal_kosong_individu.pack(pady=(0, 20), padx=50, fill=tk.X)
label_hasil_pencarian_jadwal_kosong_individu = tk.Label(frame_jadwal_kosong_individu, text="Hasil pencarian akan ditampilkan di sini", font=label_font)
label_hasil_pencarian_jadwal_kosong_individu.pack(pady=10)
frame_tombol_kembali = tk.Frame(frame_jadwal_kosong_individu)
frame_tombol_kembali.pack(pady=(20, 10))
kembali_btn = tk.Button(frame_tombol_kembali, text="Kembali", font=button_font, command=kembali_ke_menu_jadwal_kosong)
kembali_btn.pack(side=tk.LEFT, padx=(0, 10))
# Jadwal Kosong Individu

# Jadwal Kosong Prodi
def ubah_prodi_jadwal_kosong_prodi(event):
    prodi_dipilih = jadwal_kosong_prodi_prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")
    label_hasil_pencarian_jadwal_kosong_prodi.config(text=jadwalKosongProdi(jadwalKosong(listJadwal)))
frame_jadwal_kosong_prodi = tk.Frame(root)
label_jadwal_kosong_prodi = tk.Label(frame_jadwal_kosong_prodi, text="Masukkan Nama/NIM untuk mencari jadwal kosong prodi", font=label_font)
label_jadwal_kosong_prodi.pack(pady=(20, 10))
frame_dropdown_prodi = tk.Frame(frame_jadwal_kosong_prodi)
frame_dropdown_prodi.pack(pady=(0, 20), padx=50, fill=tk.X)
jadwal_kosong_prodi_prodi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
jadwal_kosong_prodi_prodi_combobox['values'] = prodi_itk 
jadwal_kosong_prodi_prodi_combobox.set("Pilih Prodi")
jadwal_kosong_prodi_prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))
jadwal_kosong_prodi_prodi_combobox.bind("<<ComboboxSelected>>", ubah_prodi_jadwal_kosong_prodi)
label_hasil_pencarian_jadwal_kosong_prodi = tk.Label(frame_jadwal_kosong_prodi, text="Hasil pencarian akan ditampilkan di sini", font=label_font)
label_hasil_pencarian_jadwal_kosong_prodi.pack(pady=10)
frame_tombol_kembali = tk.Frame(frame_jadwal_kosong_prodi)
frame_tombol_kembali.pack(pady=(20, 10))
kembali_btn = tk.Button(frame_tombol_kembali, text="Kembali", font=button_font, command=kembali_ke_menu_jadwal_kosong)
kembali_btn.pack(side=tk.LEFT, padx=(0, 10))
# Jadwal Kosong Prodi


# Jadwal Kosong Sesi
def ubah_prodi_jadwal_kosong_sesi(event):
    prodi_dipilih = jadwal_kosong_sesi_prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")
def ubah_sesi_jadwal_kosong_sesi(event):
    sesi_dipilih = jadwal_kosong_sesi_sesi_combobox.get()
    label_hasil_pencarian_jadwal_kosong_sesi.config(text=jadwalKosongSesi(jadwalKosong(listJadwal), sesi_dipilih))

frame_jadwal_kosong_sesi = tk.Frame(root)
label_jadwal_kosong_sesi = tk.Label(frame_jadwal_kosong_sesi, text="Masukkan Nama/NIM untuk mencari jadwal kosong prodi", font=label_font)
label_jadwal_kosong_sesi.pack(pady=(20, 10))
frame_dropdown_prodi = tk.Frame(frame_jadwal_kosong_sesi)
frame_dropdown_prodi.pack(pady=(0, 20), padx=50, fill=tk.X)
jadwal_kosong_sesi_prodi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
jadwal_kosong_sesi_prodi_combobox['values'] = prodi_itk 
jadwal_kosong_sesi_prodi_combobox.set("Pilih Prodi")
jadwal_kosong_sesi_prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))
jadwal_kosong_sesi_prodi_combobox.bind("<<ComboboxSelected>>", ubah_prodi_jadwal_kosong_sesi)
jadwal_kosong_sesi_sesi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
jadwal_kosong_sesi_sesi_combobox['values'] = sesi_itk
jadwal_kosong_sesi_sesi_combobox.set("Pilih Sesi")
jadwal_kosong_sesi_sesi_combobox.pack(side=tk.LEFT, padx=(10, 0))
jadwal_kosong_sesi_sesi_combobox.bind("<<ComboboxSelected>>", ubah_sesi_jadwal_kosong_sesi)

label_hasil_pencarian_jadwal_kosong_sesi = tk.Label(frame_jadwal_kosong_sesi, text="Hasil pencarian akan ditampilkan di sini", font=label_font)
label_hasil_pencarian_jadwal_kosong_sesi.pack(pady=10)
frame_tombol_kembali = tk.Frame(frame_jadwal_kosong_sesi)
frame_tombol_kembali.pack(pady=(20, 10))
kembali_btn = tk.Button(frame_tombol_kembali, text="Kembali", font=button_font, command=kembali_ke_menu_jadwal_kosong)
kembali_btn.pack(side=tk.LEFT, padx=(0, 10))
# Jadwal Kosong Sesi



# Cek List
def ubah_prodi_cek_list(event):
    prodi_dipilih = cek_list_prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")

def cek_nim_dalam_list(event):
    input_value = input_cek_list.get()
    label_hasil_pencarian_cek_list.config(text=cekList(listJadwal, input_value))

def cekList(listJadwal, list):
    tidakDitemukan = "NIM yang belum list:"
    for i in range(0, len(listJadwal), 2):
        if(listJadwal[i].split("-")[1][1:] not in list):
            tidakDitemukan = f"{tidakDitemukan}{listJadwal[i]}\n"
    return tidakDitemukan

frame_cek_list = tk.Frame(root)
label_cek_list = tk.Label(frame_cek_list, text="Masukkan list untuk mengetahui nim yang tidak ada", font=label_font)
label_cek_list.pack(pady=(20, 10))
frame_dropdown_prodi = tk.Frame(frame_cek_list)
frame_dropdown_prodi.pack(pady=(0, 20), padx=50, fill=tk.X)
cek_list_prodi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
cek_list_prodi_combobox['values'] = prodi_itk 
cek_list_prodi_combobox.set("Pilih Prodi")
cek_list_prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))
cek_list_prodi_combobox.bind("<<ComboboxSelected>>", ubah_prodi_cek_list)
input_cek_list = tk.Entry(frame_cek_list, font=label_font)
input_cek_list.pack(pady=(0, 20), padx=50, fill=tk.X)
label_hasil_pencarian_cek_list = tk.Label(frame_cek_list, text="Hasil pencarian akan ditampilkan di sini", font=label_font)
label_hasil_pencarian_cek_list.pack(pady=10)
frame_tombol_kembali = tk.Frame(frame_cek_list)
frame_tombol_kembali.pack(pady=(20, 10))
kembali_btn = tk.Button(frame_tombol_kembali, text="Kembali", font=button_font, command=back_to_menu)
kembali_btn.pack(side=tk.LEFT, padx=(0, 10))
# Cek List

root.mainloop()


