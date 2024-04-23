import tkinter as tk
from tkinter import PhotoImage

# Создание главного окна
root = tk.Tk()
root.title("NoteSculptor")

# Установка размера окна
root.geometry("350x600")
root.resizable(False, False)
root.configure(bg="white")


# Функция, вызываемая при нажатии на кнопку START
def start_action():
    print("Начать обработку")


# Создание заголовка
title_label = tk.Label(root, text="NoteSculptor", font=("Arial", 10), fg="gray")
title_label.config(bg="white")
title_label.pack(anchor='w')

# Создание кнопки START
start_button_image = PhotoImage(file="assets/start_button.png")  # Укажите путь к изображению кнопки
start_button = tk.Button(root, image=start_button_image, command=start_action)
start_button.config(bd=0, bg="white")
start_button.pack(pady=80)

# Добавление изображения с нотами (заглушка)
# В реальном приложении здесь будет использоваться PhotoImage для загрузки изображения
notes_image = PhotoImage(file="assets/start_notes.png")
notes_image_label = tk.Label(root, image=notes_image)
notes_image_label.config(bg="white")
notes_image_label.pack(pady=20)

# Создание нижней панели с кнопками
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

history_button = tk.Button(bottom_frame, text="ИСТОРИЯ")
history_button.config(bg="black", fg="white")
history_button.pack(side=tk.LEFT, expand=True, fill=tk.X)


settings_button = tk.Button(bottom_frame, text="НАСТРОЙКИ")
settings_button.config(bg="black", fg="white")
settings_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

account_button = tk.Button(bottom_frame, text="АККАУНТ")
account_button.config(bg="black", fg="white")
account_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

root.mainloop()