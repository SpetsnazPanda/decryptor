
import sys
import os

EXTENSION = ".dokb"

def decrypt(data):
    result = bytearray(len(data))

    for i in range(len(data)):
        b = data[i] & 0xFF

        # Menggeser bit ke kanan satu posisi
        result[i] = ((b >> 1) | (b << 7)) & 0xFF

    return bytes(result)


if len(sys.argv) < 2:
    print(f"Usage: python3 decrypt.py <file{EXTENSION}>")
    sys.exit(1)

filepath = sys.argv[1]

if not filepath.endswith(EXTENSION):
    print("Error: File harus memiliki ekstensi .dokb")
    sys.exit(1)

if not os.path.isfile(filepath):
    print("Error: File tidak ditemukan")
    sys.exit(1)

with open(filepath, "rb") as f:
    encrypted = f.read()

decrypted = decrypt(encrypted)

original_name = filepath[:-len(EXTENSION)]

if os.path.exists(original_name):
    print(f"Error: File tujuan sudah ada: {original_name}")
    sys.exit(1)

with open(original_name, "wb") as f:
    f.write(decrypted)

print(f"Decrypted: {original_name}")
