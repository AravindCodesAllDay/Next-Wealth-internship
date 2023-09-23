# Problem 1:
# Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

# input string
sentence= "The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day"

def findingCountOfThe(sentence) :
    # Convert the the sentence into lower case
    sentence=sentence.lower()
    #appending each word into a list
    seperateWords = sentence.split()
    #declared a variable to keep count of
    count=0
    x=0
    #looping each value in the list to find the word "the"
    while True:
        if (seperateWords[x]=="the"):
            x=x+1
            #checking is there are any presence of "a" in between "the"s
            while True:
                if ("a" in seperateWords[x])or(x>len(seperateWords)) :
                    break
                if (seperateWords[x]=="the"):
                    count=count+1
                    x=x-1
                    break
                x=x+1
        x=x+1
        #condition to break the loop
        if x==len(seperateWords):
            break
    return count
#printing the final count
print(f"Answer = {findingCountOfThe(sentence)}")

#Output:
# sentence="The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day"
# answer = 3
#it also considers the occurence of "a" between words