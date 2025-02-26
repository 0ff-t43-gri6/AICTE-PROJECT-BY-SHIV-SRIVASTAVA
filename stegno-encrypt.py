import cv2
import os

img = cv2.imread("mypic.jpg")
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
for i in range(255):
    d[chr(i)] = i

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")
print("Message encrypted successfully!")