from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os, sys

def encrypt(input_file, output_file, key_hex):
    key = bytes.fromhex(key_hex)
    data = open(input_file, 'rb').read()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(data, 16))
    open(output_file, 'wb').write(iv + ct)  # IV stored inside
    print(f"Encrypted → {output_file}")
    print(f"iv(hex): {iv.hex()}")

def decrypt(input_file, output_file, key_hex, iv_hex=None):
    key = bytes.fromhex(key_hex)
    data = open(input_file, 'rb').read()
    if iv_hex:
        # IV passed manually (for other students' files)
        iv = bytes.fromhex(iv_hex)
        ct = data
    else:
        # IV stored inside file (our own files)
        iv, ct = data[:16], data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    open(output_file, 'wb').write(unpad(cipher.decrypt(ct), 16))
    print(f"Decrypted → {output_file}")

# Usage:
#   python3 aes_cbc.py encrypt image.jpg output.bin <key_hex>
#   python3 aes_cbc.py decrypt output.bin image.jpg <key_hex>
#   python3 aes_cbc.py decrypt output.bin image.jpg <key_hex> <iv_hex>

if __name__ == '__main__':
    if len(sys.argv) not in [5, 6]:
        print("Usage: python3 aes_cbc.py <encrypt|decrypt> <input> <o> <key_hex> [iv_hex]")
        sys.exit(1)
    action = sys.argv[1]
    inp, out, key_hex = sys.argv[2], sys.argv[3], sys.argv[4]
    iv_hex = sys.argv[5] if len(sys.argv) == 6 else None
    if action == 'encrypt':
        encrypt(inp, out, key_hex)
    elif action == 'decrypt':
        decrypt(inp, out, key_hex, iv_hex)
