# 🔐 Secure Data Hiding in Images Using Steganography
A Python-based steganography tool that allows users to hide and retrieve secret messages from images using password protection. This ensures secure communication and data privacy.

📌 Features
✅ Secure Encryption – Hides a message inside an image without changing its appearance.
✅ Password Protection – Only users with the correct password can retrieve the hidden message.
✅ Graphical User Interface (GUI) – Easy-to-use interface built with Tkinter.
✅ Supports Common Image Formats – Works with PNG, JPG, JPEG files.
✅ No Data Loss – The image remains unchanged while storing the message.

🚀 Installation
🔹 Prerequisites
Ensure you have Python 3.x installed along with the required dependencies.

🔹 Install Required Libraries
Run the following command to install dependencies:
pip install opencv-python numpy tkinter

🔹 Usage Guide
🔹 Encryption (Hiding a Message)
1️⃣ Run the script:
python steganography.py
2️⃣ Click "Select Image" and choose an image to hide your message.
3️⃣ Enter your secret message and set a password for protection.
4️⃣ Click "Encrypt & Save" to store the message inside the image.
5️⃣ The encrypted image is saved and ready for secure sharing.

🔹 Decryption (Retrieving a Hidden Message)
1️⃣ Run the script and select the encrypted image.
2️⃣ Enter the correct password used during encryption.
3️⃣ Click "Decrypt Message" to retrieve the hidden text.
4️⃣ If the password is correct, the hidden message will be displayed.
5️⃣ If the password is incorrect, an error message will be shown.

🔹 Screenshots
📌 Encryption Process
![Screenshot 2025-02-26 174544](https://github.com/user-attachments/assets/3bddbd99-739b-42de-9dac-c730df88b221)


📌 Decryption Process
![Screenshot 2025-02-26 174657](https://github.com/user-attachments/assets/9084d11d-663a-4f22-b52a-1b36ad9e2019)


🔹 Technologies Used
Python – Core programming language
OpenCV – Image processing and pixel manipulation
Tkinter – Graphical User Interface (GUI)
Steganography – Technique to hide and extract messages



