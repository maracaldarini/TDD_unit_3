# def encode(text, key):
#     cipher = make_cipher(key)
#     #print(f"cipher at encode: {cipher}")

#     ciphertext_chars = []
#     for i in text:
#         #print(cipher.index(i))
#         ciphered_char = chr(65 + cipher.index(i))
#         ciphertext_chars.append(ciphered_char)
#         #print(ciphertext_chars)
        
#     #print(ciphertext_chars)
#     return "".join(ciphertext_chars)


# def decode(encrypted, key):
#     cipher = make_cipher(key)
#     #print(f"cipher: {cipher}")
#     plaintext_chars = []
#     #print(f"plaintext_chars at beginning: {plaintext_chars}")
#     for i in encrypted:
#         #print(f"i: {i}")
#         #print(f"ord(i): {ord(i)}")
#         plain_char = cipher[ord(i) - 65]
#         #print(f"cipher[65 - ord(i): {plain_char}")
#         plaintext_chars.append(plain_char)
#     #print(f"plaintext_chars after loop: {plaintext_chars}")
#     return "".join(plaintext_chars)


# def make_cipher(key):
#     alphabet = [chr(i + 96) for i in range(1, 27)]
#     #print(f"alphabet is {alphabet}")
#     cipher_with_duplicates = list(key) + alphabet
#     #print(f"cipher with duplicates: {cipher_with_duplicates}")

#     cipher = []
#     for i in range(0, len(cipher_with_duplicates)):
#         if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
#             cipher.append(cipher_with_duplicates[i])
#     #print(f"cipher at make_cipher: {cipher}")
#     return cipher

# # When you run this file, these next lines will show you the expected
# # # and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)

def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char != " ":
            counter[char] = counter.get(char, 0) + 1
    print(f"counter: {counter}")
    print(f"sorted counter: {sorted(counter)}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(f"sorted: {(sorted(counter.items(), key=lambda item: item[1]))}")
    print(f"letter: {letter}")
    print(f"correct: {(sorted(counter.items(), key=lambda item: item[1]))[-1][0]}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")