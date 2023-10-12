import tkinter as tk
from tkinter import filedialog
from tkinter import CENTER
import os

# Fungsi enkripsi Vigenere
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[index % key_length].upper()
            key_shift = ord(key_char) - ord('A')
            index += 1

            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            encrypted_text += encrypted_char

    return encrypted_text

# Fungsi dekripsi Vigenere
def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = key[index % key_length].upper()
            key_shift = ord(key_char) - ord('A')
            index += 1

            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key_shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - key_shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char

    return decrypted_text

# Fungsi saat tombol "Enkripsi" ditekan
def encrypt_button_click():
    input_text = input_text_widget.get("1.0", "end-1c")  # Ambil teks dari widget teks
    key = key_entry.get()
    encrypted_text = vigenere_encrypt(input_text, key)
    output_text_widget.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text_widget.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text_widget.insert("1.0", encrypted_text)  # Tampilkan teks terenkripsi
    output_text_widget.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Dekripsi" ditekan
def decrypt_button_click():
    input_text = input_text_widget.get("1.0", "end-1c")  # Ambil teks dari widget teks
    key = key_entry.get()
    decrypted_text = vigenere_decrypt(input_text, key)
    output_text_widget.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text_widget.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text_widget.insert("1.0", decrypted_text)  # Tampilkan teks terdekripsi
    output_text_widget.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Buka Berkas" ditekan
def open_file_button_click():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        with open(file_path, "rb") as file:
            file_contents = file.read()
            input_text_widget.delete("1.0", "end")
            input_text_widget.insert("1.0", file_contents.decode(errors="ignore"))

# Fungsi saat tombol "Simpan Sebagai" ditekan
def save_as_button_click():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "wb") as file:
            file_contents = output_text_widget.get("1.0", "end-1c").encode()
            file.write(file_contents)

# Membuat jendela utama
root = tk.Tk()
root.title("Vigenere Cipher")

# Mengatur jendela agar berada di tengah layar
root.geometry("800x600")
# center_window(root)

# Membuat label
input_label = tk.Label(root, text="Masukkan Teks:")
input_label.pack()

# Membuat widget teks untuk input
input_text_widget = tk.Text(root, height=10, width=40)
input_text_widget.pack()

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

# Membuat tombol "Buka Berkas"
open_file_button = tk.Button(root, text="Buka Berkas", command=open_file_button_click)
open_file_button.pack()

# Membuat tombol "Simpan Sebagai"
save_as_button = tk.Button(root, text="Simpan Sebagai", command=save_as_button_click)
save_as_button.pack()

# Membuat label untuk teks terenkripsi
output_label = tk.Label(root, text="Teks Terenkripsi:")
output_label.pack()

# Membuat widget teks untuk output (teks terenkripsi)
output_text_widget = tk.Text(root, height=10, width=40)
output_text_widget.config(state="disabled")  # Nonaktifkan widget teks
output_text_widget.pack()

# Memulai loop utama GUI
root.mainloop()
