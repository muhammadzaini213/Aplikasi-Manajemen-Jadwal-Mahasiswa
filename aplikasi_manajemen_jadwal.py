listJadwal = []

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

def jadwalindividu(listJadwal, text):
    found = False
    listDitemukan=""
    for i in range (0, len(listJadwal), 2):
        if (text.lower() in listJadwal[i].lower()):
            listDitemukan = f"\n{listDitemukan}{listJadwal[i]}\n"
            for j in range (0, len(listJadwal[i+1])):
                if(listJadwal[i+1][j]):
                    # print(listJadwal[i+1][j])
                    listDitemukan = f"{listDitemukan}{listJadwal[i+1][j]}\n"
                    found = True
    if(found == False):
        return "Tidak ditemukan."
    else:
        return(listDitemukan)

def jadwalKosong(listJadwal): 
    listJadwalKosong = []
    for kolom in range(1, len(listJadwal),2):
        order = ["Senin, Sesi 1","Senin, Sesi 2","Senin, Sesi 3","Senin, Sesi 4","Selasa, Sesi 1","Selasa, Sesi 2","Selasa, Sesi 3","Selasa, Sesi 4","Rabu, Sesi 1","Rabu, Sesi 2","Rabu, Sesi 3","Rabu, Sesi 4","Kamis, Sesi 1","Kamis, Sesi 2","Kamis, Sesi 3","Kamis, Sesi 4","Jumat, Sesi 1","Jumat, Sesi 2","Jumat, Sesi 3","Jumat, Sesi 4",]
        for i in listJadwal[kolom]:
            for j in order:
                if j in i:
                    order.remove(j)
        listJadwalKosong.append(listJadwal[kolom-1])
        listJadwalKosong.append(order)

    return listJadwalKosong

def jadwalKosongindividu(jadwalKosong, find):
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
    order =["Senin, Sesi 1","Senin, Sesi 2","Senin, Sesi 3","Senin, Sesi 4","Selasa, Sesi 1","Selasa, Sesi 2","Selasa, Sesi 3","Selasa, Sesi 4","Rabu, Sesi 1","Rabu, Sesi 2","Rabu, Sesi 3","Rabu, Sesi 4","Kamis, Sesi 1","Kamis, Sesi 2","Kamis, Sesi 3","Kamis, Sesi 4","Jumat, Sesi 1","Jumat, Sesi 2","Jumat, Sesi 3","Jumat, Sesi 4",]
    count = []
    for i in range(0,20):
        count.append(0)

    for i in range(0, len(order)):
        for j in range(1, len(jadwalKosong),2):
            for k in jadwalKosong[j]:
                # print(jadwalKosong[j])
                if(order[i] in k):
                    count[i] = count[i] + 1

    for list in range(0,20):
        jadwalKosongProdiDitemukan = f"{jadwalKosongProdiDitemukan}{order[list]}: {count[list]} mahasiswa kosong\n"

    return jadwalKosongProdiDitemukan
    
def jadwalKosongSesi(jadwalKosong, sesi):
    order = ["Senin, Sesi 1","Senin, Sesi 2","Senin, Sesi 3","Senin, Sesi 4","Selasa, Sesi 1","Selasa, Sesi 2","Selasa, Sesi 3","Selasa, Sesi 4","Rabu, Sesi 1","Rabu, Sesi 2","Rabu, Sesi 3","Rabu, Sesi 4","Kamis, Sesi 1","Kamis, Sesi 2","Kamis, Sesi 3","Kamis, Sesi 4","Jumat, Sesi 1","Jumat, Sesi 2","Jumat, Sesi 3","Jumat, Sesi 4",]
    
    jadwalKosongSesiDitemukan = ""
    for i in range(1, len(jadwalKosong), 2):
        if(sesi in jadwalKosong[i]):
            jadwalKosongSesiDitemukan = f"{jadwalKosongSesiDitemukan}{jadwalKosong[i-1]}\n"

    if(jadwalKosongSesiDitemukan == ""):
        return f"Tidak ada mahasiswa kosong saat {sesi}"
    else:
        return jadwalKosongSesiDitemukan

def openData(path):
    with open(path, 'r') as file:
        line = file.read().split("\n")
        matkul = line[0].replace("\t\t", "\t").split("\t")[:-1]

        listJadwal.clear()
        for mahasiswa in range (1, len(line)):
            column = line[mahasiswa].split("\t")
            individu = column[0]
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
            listJadwal.append(f"{nama} - {individu}")
            listJadwal.append(matkulDanKelas)

openData("mahasiswa/fisika.txt")

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Manajemen Jadwal")
root.state('zoomed') 
button_font = ("Helvetica", 18)
label_font = ("Helvetica", 16)
frame = tk.Frame(root)
frame_dropdown_prodi = tk.Frame(frame)
frame_dropdown_prodi.pack(pady=(0, 20), padx=50, fill=tk.X)
label= tk.Label(frame, text="Masukkan Nama/NIM untuk mencari jadwal matkul", font=label_font)
label.pack(pady=(20, 10))
prodi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
prodi_combobox['values'] = ["Fisika", "Matematika", "Teknik Mesin", "Teknik Elektro", "Teknik Kimia", "Teknik Material dan Metalurgi", "Teknik Sipil", "Perencanaan Wilayah dan Kota", "Teknik Perkapalan", "Sistem Informasi", "Informatika", "Teknik Industri", "Teknik Lingkungan", "Teknik Kelautan", "Arsitektur", "Statistika", "Ilmu Aktuaria", "Rekayasa Keselamatan", "Teknologi Pangan", "Bisnis Digital", "Teknik Logistik", "Desain Komunikasi Visual"]  
prodi_combobox.set("Pilih Prodi")
prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))
sesi_combobox = ttk.Combobox(frame_dropdown_prodi, font=label_font, state="readonly")
sesi_combobox['values'] = ["Senin, Sesi 1","Senin, Sesi 2","Senin, Sesi 3","Selasa, Sesi 1","Selasa, Sesi 3","Rabu, Sesi 1","Rabu, Sesi 3","Rabu, Sesi 4","Kamis, Sesi 1","Kamis, Sesi 2","Kamis, Sesi 3","Kamis, Sesi 4","Jumat, Sesi 1","Jumat, Sesi 2","Jumat, Sesi 3","Jumat, Sesi 4"]  
sesi_combobox.set("Pilih Sesi")
sesi_combobox.pack(side=tk.LEFT, padx=(10, 0))
input = tk.Entry(frame, font=label_font)
input.pack(pady=(0, 20), padx=50, fill=tk.X)
frame_hasil_pencarian = tk.Frame(frame)
frame_hasil_pencarian.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
scrollbar_hasil = ttk.Scrollbar(frame_hasil_pencarian, orient=tk.VERTICAL)
text_hasil_pencarian = tk.Text(frame_hasil_pencarian, font=label_font, wrap=tk.WORD, yscrollcommand=scrollbar_hasil.set, height=10, width=50)
scrollbar_hasil.config(command=text_hasil_pencarian.yview)
text_hasil_pencarian.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_hasil.pack(side=tk.RIGHT, fill=tk.Y)
text_hasil_pencarian.config(state=tk.DISABLED)

frame_tombol_kembali = tk.Frame(frame)
frame_tombol_kembali.pack(pady=(20, 10))

def back_to_menu():
    frame.pack_forget()
    frame_jadwal_kosong_opsi.pack_forget()  
    frame_menu_awal.pack(expand=True)  


def buatTombol(frame_tombol, teks, fungsi):
    tombol = tk.Button(frame_tombol, text=teks, font=button_font, command=fungsi)
    tombol.pack(fill=tk.X, pady=10, padx=50)


buatTombol(frame_tombol_kembali, "Kembali", back_to_menu)
def menu_jadwal_kosong():
    frame_menu_awal.pack_forget()  
    frame_jadwal_kosong_opsi.pack(expand=True) 

def openTools(key, prodiComboboxAction, sesiComboboxAction):
    frame_menu_awal.pack_forget() 
    frame_jadwal_kosong_opsi.pack_forget() 
    frame.pack(expand=True)  
    input.bind("<KeyRelease>", key)
    prodi_combobox.bind("<<ComboboxSelected>>", prodiComboboxAction)
    sesi_combobox.bind("<<ComboboxSelected>>", sesiComboboxAction)
    if key == None : input.unbind("<KeyRelease>")
    if prodi_combobox == None : prodi_combobox.unbind("<<ComboboxSelected>>")
    if sesi_combobox == None : sesi_combobox.unbind("<<ComboboxSelected>>")
    
def ubah_prodi(event):
    prodi_dipilih = prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")


def gantiTeks(output_teks):
    clean_result = "\n".join(line for line in output_teks.splitlines() if line.strip())
    text_hasil_pencarian.config(state=tk.NORMAL)
    text_hasil_pencarian.delete("1.0", tk.END)
    text_hasil_pencarian.insert(tk.END, clean_result)
    text_hasil_pencarian.config(state=tk.DISABLED)
    text_hasil_pencarian.yview_moveto(0)  

def cari_jadwal_individu(event):
    input_value = input.get()
    gantiTeks(jadwalindividu(listJadwal, input_value))

def cari_jadwal_kosong_individu(event):
    input_value = input.get()
    gantiTeks(jadwalKosongindividu(jadwalKosong(listJadwal), input_value))

    
def cek_individu_dalam_list(event):
    input_value = input.get()
    gantiTeks(cekList(listJadwal, input_value))
    

def cekList(listJadwal, list):
    tidakDitemukan = "NIM yang belum list:\n"
    for i in range(0, len(listJadwal), 2):
        if(listJadwal[i].split("-")[1][1:] not in list):
            tidakDitemukan = f"{tidakDitemukan}{listJadwal[i]}\n"
    return tidakDitemukan

def ubah_combobox_prodi(event):
    prodi_dipilih = prodi_combobox.get()
    openData(f"mahasiswa/{prodi_dipilih.lower()}.txt")
    gantiTeks(jadwalKosongProdi(jadwalKosong(listJadwal)))
    

def ubah_combobox_sesi(event):
    sesi_dipilih = sesi_combobox.get()
    gantiTeks(jadwalKosongSesi(jadwalKosong(listJadwal), sesi_dipilih))

frame_menu_awal = tk.Frame(root)
frame_menu_awal.pack(expand=True)

buatTombol(frame_menu_awal, "Lihat Jadwal",lambda: openTools(cari_jadwal_individu, ubah_prodi, {}))
buatTombol(frame_menu_awal, "Jadwal Kosong", menu_jadwal_kosong)
buatTombol(frame_menu_awal, "Edit Jadwal",lambda: {})
buatTombol(frame_menu_awal, "Cek List",lambda: openTools(cek_individu_dalam_list, ubah_prodi, {}))

frame_jadwal_kosong_opsi = tk.Frame(root)
buatTombol(frame_jadwal_kosong_opsi, "Jadwal Kosong Individu",lambda: openTools(cari_jadwal_kosong_individu, ubah_prodi, {}))
buatTombol(frame_jadwal_kosong_opsi, "Jadwal Kosong Prodi",lambda: openTools(None, ubah_combobox_prodi,None))
buatTombol(frame_jadwal_kosong_opsi, "Jadwal Kosong Sesi",lambda: openTools(None, ubah_prodi, ubah_combobox_sesi))
buatTombol(frame_jadwal_kosong_opsi, "Kembali", back_to_menu)

root.mainloop()
