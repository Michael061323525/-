import customtkinter as ctk
import tkinter as tk

# Определяем функцию encrypt(), которая шифрует текст
def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha() and char.islower():
            result += chr((ord(char) + 5 - ord('а')) % 32 + ord('а'))
        elif char.isalpha() and char.isupper():
            result += chr((ord(char) + 5 - ord('А')) % 32 + ord('А'))
        else:
            result += char
    return result

# Определяем функцию decrypt(), которая дешифрует текст
def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha() and char.islower():
            result += chr((ord(char) - 5 - ord('а')) % 32 + ord('а'))
        elif char.isalpha() and char.isupper():
            result += chr((ord(char) - 5 - ord('А')) % 32 + ord('А'))
        else:
            result += char
    return result

# Определяем функцию on_encrypt(), которая вызывается при нажатии кнопки "Зашифровать"
def on_encrypt():
    text = input_text.get("1.0", "end-1c")
    encrypted_text = encrypt(text)
    output_text.delete(1.0, tk.END)
    output_text.insert(1.0, encrypted_text)

# Определяем функцию on_decrypt(), которая вызывается при нажатии кнопки "Дешифровать"
def on_decrypt():
    text = input_text.get("1.0", "end-1c")
    decrypted_text = decrypt(text)
    output_text.delete(1.0, tk.END)
    output_text.insert(1.0, decrypted_text)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

# Создаем главное окно, задаем ему размер, цвет фона и заголовок
root = ctk.CTk()
root.geometry("600x450")
root.title("Шифр Цезаря")


# Создаем надпись "Входной текст:" и добавляем ее на главное окно
input_label = ctk.CTkLabel(root, text="Входной текст:")
input_label.pack(pady=10)

# Создаем текстовое поле для ввода текста
input_text = ctk.CTkTextbox(root, wrap="word", width=350, height=100, border_color="grey", border_width=1)
input_text.pack()


# Создание кнопки для шифрования текста
encrypt_button = ctk.CTkButton(root, text="Зашифровать", command=on_encrypt)
encrypt_button.pack(pady=10)

# Создание кнопки для дешифрования текста
decrypt_button = ctk.CTkButton(root, text="Дешифровать", command=on_decrypt)
decrypt_button.pack(pady=10)

# Создаем метку для выходного текста
output_label = ctk.CTkLabel(root, text="Выходной текст:")
output_label.pack(pady=10)

# Создаем текстовое поле для вывода текста
output_text = ctk.CTkTextbox(root, wrap="word", width=350, height=100, border_color="grey", border_width=1)
output_text.pack()

# Создание контекстного меню


context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Копировать", command=lambda: root.focus_get().event_generate("<<Copy>>"))
context_menu.add_command(label="Вставить", command=lambda: root.focus_get().event_generate("<<Paste>>"))

root.bind("<Button-3>", show_context_menu)

# Запуск главного цикла обработки событий tkinter

root.mainloop()