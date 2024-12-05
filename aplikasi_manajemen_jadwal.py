dataJadwal = []

# List
prodi = ["Fisika", "Matematika", "Teknik Mesin", "Teknik Elektro", "Teknik Kimia", "Teknik Material dan Metalurgi", "Teknik Sipil", "Perencanaan Wilayah dan Kota", "Teknik Perkapalan", "Sistem Informasi", "Informatika", "Teknik Industri", "Teknik Lingkungan", "Teknik Kelautan", "Arsitektur", "Statistika", "Ilmu Aktuaria", "Rekayasa Keselamatan", "Teknologi Pangan", "Bisnis Digital", "Teknik Logistik", "Desain Komunikasi Visual"] 
sesi = ["Senin, Sesi 1","Senin, Sesi 2","Senin, Sesi 3","Senin, Sesi 4","Selasa, Sesi 1","Selasa, Sesi 2","Selasa, Sesi 3","Selasa, Sesi 4","Rabu, Sesi 1","Rabu, Sesi 2","Rabu, Sesi 3","Rabu, Sesi 4","Kamis, Sesi 1","Kamis, Sesi 2","Kamis, Sesi 3","Kamis, Sesi 4","Jumat, Sesi 1","Jumat, Sesi 2","Jumat, Sesi 3","Jumat, Sesi 4"]

def sorting(listSesi):
    listSesiSorted = []
    for urutan in range(0, len(sesi)):
        for jadwalMahasiswa in range(0, len(listSesi)):
            if(listSesi[jadwalMahasiswa].startswith(sesi[urutan])):
                listSesiSorted.append(listSesi[jadwalMahasiswa])     
    return listSesiSorted

def jadwalindividu(dataJadwal, namaNim):
    found = False
    jadwalDitemukan=""
    for data in range (0, len(dataJadwal), 2):
        if (namaNim.lower() in dataJadwal[data].lower()):
            jadwalDitemukan = f"\n{jadwalDitemukan}{dataJadwal[data]}\n" # Ini bakal nyari berdasarkan nama/nim
            for j in range (0, len(dataJadwal[data+1])):
                if(dataJadwal[data+1][j]):
                    jadwalDitemukan = f"{jadwalDitemukan}{dataJadwal[data+1][j]}\n" # ini akan menambahkan jadwal berdasarkan nama/nim yang ditemukan
                    found = True
    if(found == False): return "Nama/NIM Tidak ditemukan didalam data yang disimpan."
    else: return(jadwalDitemukan)

def jadwalKosong(dataJadwal, opsi): 
    dataJadwalKosong = []
    for indeksJadwal in range(1, len(dataJadwal),2):
        listSesiKosong = sesi.copy()
        for jadwalMahasiswa in dataJadwal[indeksJadwal]: 
            for jadwalMatkul in listSesiKosong: 
                if jadwalMatkul in jadwalMahasiswa: listSesiKosong.remove(jadwalMatkul)
        dataJadwalKosong.append(dataJadwal[indeksJadwal-1])
        dataJadwalKosong.append(listSesiKosong)

    if(opsi == 1):
        jadwalKosongProdiDitemukan = ""
        listSesi = sesi.copy()
        count = []
        for sesiAktif in range (0, len(listSesi)):
            for mahasiswa in range(1, len(dataJadwalKosong), 2):
                for k in dataJadwalKosong[mahasiswa]:
                    count.append(0)
                    if(listSesi[sesiAktif] in k): count[sesiAktif] = count[sesiAktif] + 1

        for totalKosong in range (0, len(listSesi)):
            jadwalKosongProdiDitemukan = f"{jadwalKosongProdiDitemukan}{listSesi[totalKosong]}: {count[totalKosong]} mahasiswa kosong\n"
        return jadwalKosongProdiDitemukan
    
    elif(opsi == 2):
        jadwalKosongSesiDitemukan = ""
        for i in range(1, len(dataJadwalKosong), 2):
            if(dropdownJadwalKosongSesi.get() in dataJadwalKosong[i]): 
                jadwalKosongSesiDitemukan = f"{jadwalKosongSesiDitemukan}{dataJadwalKosong[i-1]}\n"
        if(jadwalKosongSesiDitemukan == ""): 
            return f"Tidak ada mahasiswa prodi {dropdownCariProdiKosong.get()} yang kosong saat {dropdownJadwalKosongSesi.get()}"
        else: 
            return jadwalKosongSesiDitemukan
        
def bukaData(path):
    with open(path, 'r') as file:
        line = file.read().split("\n")

        matkul = line[0].replace("\t\t", "\t").split("\t")[:-1]
        dataJadwal.clear()
        for mahasiswa in range (1, len(line)):
            column = line[mahasiswa].split("\t")
            individu = column[0]
            nama = column[1]
            matkulDanKelas, listSesi, listKelas= [], [], []

            for sesi in range(3, len(column), 2):
                listSesi.append(column[sesi])
            for mataKuliah in range (0, len(listSesi)):
                listSesi[mataKuliah] = f"{listSesi[mataKuliah]} {matkul[mataKuliah]}"
            for kelas in range (2, len(column), 2):
                listKelas.append(column[kelas])
            for matkulKelas in range (0, len(listSesi)):
                matkulDanKelas.append(f"{listSesi[matkulKelas]} {listKelas[matkulKelas]}")

            matkulDanKelas = sorting(matkulDanKelas)
            dataJadwal.append(f"{nama} - {individu}")
            dataJadwal.append(matkulDanKelas)

        return matkul
    
bukaData("mahasiswa/fisika.txt")

# Materi 1
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Manajemen Jadwal")
root.state('zoomed') 
font = ("Helvetica", 15)

frame_alat = tk.Frame(root)
frame_menu_awal = tk.Frame(root)
frame_menu_awal.pack(expand=True)
frame_dropdown = tk.Frame(frame_alat)
frame_dropdown.pack(pady=(0, 20), padx=50, fill=tk.X)

input = tk.Entry(frame_alat, font=font)
input.pack(pady=(0, 20), padx=50, fill=tk.X)
def cekJadwalMahasiswa(event):
    input_value = input.get()
    gantiTeks(jadwalindividu(dataJadwal, input_value))
input.bind("<KeyRelease>", cekJadwalMahasiswa)

dropdownUbahProdi = ttk.Combobox(frame_dropdown, font=font, state="readonly")
dropdownCariProdiKosong = ttk.Combobox(frame_dropdown, font=font, state="readonly")
dropdownJadwalKosongSesi = ttk.Combobox(frame_dropdown, font=font, state="readonly")

frame_hasil_pencarian = tk.Frame(frame_alat)
frame_hasil_pencarian.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
scrollbar_hasil = ttk.Scrollbar(frame_hasil_pencarian, orient=tk.VERTICAL)
text_hasil_pencarian = tk.Text(frame_hasil_pencarian, font=font, yscrollcommand=scrollbar_hasil.set)
scrollbar_hasil.config(command=text_hasil_pencarian.yview)
text_hasil_pencarian.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar_hasil.pack(side=tk.RIGHT, fill=tk.Y)

def pilihAlat(option):
    frame_menu_awal.pack_forget() 
    frame_alat.pack(expand=True)  
    if(option == 1):
        input.pack(expand=True)
        dropdownUbahProdi.pack(expand=True)
        dropdownCariProdiKosong.pack_forget()
        dropdownJadwalKosongSesi.pack_forget()
    elif(option == 2):
        input.pack_forget()
        dropdownUbahProdi.pack_forget()
        dropdownCariProdiKosong.pack(expand=True)
        dropdownJadwalKosongSesi.pack(expand=True)
    elif(option == 5):
        frame_alat.pack_forget()
        tree_frame.pack_forget()
        bottom_frame.pack_forget()
        frame_menu_awal.pack(expand=True)
    


tree_frame = ttk.Frame(root)
hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
hsb.pack(fill="x")

tabel_edit_jadwal = ttk.Treeview(tree_frame, columns=[], show="headings", xscrollcommand=hsb.set)
tabel_edit_jadwal.configure(xscrollcommand=hsb.set)
hsb.configure(command=tabel_edit_jadwal.xview)

bottom_frame = ttk.Frame(root)
dropdown = ttk.Combobox(bottom_frame,font = font, state='readonly')
dropdown['values'] = prodi
dropdown.pack(side="right", padx=40)
dropdown.set("Fisika")


def gantiTeks(output_teks):
    clean_result = "\n".join(line for line in output_teks.splitlines() if line.strip())
    text_hasil_pencarian.config(state=tk.NORMAL)
    text_hasil_pencarian.delete("1.0", tk.END)
    text_hasil_pencarian.insert(tk.END, clean_result)
    text_hasil_pencarian.config(state=tk.DISABLED)
    text_hasil_pencarian.yview_moveto(0)   

def ganti_prodi_edit(event):
    menuEdit()

def ubahProdi(event):
    bukaData(f"mahasiswa/{dropdownUbahProdi.get().lower()}.txt")

def cekJadwalKosongProdi(event):
    bukaData(f"mahasiswa/{dropdownCariProdiKosong.get().lower()}.txt")
    gantiTeks(jadwalKosong(dataJadwal, 1))

def cekSesiKosong(event):
    gantiTeks(jadwalKosong(dataJadwal, 2))

nama_kolom = []

def editData(path):
    table = []
    with open(path, 'r') as file:
        line = file.read().split("\n")
        matkul = line[0].replace("\t\t", "\t").split("\t")[:-1]
        matkulDanKelas = []
        for m in matkul:
            matkulDanKelas.extend(["Kelas", m])        
        for mahasiswa in range(1, len(line)):
            column = line[mahasiswa].split("\t")
            table.append(column)
        return table, matkulDanKelas
    
def ubahData(baris_tujuan, data_input, window_edit_jadwal):
    data = ""
    with open(f"mahasiswa/{dropdown.get()}.txt", 'r') as file:
        data = file.read()
    with open(f"mahasiswa/{dropdown.get()}.txt", 'w') as file:
        file.write(data.replace(baris_tujuan, data_input))
    window_edit_jadwal.destroy()   
    menuEdit()

def windowEdit(dataTabel):
    window_edit_jadwal = tk.Toplevel()
    window_edit_jadwal.title("Edit Jadwal")
    window_edit_jadwal.grab_set()
    window_edit_jadwal.geometry("800x150")

    canvas = tk.Canvas(window_edit_jadwal)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side="bottom", fill="x") 
    canvas.configure(xscrollcommand=scrollbar.set)
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    tabel_widget = ttk.Treeview(content_frame, columns=nama_kolom , show='headings')
    tabel_widget.insert('', 'end', values=dataTabel)
    data = []
    for kolom in range(0, len(nama_kolom)):
        label = tk.Label(content_frame, text=nama_kolom[kolom])
        label.grid(row=0, column=kolom, padx=10, pady=5)

        if kolom > 2 and kolom % 2 != 0:
            edit_sesi = ttk.Combobox(content_frame, state="readonly")
            edit_sesi['values'] = prodi
            edit_sesi.grid(row=1, column=kolom, padx=10, pady=5)
            edit_sesi.set(dataTabel[kolom])
            data.append(edit_sesi)
        else:
            input = tk.Entry(content_frame)
            input.grid(row=1, column=kolom, padx=10, pady=5)
            input.insert(0, dataTabel[kolom])
            data.append(input)

        formatted_values = "\t".join(dataTabel)
        
        save_button = tk.Button(content_frame, text="Simpan", command=lambda: 
                                ubahData(formatted_values, "\t".join([widget.get() for widget in data]), window_edit_jadwal))
        save_button.grid(row=2, column=0, padx=10, pady=5)
        content_frame.update_idletasks() 
        canvas.config(scrollregion=canvas.bbox("all"))

def popup(event):
    item_id = tabel_edit_jadwal.selection()
    item_values = tabel_edit_jadwal.item(item_id, 'values')
    formatted_values = "\t".join(item_values)
    tabel_edit_jadwal.selection_set(item_id)
    popup = tk.Menu(root, tearoff=0)
    popup.add_command(label="Edit", command=lambda: windowEdit(item_values))
    popup.add_command(label="Hapus", command=lambda: ubahData(f"{formatted_values}\n", ""))
    popup.post(event.x_root, event.y_root)

def menuEdit():
    global nama_kolom
    path = dropdown.get()
    tabel, matkulDanKelas = [],[]
    tabel, matkulDanKelas = editData(f"mahasiswa/{path}.txt")
    id_kolom = ["NIM", "Nama"] + [f"col_{i}" for i in range(len(matkulDanKelas))]
    nama_kolom = ["NIM", "Nama"]

    for urutanKolom in range(len(matkulDanKelas)):
        if (urutanKolom % 2 != 0): nama_kolom.append(matkulDanKelas[urutanKolom])  
        else: nama_kolom.append("Kelas")     

    frame_menu_awal.pack_forget()
    tree_frame.pack(fill=tk.BOTH, expand=True)
    bottom_frame.pack(fill=tk.BOTH, expand=True)
    tabel_edit_jadwal["columns"] = id_kolom 
    tabel_edit_jadwal.pack(fill=tk.BOTH, expand=True) 
    tabel_edit_jadwal.delete(*tabel_edit_jadwal.get_children())

    for col in range(0, len(id_kolom)):
        tabel_edit_jadwal.heading(col, text=nama_kolom[col])
        tabel_edit_jadwal.column(col, anchor=tk.CENTER)  
    for row in tabel:
        tabel_edit_jadwal.insert("", tk.END, values=row)

    hsb.configure(command=tabel_edit_jadwal.xview)
    tabel_edit_jadwal.bind("<Button-3>", popup) # Klik kanan


def buatTombol(frame_tombol, teks, fungsi):
    tombol = tk.Button(frame_tombol, text=teks, font=font, command=fungsi)
    tombol.pack(fill=tk.X, pady=10, padx=50)

def buatDropdown(comboBox, values, text, fungsi):
    comboBox['values'] = values
    comboBox.set(text)
    comboBox.pack(padx=(10, 0))
    comboBox.bind("<<ComboboxSelected>>", fungsi)

buatDropdown(dropdownUbahProdi, prodi, "Pilih Prodi", ubahProdi)
buatDropdown(dropdownCariProdiKosong, prodi, "Cari Berdasarkan Prodi", cekJadwalKosongProdi)
buatDropdown(dropdownJadwalKosongSesi, sesi, "Cari Berdasarkan Sesi", cekSesiKosong)
dropdown.bind("<<ComboboxSelected>>", ganti_prodi_edit)

buatTombol(frame_menu_awal, "Lihat Jadwal Matkul", lambda: pilihAlat(1))
buatTombol(frame_menu_awal, "Jadwal Kosong",lambda: pilihAlat(2))
buatTombol(frame_menu_awal, "Edit Jadwal",menuEdit)
buatTombol(frame_alat, "Kembali", lambda: pilihAlat(5))
buatTombol(bottom_frame, "Kembali", lambda: pilihAlat(5))

root.mainloop()
