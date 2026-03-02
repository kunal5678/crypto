from collections import Counter

ciphertext = "qkgszbdekfinjvnnocxhomnfnjfdakfkszxbiksnbwtasjfofutnwhihqkeimmubikwfyzmwxkrtmhmmaabcxgcutpfftrofxswoyojhcmbryuucolbqshvhkvzmkfjxsnnmzcasacmsnjeufiflafjjbsglotnxowmywbybcaxunyjyliwcxsaprcswjgqeebxsmprcybeyindndmxqfgqxblvvzcezjqqjfmubmkdrdubprcyliicczkuzjqqjjwbniezwehckvczziubkdxiscdkvxapotujcocdroitmxcaukvqbmqxfjktniezrducnochaflgrjmlwxhophxblmjlnqfblyksmfxikxxjvnjnuyafsefqwthqkcgbaplmjkajhxprgrpplavpqqbcdokwxoyuzabjvnnokxgpmctdcxwwckuzgncfvznlwuwwcspiitfonivrowqsxzaizjbqhuakuyxyjmiendqnwxfxhnybzinigxiovmboajvpcufqadjfmxuvkovebnuwgfgtuvuyxdhnjdkxpjnpfqcjvaaoithezzzawtguweimmflqjlxygxjdqkxbl"

# -------------------------
# 1) Calculate IC
# -------------------------
N = len(ciphertext)
freq = Counter(ciphertext)

top = 0
for f in freq.values():
    top += f * (f - 1)

ic = top / (N * (N - 1))
print("Index of Coincidence:", round(ic, 4))


# -------------------------
# 2) Try key lengths
# -------------------------
def average_ic(text, key_len):
    total_ic = 0

    for i in range(key_len):
        sub = text[i::key_len]
        N = len(sub)

        if N < 2:
            continue

        freq = Counter(sub)

        top = 0
        for f in freq.values():
            top += f * (f - 1)

        total_ic += top / (N * (N - 1))

    return total_ic / key_len


print("\nTesting key lengths:")
for k in range(2, 16):
    print("Key length", k, "IC =", round(average_ic(ciphertext, k), 4))


# -------------------------
# 3) Guess key (assume most common letter = 'e')
# -------------------------
KEY_LEN = 14
key = ""

for i in range(KEY_LEN):
    sub = ciphertext[i::KEY_LEN]
    
    best_shift = 0
    best_score = -1

    for shift in range(26):
        decrypted = ""
        for c in sub:
            new_char = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            decrypted += new_char
        
        # Simple English test
        score = decrypted.count('e') + decrypted.count('t')
        
        if score > best_score:
            best_score = score
            best_shift = shift

    key_letter = chr(ord('a') + best_shift)
    key += key_letter

print("Better guessed key:", key.upper())

# -------------------------
# 4) Decrypt
# -------------------------
def vigenere_decrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        shift = ord(key[key_index % len(key)]) - ord('a')
        new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        result += new_char
        key_index += 1

    return result


plaintext = vigenere_decrypt(ciphertext, key)
print("\nDecrypted message:")
print(plaintext)