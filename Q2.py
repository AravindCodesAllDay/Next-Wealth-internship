sentence = "I am the King"
key = 2

words = sentence.split()
seperateWords = []

for i, word in enumerate(words):
    if (i + 1) % 2 == 1:
        Seperateword = ''.join([chr(ord(letter) + key) for letter in word])

print(seperateWords)
