listJadwal = []

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

def jadwalindividu(listJadwal, text):
    found = False
    listDitemukan=""
    for i in range (0, len(listJadwal), 2):
        if (text.lower() in listJadwal[i].lower()):
            listDitemukan = f"\n{listDitemukan}{listJadwal[i]}\n"
            for j in range (0, len(listJadwal[i+1])):
                if(listJadwal[i+1][j]):
                    listDitemukan = f"{listDitemukan}{listJadwal[i+1][j]}\n"
                    found = True
    if(found == False): return "Tidak ditemukan."
    else: return(listDitemukan)

def jadwalKosong(listJadwal, opsi): 
    listJadwalKosong = []
    for indeksJadwal in range(1, len(listJadwal),2):
        listSesiKosong = sesi.copy()
        for jadwalMahasiswa in listJadwal[indeksJadwal]: 
            for jadwalMatkul in listSesiKosong: 
                if jadwalMatkul in jadwalMahasiswa: listSesiKosong.remove(jadwalMatkul)
        listJadwalKosong.append(listJadwal[indeksJadwal-1])
        listJadwalKosong.append(listSesiKosong)

    if(opsi == 1):
        jadwalKosongProdiDitemukan = ""
        listSesi = sesi.copy()
        count = []
        for sesiAktif in range (0, len(listSesi)):
            for mahasiswa in range(1, len(listJadwalKosong), 2):
                for k in listJadwalKosong[mahasiswa]:
                    count.append(0)
                    if(listSesi[sesiAktif] in k): count[sesiAktif] = count[sesiAktif] + 1

        for totalKosong in range (0, len(listSesi)):
            jadwalKosongProdiDitemukan = f"{jadwalKosongProdiDitemukan}{listSesi[totalKosong]}: {count[totalKosong]} mahasiswa kosong\n"
        return jadwalKosongProdiDitemukan
    
    elif(opsi == 2):
        jadwalKosongSesiDitemukan = ""
        for i in range(1, len(listJadwalKosong), 2):
            if(dropdownJadwalKosongSesi.get() in listJadwalKosong[i]): 
                jadwalKosongSesiDitemukan = f"{jadwalKosongSesiDitemukan}{listJadwalKosong[i-1]}\n"
        if(jadwalKosongSesiDitemukan == ""): 
            return f"Tidak ada mahasiswa prodi {dropdownCariProdiKosong.get()} yang kosong saat {dropdownJadwalKosongSesi.get()}"
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
            listJadwal.append(f"{nama} - {individu}")
            listJadwal.append(matkulDanKelas)

        return matkul
    
openData("mahasiswa/fisika.txt")

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
    gantiTeks(jadwalindividu(listJadwal, input_value))
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

def openTools(option):
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

tree = ttk.Treeview(tree_frame, columns=[], show="headings", xscrollcommand=hsb.set)
tree.configure(xscrollcommand=hsb.set)
hsb.configure(command=tree.xview)

bottom_frame = ttk.Frame(root)
dropdown = ttk.Combobox(bottom_frame,font = font, state='readonly')
dropdown['values'] = sesi
dropdown.pack(side="right", padx=40)
dropdown.set("Fisika")

def dataEdit(path):
    table = []
    with open(path, 'r') as file:
        line = file.read().split("\n")
        matkul = line[0].replace("\t\t", "\t").split("\t")[:-1]
        matkulDanKelas = []
        for m in matkul:
            matkulDanKelas.extend(["Kelas", m])        
        for mahasiswa in range(1, len(line)):
            column = line[mahasiswa].split("\t")
            table.append(tuple(column))
        return table, matkulDanKelas
    
def ubahData(baris_tujuan, data_input):
    data = ""
    with open(f"mahasiswa/{dropdown.get()}.txt", 'r') as file:
        data = file.read()
    with open(f"mahasiswa/{dropdown.get()}.txt", 'w') as file:
        file.write(data.replace(baris_tujuan, data_input))
    openEditor()

def menu_edit(row_data):
    edit_window = tk.Toplevel()
    edit_window.title("Edit Jadwal")
    edit_window.grab_set()
    edit_window.geometry("800x600")

    canvas = tk.Canvas(edit_window)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side="bottom", fill="x") 
    canvas.configure(xscrollcommand=scrollbar.set)
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    tree = ttk.Treeview(content_frame, columns=kolom_tabel , show='headings')
    tree.insert('', 'end', values=row_data)
    data = []
    for i in range(0, len(kolom_tabel)):
        label = tk.Label(content_frame, text=kolom_tabel[i])
        label.grid(row=0, column=i, padx=10, pady=5)  # Place label in grid

        if i > 2 and i % 2 != 0:
            edit_sesi = ttk.Combobox(content_frame, state="readonly")
            edit_sesi['values'] = prodi
            edit_sesi.grid(row=1, column=i, padx=10, pady=5)
            edit_sesi.set(row_data[i])
            data.append(edit_sesi)
        else:
            entry = tk.Entry(content_frame)
            entry.grid(row=1, column=i, padx=10, pady=5)
            entry.insert(0, row_data[i])
            data.append(entry)

        formatted_values = "\t".join(row_data)
        
        save_button = tk.Button(content_frame, text="Simpan", command=lambda: ubahData(formatted_values, "\t".join([widget.get() for widget in data])))
        save_button.grid(row=2, column=0, padx=10, pady=5)
        content_frame.update_idletasks() 
        canvas.config(scrollregion=canvas.bbox("all"))

def show_popup(event):
    item_id = tree.selection()
    item_values = tree.item(item_id, 'values')
    formatted_values = "\t".join(item_values)
    tree.selection_set(item_id)
    popup = tk.Menu(root, tearoff=0)
    popup.add_command(label="Edit", command=lambda: menu_edit(item_values))
    popup.add_command(label="Hapus", command=lambda: ubahData(f"{formatted_values}\n", ""))
    popup.post(event.x_root, event.y_root)

kolom_tabel = []

def gantiTeks(output_teks):
    clean_result = "\n".join(line for line in output_teks.splitlines() if line.strip())
    text_hasil_pencarian.config(state=tk.NORMAL)
    text_hasil_pencarian.delete("1.0", tk.END)
    text_hasil_pencarian.insert(tk.END, clean_result)
    text_hasil_pencarian.config(state=tk.DISABLED)
    text_hasil_pencarian.yview_moveto(0)   

def ganti_prodi_edit(event):
    openEditor()

def ubahProdi(event):
    openData(f"mahasiswa/{dropdownUbahProdi.get().lower()}.txt")

def cekJadwalKosongProdi(event):
    openData(f"mahasiswa/{dropdownCariProdiKosong.get().lower()}.txt")
    gantiTeks(jadwalKosong(listJadwal, 1))

def cekSesiKosong(event):
    gantiTeks(jadwalKosong(listJadwal, 2))

def openEditor():
    global kolom_tabel
    path = dropdown.get()
    table, matkulDanKelas = [],[]
    table, matkulDanKelas = dataEdit(f"mahasiswa/{path}.txt")
    columns = ["NIM", "Nama"] + [f"col_{i}" for i in range(len(matkulDanKelas))]
    kolom_tabel = ["NIM", "Nama"] 

    for i in range(len(matkulDanKelas)):
        if (i % 2 != 0): kolom_tabel.append(matkulDanKelas[i])  
        else: kolom_tabel.append("Kelas")     

    frame_menu_awal.pack_forget()
    tree_frame.pack(fill=tk.BOTH, expand=True)
    bottom_frame.pack(fill=tk.BOTH, expand=True)
    tree["columns"] = columns 
    tree.pack(fill=tk.BOTH, expand=True) 
    tree.delete(*tree.get_children())

    for i, col in enumerate(columns):
        tree.heading(col, text=kolom_tabel[i])
        tree.column(col, anchor=tk.CENTER)  
    for row in table:
        tree.insert("", tk.END, values=row)

    hsb.configure(command=tree.xview)
    tree.bind("<Button-3>", show_popup)

dropdown.bind("<<ComboboxSelected>>", ganti_prodi_edit)

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

buatTombol(frame_menu_awal, "Lihat Jadwal Matkul", lambda: openTools(1))
buatTombol(frame_menu_awal, "Jadwal Kosong",lambda: openTools(2))
buatTombol(frame_menu_awal, "Edit Jadwal",openEditor)
buatTombol(frame_alat, "Kembali", lambda: openTools(5))
buatTombol(bottom_frame, "Kembali", lambda: openTools(5))

root.mainloop()
