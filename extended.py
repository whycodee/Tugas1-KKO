import tkinter as tk
from tkinter import filedialog
from tkinter import CENTER

# Fungsi enkripsi Extended Vigenere
def extended_vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[index % key_length]
            key_shift = ord(key_char)
            encrypted_char = chr((ord(char) + key_shift) % 256)
            encrypted_text += encrypted_char
            index += 1

    return encrypted_text

# Fungsi dekripsi Extended Vigenere
def extended_vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = key[index % key_length]
            key_shift = ord(key_char)
            decrypted_char = chr((ord(char) - key_shift) % 256)
            decrypted_text += decrypted_char
            index += 1

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
    input_text = input_text_widget.get("1.0", "end-1c")  # Ambil teks dari widget teks
    key = key_entry.get()
    encrypted_text = extended_vigenere_encrypt(input_text, key)
    output_text_widget.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text_widget.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text_widget.insert("1.0", encrypted_text)  # Tampilkan teks terenkripsi
    output_text_widget.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi saat tombol "Dekripsi" ditekan
def decrypt_button_click():
    input_text = input_text_widget.get("1.0", "end-1c")  # Ambil teks dari widget teks
    key = key_entry.get()
    decrypted_text = extended_vigenere_decrypt(input_text, key)
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
root.title("Extended Vigenere Cipher")

# Mengatur jendela agar berada di tengah layar
root.geometry("800x600")
center_window(root)

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

# Label untuk menampilkan teks terenkripsi
output_label = tk.Label(root, text="Teks Terenkripsi:")
output_label.pack()

# Membuat widget teks untuk output (teks terenkripsi)
output_text_widget = tk.Text(root, height=10, width=40)
output_text_widget.config(state="disabled")  # Nonaktifkan widget teks
output_text_widget.pack()

# Memulai loop utama GUI
root.mainloop()
