import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if img_path:
        img = cv2.imread(img_path)
        if img is None:
            messagebox.showerror("Error", "Invalid image file!")

def encrypt_message():
    if not img_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    msg = msg_entry.get()
    password = pass_entry.get()

    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    secret_data = password + "|" + msg + "~"  # Store password + message

    height, width, _ = img.shape
    d = {chr(i): i for i in range(256)}
    
    index = 0
    for row in range(height):
        for col in range(width):
            for channel in range(3):  
                if index < len(secret_data):
                    img[row, col, channel] = d[secret_data[index]]
                    index += 1
                else:
                    break

    save_path = "encrypted_image.png"
    cv2.imwrite(save_path, img)
    os.system(f"start {save_path}")  # Opens image (Windows)

    messagebox.showinfo("Success", "Message encrypted successfully!\nSaved as encrypted_image.png")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Encryption")
root.geometry("400x300")

tk.Button(root, text="Select Image", command=select_image).pack(pady=10)
tk.Label(root, text="Enter Secret Message:").pack()
msg_entry = tk.Entry(root, width=40)
msg_entry.pack(pady=5)

tk.Label(root, text="Enter Password:").pack()
pass_entry = tk.Entry(root, width=40, show="*")
pass_entry.pack(pady=5)

tk.Button(root, text="Encrypt & Save", command=encrypt_message).pack(pady=10)

root.mainloop()
