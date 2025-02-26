import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def select_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if img_path:
        img = cv2.imread(img_path)
        if img is None:
            messagebox.showerror("Error", "Invalid image file!")
        else:
            messagebox.showinfo("Success", "Image selected successfully!")

def decrypt_message():
    if not img_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    input_pass = pass_entry.get()
    if not input_pass:
        messagebox.showerror("Error", "Password cannot be empty!")
        return

    decrypted_msg = ""
    height, width, _ = img.shape
    c = {i: chr(i) for i in range(256)}

    # Extract the encrypted text from the image
    for row in range(height):
        for col in range(width):
            for channel in range(3):
                char = c[img[row, col, channel]]
                if char == "~":  # Stop at the end marker
                    break
                decrypted_msg += char

    # Ensure proper formatting
    if "|" in decrypted_msg:
        stored_password, message = decrypted_msg.split("|", 1)

        # Verify password
        if input_pass == stored_password:
            messagebox.showinfo("Decryption Result", message)  # Show only the message
        else:
            messagebox.showerror("Error", "Incorrect password!")
    else:
        messagebox.showerror("Error", "No hidden message found!")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Decryption")
root.geometry("400x250")

tk.Button(root, text="Select Encrypted Image", command=select_image).pack(pady=10)
tk.Label(root, text="Enter Password:").pack()
pass_entry = tk.Entry(root, width=40, show="*")
pass_entry.pack(pady=5)

tk.Button(root, text="Decrypt Message", command=decrypt_message).pack(pady=10)

root.mainloop()
