import os
import pyaes

#open files
file_name = "foto.jpg.pyghost"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = b"uvNk2dMl6wqGN7xq17KmtmK8wgBAjewk" 
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file_name = "foto.jpg"
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()
print('✅🍕 Successfully decrypted file')