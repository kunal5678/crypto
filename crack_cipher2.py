ciphertext = "hehidrototlewtbumnssenotvohelsetlotoueliaikhrhasidxeoofshssintofsnedsidsueedhetcimseatswaeihvaetnenuoaxsacdoptosthhdwgwneeidglstnhpuuautotatdgaeonnntlgvnpeahathredrenyidioaeythishsbntissteecutahdstnettssusntasucegerauynsofstslinhoaumrseggnrochfahrpmrethunfeseestpnonhsgdmegbleuwrroccarrhtenurnaogilvtsptnoeavnratmsrhretosoenrlieageehgigsynnitofhnrnrmorredeeeiiaberilleidoieealhwtntecltlaaniawhrhntwefsnnecaihmrioyecauiadateefeinfibrvnredotaerfventosifnwreaaheeaenhtodtaueglitrithuryostanitanisladomoeatwlorrotomaqfadsiveaniisangneionnneanghdmitripetkcrrrfiteyoaohorisaeuaideemlrrhshtoielatgee"
print(f"Total letters: {len(ciphertext)}")

from collections import Counter
freq = Counter(ciphertext)
total = sum(freq.values())
print("\nLetter Frequencies:")
for letter, count in freq.most_common():
    print(f"  {letter}: {count}  ({count/total*100:.1f}%)")

N = len(ciphertext)
ic = sum(f*(f-1) for f in freq.values()) / (N*(N-1))
print(f"\nIndex of Coincidence: {ic:.4f}")
print("~0.065 = substitution/transposition cipher")
print("~0.038 = Vigenere cipher")

import math

def columnar_decrypt(ciphertext, key_order):
    ncols = len(key_order)
    nrows = math.ceil(len(ciphertext) / ncols)
    remainder = len(ciphertext) % ncols

    # Work out how long each column is
    col_lengths = []
    for i in range(ncols):
        if remainder == 0 or i < remainder:
            col_lengths.append(nrows)
        else:
            col_lengths.append(nrows - 1)

    # Split ciphertext into columns in key order
    sorted_positions = sorted(range(ncols), key=lambda x: key_order[x])
    cols = {}
    idx = 0
    for pos in sorted_positions:
        cols[pos] = list(ciphertext[idx:idx + col_lengths[pos]])
        idx += col_lengths[pos]

    # Read off row by row
    result = ""
    for row in range(nrows):
        for col in range(ncols):
            if row < len(cols[col]):
                result += cols[col][row]
    return result
def score_text(text):
    common_words = [
        'the', 'and', 'that', 'this', 'with', 'have', 'for',
        'are', 'not', 'was', 'there', 'their', 'which', 'about',
        'would', 'could', 'every', 'good', 'very', 'after',
        'these', 'violent', 'delights', 'gentleman', 'varnish',
        'grain', 'wood', 'blind', 'treasure'
    ]
    score = 0
    t = text.lower()
    for w in common_words:
        score += t.count(w) * (len(w) ** 2)
    return score
import random

def hill_climb(ciphertext, ncols, iterations=40000):
    # Start with a random column order
    key = list(range(ncols))
    random.shuffle(key)
    current_text = columnar_decrypt(ciphertext, key)
    current_score = score_text(current_text)

    for _ in range(iterations):
        # Try swapping two random columns
        new_key = key[:]
        i, j = random.sample(range(ncols), 2)
        new_key[i], new_key[j] = new_key[j], new_key[i]

        new_text = columnar_decrypt(ciphertext, new_key)
        new_score = score_text(new_text)

        # Keep the swap only if it improved the score
        if new_score >= current_score:
            key = new_key
            current_score = new_score
            current_text = new_text

    return key, current_score, current_text

# Run hill climbing for 8 columns, 5 attempts
print("\nSearching for the correct column order...")
print("(This may take 30-60 seconds)\n")

random.seed(None)  # ← change this (remove fixed seed)
best_score = 0
best_result = ""
best_key = None

for attempt in range(10):   # ← increase from 5 to 10
    key, score, result = hill_climb(ciphertext, 8, iterations=80000)  # ← increase from 40000 to 80000
    print(f"  Attempt {attempt+1}: score={score}, preview: {result[:50]}")
    if score > best_score:
        best_score = score
        best_result = result
        best_key = key

print(f"\nBest key found: {best_key}")
print(f"Best score: {best_score}")
print(f"\nDecrypted:\n{best_result}")

KNOWN_KEY = [2, 0, 6, 3, 1, 7, 4, 5]

print("\n" + "=" * 50)
print("FINAL DECRYPTED MESSAGE (verified key):")
print("=" * 50)
print(columnar_decrypt(ciphertext, KNOWN_KEY))