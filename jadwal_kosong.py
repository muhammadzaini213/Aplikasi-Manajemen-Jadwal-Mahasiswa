import tkinter as tk
from tkinter import ttk

def fixFormat(path):
    dataMahasiswa = open(path, "r")
    data = dataMahasiswa.read()

    with open (path, 'w') as file:
        file.write(data.replace("'", ""))    

def lining(file):
    return file.read().split("\n")

def splitColumn(string):
    return string.split("\t")

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

def menuAwal(pil, listJadwal):
    if(pil == "1"):
        jadwalNIM(listJadwal)
        print("1. Jadwal\n2. Edit Jadwal\n3. Cek List")
        menuAwal(input(""), listJadwal)
    else:
        print("1. Jadwal\n2. Edit Jadwal\n3. Cek List")
        menuAwal(input(""), listJadwal)

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
        order = ["Senin, Sesi 1",
        "Senin, Sesi 2",
        "Senin, Sesi 3",
        "Senin, Sesi 4",
        "Selasa, Sesi 1",
        "Selasa, Sesi 2",
        "Selasa, Sesi 3",
        "Selasa, Sesi 4",
        "Rabu, Sesi 1",
        "Rabu, Sesi 2",
        "Rabu, Sesi 3",
        "Rabu, Sesi 4",
        "Kamis, Sesi 1",
        "Kamis, Sesi 2",
        "Kamis, Sesi 3",
        "Kamis, Sesi 4",
        "Jumat, Sesi 1",
        "Jumat, Sesi 2",
        "Jumat, Sesi 3",
        "Jumat, Sesi 4",]
        for i in listJadwal[kolom]:
            for j in order:
                if j in i:
                    order.remove(j)
        listJadwalKosong.append(listJadwal[kolom-1])
        listJadwalKosong.append(order)

    jadwalKosongSesi(listJadwalKosong)

def jadwalKosongNIM(jadwalKosong):
    find = input("Cari NIM/Nama?")
    found = False
    for i in range (0, len(jadwalKosong), 2):
        if (find.lower() in jadwalKosong[i].lower()):
            print(f"{jadwalKosong[i]}")
            for j in range (0, len(jadwalKosong[i+1])):
                if(jadwalKosong[i+1][j]):
                    print(jadwalKosong[i+1][j])
                    found = True
    if(found == False):
        print("Tidak ditemukan.")


def jadwalKosongBersama(jadwalKosong):
    order = ["Senin, Sesi 1",
        "Senin, Sesi 2",
        "Senin, Sesi 3",
        "Senin, Sesi 4",
        "Selasa, Sesi 1",
        "Selasa, Sesi 2",
        "Selasa, Sesi 3",
        "Selasa, Sesi 4",
        "Rabu, Sesi 1",
        "Rabu, Sesi 2",
        "Rabu, Sesi 3",
        "Rabu, Sesi 4",
        "Kamis, Sesi 1",
        "Kamis, Sesi 2",
        "Kamis, Sesi 3",
        "Kamis, Sesi 4",
        "Jumat, Sesi 1",
        "Jumat, Sesi 2",
        "Jumat, Sesi 3",
        "Jumat, Sesi 4",]
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
        print(f"{order[list]}: {count[list]} mahasiswa kosong")
    
def jadwalKosongSesi(jadwalKosong):
    order = ["Senin, Sesi 1",
        "Senin, Sesi 2",
        "Senin, Sesi 3",
        "Senin, Sesi 4",
        "Selasa, Sesi 1",
        "Selasa, Sesi 2",
        "Selasa, Sesi 3",
        "Selasa, Sesi 4",
        "Rabu, Sesi 1",
        "Rabu, Sesi 2",
        "Rabu, Sesi 3",
        "Rabu, Sesi 4",
        "Kamis, Sesi 1",
        "Kamis, Sesi 2",
        "Kamis, Sesi 3",
        "Kamis, Sesi 4",
        "Jumat, Sesi 1",
        "Jumat, Sesi 2",
        "Jumat, Sesi 3",
        "Jumat, Sesi 4",]
    for i in range(1, len(jadwalKosong), 2):
        if(order[2] in jadwalKosong[i]):
            print(jadwalKosong[i-1])


listJadwal = []

def openData(path):
    fixFormat(path)

    with open(path, 'r') as file:
        line = lining(file)
        matkul = listMatkul(line)

        listJadwal.clear()
        for mahasiswa in range (1, len(line)):
            column = splitColumn(line[mahasiswa])
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

# Initialize the main application window
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Manajemen Jadwal")
root.state('zoomed')  # Maximize window but keep title bar

# Define a function to log input text each time a key is released
def search_input(event):
    input_value = input_text.get()
    response_label.config(text=jadwalNIM(listJadwal, input_value))  # Update label with search result

# Define the function to show the "Lihat Jadwal" form
def show_lihat_jadwal():
    button_frame.pack_forget()  # Hide the button frame
    input_frame.pack(expand=True)  # Show the input frame

# Define the function to return to the main button layout (optional)
def back_to_menu():
    input_frame.pack_forget()  # Hide the input frame
    button_frame.pack(expand=True)  # Show the button frame

# Define the function for "Jadwal Kosong" button
def show_jadwal_kosong():
    button_frame.pack_forget()  # Hide the main button layout
    jadwal_kosong_frame.pack(expand=True)  # Show the "Jadwal Kosong" options

# Functions for the "Jadwal Kosong" options
def show_jadwal_kosong_individu():
    response_label.config(text="Menampilkan Jadwal Kosong Individu")

def show_jadwal_kosong_prodi():
    response_label.config(text="Menampilkan Jadwal Kosong Prodi")

def show_jadwal_kosong_sesi():
    response_label.config(text="Menampilkan Jadwal Kosong Sesi")

# Function to return to main menu from "Jadwal Kosong"
def back_to_main_menu():
    jadwal_kosong_frame.pack_forget()  # Hide the "Jadwal Kosong" options
    button_frame.pack(expand=True)  # Show the main button layout

# Set font for buttons and labels
button_font = ("Helvetica", 18)
label_font = ("Helvetica", 16)

# Create a frame to hold the buttons and center it vertically
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# Create the main buttons
button1 = tk.Button(button_frame, text="Lihat Jadwal", font=button_font, command=show_lihat_jadwal)
button1.pack(fill=tk.X, pady=10, padx=50)

button2 = tk.Button(button_frame, text="Jadwal Kosong", font=button_font, command=show_jadwal_kosong)
button2.pack(fill=tk.X, pady=10, padx=50)

button3 = tk.Button(button_frame, text="Edit Jadwal", font=button_font, command=lambda: print("Edit Jadwal"))
button3.pack(fill=tk.X, pady=10, padx=50)

button4 = tk.Button(button_frame, text="Cek List", font=button_font, command=lambda: print("Cek List"))
button4.pack(fill=tk.X, pady=10, padx=50)

# Create the "Lihat Jadwal" input frame
input_frame = tk.Frame(root)

# Input field and label for the "Lihat Jadwal" form
input_label = tk.Label(input_frame, text="Masukkan Jadwal:", font=label_font)
input_label.pack(pady=(20, 10))

input_dropdown_frame = tk.Frame(input_frame)
input_dropdown_frame.pack(pady=(0, 20), padx=50, fill=tk.X)

prodi_combobox = ttk.Combobox(input_dropdown_frame, font=label_font, state="readonly")
prodi_combobox['values'] = ["Fisika", "Matematika", "Teknik Mesin", "Teknik Elektro", "Teknik Kimia", "Teknik Material dan Metalurgi", "Teknik Sipil", "Perencanaan Wilayah dan Kota", "Teknik Perkapalan", "Sistem Informasi", "Informatika", "Teknik Industri", "Teknik Lingkungan", "Teknik Kelautan", "Arsitektur", "Statistika", "Ilmu Aktuaria", "Rekayasa Keselamatan", "Teknologi Pangan", "Bisnis Digital", "Teknik Logistik", "Desain Komunikasi Visual"]  # Dropdown options
prodi_combobox.set("Pilih Prodi")  # Default text
prodi_combobox.pack(side=tk.LEFT, padx=(10, 0))

def on_prodi_changed(event):
    selected_prodi = prodi_combobox.get()
    openData(f"mahasiswa/{selected_prodi.lower()}.txt")

prodi_combobox.bind("<<ComboboxSelected>>", on_prodi_changed)

input_text = tk.Entry(input_frame, font=label_font)
input_text.pack(pady=(0, 20), padx=50, fill=tk.X)

input_text.bind("<KeyRelease>", search_input)

response_label = tk.Label(input_frame, text="Hasil pencarian akan ditampilkan di sini", font=label_font)
response_label.pack(pady=10)

button_frame_bottom = tk.Frame(input_frame)
button_frame_bottom.pack(pady=(20, 10))

back_button = tk.Button(button_frame_bottom, text="Kembali", font=button_font, command=back_to_menu)
back_button.pack(side=tk.LEFT, padx=(0, 10))

# Create the frame for the "Jadwal Kosong" options
jadwal_kosong_frame = tk.Frame(root)

# New buttons for Jadwal Kosong options
button1_kosong = tk.Button(jadwal_kosong_frame, text="Jadwal Kosong Individu", font=button_font, command=show_jadwal_kosong_individu)
button1_kosong.pack(fill=tk.X, pady=10, padx=50)

button2_kosong = tk.Button(jadwal_kosong_frame, text="Jadwal Kosong Prodi", font=button_font, command=show_jadwal_kosong_prodi)
button2_kosong.pack(fill=tk.X, pady=10, padx=50)

button3_kosong = tk.Button(jadwal_kosong_frame, text="Jadwal Kosong Sesi", font=button_font, command=show_jadwal_kosong_sesi)
button3_kosong.pack(fill=tk.X, pady=10, padx=50)

# Back button for returning to main menu from "Jadwal Kosong"
back_button_kosong = tk.Button(jadwal_kosong_frame, text="Kembali", font=button_font, command=back_to_main_menu)
back_button_kosong.pack(side=tk.LEFT, padx=(0, 10), pady=20)

root.mainloop()

        
        