import tkinter as tk
from tkinter import filedialog
from tkinter import CENTER
import os

# Fungsi enkripsi One-time pad
def one_time_pad_encrypt(plain_text, key):
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i].upper()
            key_shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi dekripsi One-time pad
def one_time_pad_decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i].upper()
            key_shift = ord(key_char) - ord('A')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key_shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - key_shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk menengahkan jendela GUI
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    # window.geometry('{}x{}+{}+{}'.format(width, height, x, y)

# Fungsi saat tombol "Enkripsi" ditekan
def encrypt_button_click():
    plain_text = input_text.get("1.0", "end-1c")  # Ambil teks dari widget teks
    key = key_entry.get()
    encrypted_text = one_time_pad_encrypt(plain_text, key)
    output_text.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text.insert("1.0", encrypted_text)  # Tampilkan teks terenkripsi
    output_text.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Dekripsi" ditekan
def decrypt_button_click():
    encrypted_text = output_text.get("1.0", "end-1c")  # Ambil teks terenkripsi dari widget teks
    key = key_entry.get()
    decrypted_text = one_time_pad_decrypt(encrypted_text, key)
    input_text.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    input_text.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    input_text.insert("1.0", decrypted_text)  # Tampilkan teks terdekripsi
    input_text.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Buka Kunci" ditekan
def open_key_button_click():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as key_file:
            key = key_file.read()
            key_entry.delete(0, "end")  # Hapus kunci sebelumnya (jika ada)
            key_entry.insert(0, key)

# Membuat jendela utama
root = tk.Tk()
root.title("One-time Pad")

# Mengatur jendela agar berada di tengah layar
root.geometry("800x600")
center_window(root)

# Membuat label
input_label = tk.Label(root, text="Masukkan Teks:")
input_label.pack()

# Membuat widget teks untuk input
input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# Membuat label untuk kunci
key_label = tk.Label(root, text="Masukkan Kunci:")
key_label.pack()

# Membuat kotak input untuk kunci
key_entry = tk.Entry(root)
key_entry.pack()

# Membuat tombol untuk mengenkripsi
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_button_click)
encrypt_button.pack()

# Membuat tombol untuk mendekripsi
decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt_button_click)
decrypt_button.pack()

# Membuat tombol "Buka Kunci"
open_key_button = tk.Button(root, text="Buka Kunci", command=open_key_button_click)
open_key_button.pack()

# Label untuk menampilkan teks terenkripsi
output_label = tk.Label(root, text="Teks Terenkripsi:")
output_label.pack()

# Membuat widget teks untuk output (teks terenkripsi)
output_text = tk.Text(root, height=10, width=40)
output_text.config(state="disabled")  # Nonaktifkan widget teks
output_text.pack()

# Memulai loop utama GUI
root.mainloop()
