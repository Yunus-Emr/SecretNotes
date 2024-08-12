import tkinter as tk
from tkinter import PhotoImage


# UI
window = tk.Tk()
window.title("Secret Notes")
window.minsize(width=400, height=800)

image = PhotoImage(file='top_secret.png')
image_label = tk.Label(image=image)
image_label.config(height=200)
image_label.pack()

title_label = tk.Label(text="Enter your title", font=('Arial', 13, 'normal'))
title_label.place(x=132, y=230)

title_entry = tk.Entry(width=35)
title_entry.place(x=93, y=260)

secret_label = tk.Label(text="Enter your secret", font=('Arial', 13, 'normal'))
secret_label.place(x=132, y=285)

secret_text = tk.Text(width=35, height=20)
secret_text.place(x=58, y=310)

master_key_label = tk.Label(text="Enter master key", font=('Arial', 13, 'normal'))
master_key_label.place(x=132, y=640)

master_key_entry = tk.Entry(width=35)
master_key_entry.place(x=93, y=670)

save_button = tk.Button(text="Save & Encrypt", width=20)
save_button.place(x=125, y=700)

decrypt_button = tk.Button(text="Decrypt", width=15)
decrypt_button.place(x=142.5, y=730)

window.mainloop()
