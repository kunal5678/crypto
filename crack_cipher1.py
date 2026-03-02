ciphertext = "xzkfkrfkuhlrwqmwijkrurwxxzswauswxzkchfjvrjfkrvqxzrxxzkfksuwhmukswslraswswarwqlhfkuhlkzriiqxrjkwxrwvuhlkphfxmwrxkhiihfxmwsxqlrqphflxzkxchusvkuhpxzkjrvvkfhwczsbzuhlklkwlhmwxtmxxzkfhmwvuhpxzrxjrvvkflmuxtklrvkhpuxmppxhuxrwvckrfrwvxkrfrwvxzkfksuwhumtuxsxmxkphfxzhfhmazahswarfvkwxrwvuswbkfkkrfwkuxwkuuzkursvuhlkxzswarthmximwbxmrjsxqtkswahwkhpxzklswhfosfxmkuczsbzckvhwhxrbgmsfkmwxsjjrxkfswjspkrjjckzrokxhvkbsvksuczrxxhvhcsxzxzkxslkxzrxsuasokwmuxzswaucsxzhmxrjjfklkvquzhmjvtkcsxzhmxfkarfvczrxuvhwksuvhwkzkxzrxcrwxulhwkqlkrwurwvbhwxkwxsucsxzhmxxzfkkahhvpfskwvuxzkifrsukhprphhjsuswbkwukxhxzkcsukuxhpmuh"
print(f"Total letters: {len(ciphertext)}")

from collections import Counter

freq = Counter(ciphertext)
total = sum(freq.values())

print("\nLetter Frequencies:")
for letter, count in freq.most_common():
    print(f"  {letter}: {count}  ({count/total*100:.1f}%)")

N = len(ciphertext)   # total number of letters
top = 0
for f in freq.values():
    top += f * (f - 1)
bottom = N * (N - 1)
ic = top / bottom
print("\nIndex of Coincidence:", round(ic, 4))
print("~0.065 = substitution cipher")
print("~0.038 = Vigenere")

def ngrams(text, n):
    return Counter([text[i:i+n] for i in range(len(text)-n+1)])

print("\nTop 10 Bigrams:")
for bg, count in ngrams(ciphertext, 2).most_common(10):
    print(f"  '{bg}': {count}")

print("\nTop 10 Trigrams:")
for tg, count in ngrams(ciphertext, 3).most_common(10):
    print(f"  '{tg}': {count}")

mapping = {
    'x': 't', 'z': 'h', 'k': 'e',
    'r': 'a', 'w': 'n', 'h': 'o', 'u': 's',
    's': 'i', 'f': 'r', 'v': 'd', 'm': 'u',
    'l': 'm', 'j': 'l', 'c': 'w', 'b': 'c',
    'p': 'f', 'a': 'g', 'i': 'p', 'q': 'y',
    't': 'b', 'o': 'v', 'g': 'q',
}

def decrypt(text, mapping):
    result = ""
    for char in text:
        result += mapping.get(char, '_')
    return result

print("\nPartial decryption (only 3 letters known):")
print(decrypt(ciphertext, mapping))

