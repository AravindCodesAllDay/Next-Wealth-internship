def encodeWord(word, key):
    encoded = ""
    for letter in word:
        # Calculate the new letter after shifting by the key positions
        encodedLetter = chr(ord(letter) + key)
        encoded += encodedLetter
    return encoded

def encodeSentence(sentence, key):
    words = sentence.split()
    encodedWords = []

    for i, word in enumerate(words):
        # Reverse the word if it's in an even position
        if i % 2 == 0:
            word = word[::-1]
        encodedWord = encodeWord(word, key)
        encodedWords.append(encodedWord)

    encoded_sentence = " ".join(encodedWords)
    return encoded_sentence

# Input sentence and key
sentence = "I am the King"
key = 2

# Encode the sentence
encodedSentence = encodeSentence(sentence, key)

# Print the encoded sentence
print(encodedSentence)
