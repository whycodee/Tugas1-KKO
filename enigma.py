import tkinter as tk
from tkinter import CENTER

# Daftar rotor Enigma
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

# Fungsi enkripsi Enigma
def enigma_encrypt(plain_text):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            index = ord(char) - ord('A')
            encrypted_char = rotor3[rotor2[rotor1[index]]]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


# Fungsi saat tombol "Enkripsi" ditekan
def encrypt_button_click():
    input_text = input_text_widget.get("1.0", "end-1c")  # Ambil teks dari widget teks
    encrypted_text = enigma_encrypt(input_text)
    output_text_widget.config(state="normal")  # Aktifkan widget teks agar dapat diubah
    output_text_widget.delete("1.0", "end")  # Hapus teks sebelumnya (jika ada)
    output_text_widget.insert("1.0", encrypted_text)  # Tampilkan teks terenkripsi
    output_text_widget.config(state="disabled")  # Nonaktifkan kembali widget teks

# Fungsi untuk menengahkan jendela GUI
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    # window.geometry('{}x{}+{}+{}'.format(width, height, x, y)

# Membuat jendela utama
root = tk.Tk()
root.title("Enigma Cipher")

# Mengatur jendela agar berada di tengah layar
root.geometry("800x600")
center_window(root)

# Membuat label
input_label = tk.Label(root, text="Masukkan Teks:")
input_label.pack()

# Membuat widget teks untuk input
input_text_widget = tk.Text(root, height=10, width=40)
input_text_widget.pack()

# Membuat tombol untuk mengenkripsi
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_button_click)
encrypt_button.pack()

# Label untuk menampilkan teks terenkripsi
output_label = tk.Label(root, text="Teks Terenkripsi:")
output_label.pack()

# Membuat widget teks untuk output (teks terenkripsi)
output_text_widget = tk.Text(root, height=10, width=40)
output_text_widget.config(state="disabled")  # Nonaktifkan widget teks
output_text_widget.pack()

# Memulai loop utama GUI
root.mainloop()
