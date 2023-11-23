import random

txt = "Deus Lo Vult, Mi Amor"
print(f"Original Text: {txt}")

encryption_level = 128 // 8

char_pool = ""

for i in range(0x00, 0x255):
    char_pool += chr(i)
print(char_pool)

key = ""

for i in range(encryption_level):
    key += random.choice(char_pool)

print(key)

key_index = 0
max_key_index = encryption_level - 1
encrypted_txt = ""

for char in txt:
    encrypted_char = ord(char) ^ ord(key[key_index])
    encrypted_txt += chr(encrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f"Encrypted Text {encrypted_txt}")

# Decryption
key_index = 0

decrypted_txt = ""

for char in encrypted_txt:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_txt += chr(decrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f"Decrypted Text: {decrypted_txt}")
