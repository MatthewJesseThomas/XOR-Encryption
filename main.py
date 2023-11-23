import random
import time

def timer(seconds):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= seconds:
            break

def get_five_digit_input():
    while True:
        user_input = input("Enter a 5-digit number for decryption: ")
        if user_input.isdigit() and len(user_input) == 5:
            return int(user_input)
        else:
            print("Invalid input. Please enter a 5-digit number.")

txt = "Deus Lo Vult, Mi Amor"
print(f'Original Text: {txt}')

encryption_level = 128 // 8

char_pool = ''

for i in range(0x00, 0x255):
    char_pool += chr(i)
print(char_pool)

key = ''

for i in range(encryption_level):
    key += random.choice(char_pool)

print(key)

key_index = 0
max_key_index = encryption_level - 1
encrypted_txt = ''

for char in txt:
    encrypted_char = ord(char) ^ ord(key[key_index])
    encrypted_txt += chr(encrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'Encrypted Text: {encrypted_txt}')

# Wait for 5-digit input before starting decryption timer
decryption_key = get_five_digit_input()

# Start decryption timer
timer_duration = 10  # Adjust the timer duration as needed
print(f'Decryption timer started for {timer_duration} seconds...')
timer(timer_duration)

# Decryption
key_index = 0
decrypted_txt = ''

for char in encrypted_txt:
    decrypted_char = ord(char) ^ decryption_key
    decrypted_txt += chr(decrypted_char)

print(f'Decrypted Text: {decrypted_txt}')
