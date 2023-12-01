# -*- coding: UTF-8 -*-
# 回答問題以產生 QRcode 圖檔，編碼可中文
import pyqrcode

def generate_qr_code():
    print("Choose QR code type:")
    print("1. URL")
    print("2. Text")
    print("3. WiFi")
    print("4. Email")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        content = input("Enter the URL: ")
    elif choice == '2':
        content = input("Enter the text: ")
    elif choice == '3':
        ssid = input("Enter the WiFi SSID: ")
        password = input("Enter the WiFi password: ")
        content = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    elif choice == '4':
        email = input("Enter the email address: ")
        subject = input("Enter the email subject: ")
        body = input("Enter the email body: ")
        content = f"mailto:{email}?subject={subject}&body={body}"
    else:
        print("Invalid choice. Exiting.")
        return

    # Create QR code
    qr = pyqrcode.create(content, encoding='utf-8')

    # Save the QR code as an image
    filename = input("Enter the filename for the QR code image (with extension): ")
    qr.png(filename, scale=8)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    generate_qr_code()
