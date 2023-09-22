# Problem 1:
# Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

sentence= "The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day"
sentence=sentence.lower()
seperateWords = sentence.split()
count=0

x=0
while True:
    if seperateWords[x]=="the":
        x=x+1
        while True:
            if "a" in seperateWords[x] :
                x=x+1
                break
            if (x<=len(seperateWords)):
                if (seperateWords[x]=="the"):
                    count=count+1
                    break
            x=x+1
    x=x+1

    if x==len(seperateWords):
        break
print(count)
