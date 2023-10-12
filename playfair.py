import tkinter as tk
from tkinter import filedialog
from tkinter import CENTER
import os

# Matriks Playfair
playfair_matrix = [['D', 'I', 'S', 'T', 'O'],
                  ['A', 'N', 'E', 'X', 'B'],
                  ['C', 'F', 'G', 'H', 'K'],
                  ['L', 'M', 'P', 'Q', 'R'],
                  ['U', 'V', 'W', 'Y', 'Z']]

# Fungsi untuk mengenkripsi pesan menggunakan Playfair Cipher
def playfair_encrypt(plain_text):
    encrypted_text = ""
    plain_text = plain_text.replace("J", "I")  # Ganti J dengan I
    plain_text = "".join(e for e in plain_text if e.isalpha()).upper()  # Hanya karakter alfabet dan ubah ke huruf besar

    for i in range(0, len(plain_text), 2):
        if i == len(plain_text) - 1:
            pair = plain_text[i] + 'X'  # Tambah 'X' jika karakter terakhir sendirian
        else:
            pair = plain_text[i] + plain_text[i + 1]

        row1, col1 = None, None
        row2, col2 = None, None

        # Temukan koordinat karakter di matriks Playfair
        for row in range(5):
            if row1 is not None and row2 is not None:
                break
            for col in range(5):
                if playfair_matrix[row][col] == pair[0]:
                    row1, col1 = row, col
                if playfair_matrix[row][col] == pair[1]:
                    row2, col2 = row, col

        if row1 is not None and row2 is not None:
            if col1 == col2:  # Karakter berada pada kolom yang sama
                encrypted_text += playfair_matrix[(row1 + 1) % 5][col1]
                encrypted_text += playfair_matrix[(row2 + 1) % 5][col2]
            elif row1 == row2:  # Karakter berada pada baris yang sama
                encrypted_text += playfair_matrix[row1][(col1 + 1) % 5]
                encrypted_text += playfair_matrix[row2][(col2 + 1) % 5]
            else:  # Karakter berada pada baris dan kolom yang berbeda
                encrypted_text += playfair_matrix[row1][col2]
                encrypted_text += playfair_matrix[row2][col1]

    return encrypted_text

# Fungsi untuk mendekripsi pesan menggunakan Playfair Cipher
def playfair_decrypt(encrypted_text):
    decrypted_text = ""
    encrypted_text = "".join(e for e in encrypted_text if e.isalpha()).upper()

    for i in range(0, len(encrypted_text), 2):
        pair = encrypted_text[i] + encrypted_text[i + 1]

        row1, col1 = None, None
        row2, col2 = None, None

        for row in range(5):
            if row1 is not None and row2 is not None:
                break
            for col in range(5):
                if playfair_matrix[row][col] == pair[0]:
                    row1, col1 = row, col
                if playfair_matrix[row][col] == pair[1]:
                    row2, col2 = row, col

        if row1 is not None and row2 is not None:
            if col1 == col2:  # Karakter berada pada kolom yang sama
                decrypted_text += playfair_matrix[(row1 - 1) % 5][col1]
                decrypted_text += playfair_matrix[(row2 - 1) % 5][col2]
            elif row1 == row2:  # Karakter berada pada baris yang sama
                decrypted_text += playfair_matrix[row1][(col1 - 1) % 5]
                decrypted_text += playfair_matrix[row2][(col2 - 1) % 5]
            else:  # Karakter berada pada baris dan kolom yang berbeda
                decrypted_text += playfair_matrix[row1][col2]
                decrypted_text += playfair_matrix[row2][col1]

    return decrypted_text

# Fungsi untuk menengahkan jendela GUI
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Fungsi saat tombol "Enkripsi" ditekan
def encrypt_button_click():
    plain_text = input_text.get("1.0", "end-1c")  # Ambil teks dari widget teks
    encrypted_text = playfair_encrypt(plain_text)
    output_text.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text.insert("1.0", encrypted_text)  # Tampilkan teks terenkripsi
    output_text.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Dekripsi" ditekan
def decrypt_button_click():
    encrypted_text = input_text.get("1.0", "end-1c")  # Ambil teks dari widget teks
    decrypted_text = playfair_decrypt(encrypted_text)
    output_text.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text.insert("1.0", decrypted_text)  # Tampilkan teks terdekripsi
    output_text.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Buka Berkas" ditekan
def open_file_button_click():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            input_text.delete("1.0", "end")
            input_text.insert("1.0", file_contents)

# Fungsi saat tombol "Simpan Sebagai" ditekan
def save_as_button_click():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file_contents = output_text.get("1.0", "end-1c")
            file.write(file_contents)

# Membuat jendela utama
root = tk.Tk()
root.title("Playfair Cipher")

# Mengatur jendela agar berada di tengah layar
root.geometry("800x600")
center_window(root)

# Membuat label
input_label = tk.Label(root, text="Masukkan Teks:")
input_label.pack()

# Membuat widget teks untuk input
input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# Membuat tombol untuk mengenkripsi
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_button_click)
encrypt_button.pack()

# Membuat tombol untuk mendekripsi
decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt_button_click)
decrypt_button.pack()

# Label untuk menampilkan teks terenkripsi
output_label = tk.Label(root, text="Teks Terenkripsi:")
output_label.pack()

# Membuat widget teks untuk output (teks terenkripsi)
output_text = tk.Text(root, height=10, width=40)
output_text.config(state="disabled")  # Nonaktifkan widget teks
output_text.pack()

# Membuat tombol "Buka Berkas"
open_file_button = tk.Button(root, text="Buka Berkas", command=open_file_button_click)
open_file_button.pack()

# Membuat tombol "Simpan Sebagai"
save_as_button = tk.Button(root, text="Simpan Sebagai", command=save_as_button_click)
save_as_button.pack()

# Memulai loop utama GUI
root.mainloop()
