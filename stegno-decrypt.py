import cv2

img = cv2.imread("encryptedImage.jpg")

c = {}
for i in range(255):
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

stored_password = input("Enter the original passcode: ")
pas = input("Enter passcode for decryption: ")

if stored_password == pas:
    msg_length = int(input("Enter the length of the original message: "))
    for i in range(msg_length):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Authentication failed - incorrect passcode")