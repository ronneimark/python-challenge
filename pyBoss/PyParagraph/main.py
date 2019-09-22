# Import a text file filled with a paragraph of your choosing.

import re

paragraph = open("manifesto.txt", "r")

strText = paragraph.read()

word_total = 0
sentence_total = 0 
# Assess the passage for each of the following:

print("")
print("Paragraph to Analyze")
print("")
print("-----------------------------")
print("")
print(strText)
print("")
print("-----------------------------")
print("")
print("Paragraph Analysis")
print("")
print("-----------------------------")
print("")

# Approximate word count

for i in range(len(strText)):
    if(strText[i]) == " ":
        word_total += 1

print(f"Approximate word count: {word_total}")

# Approximate sentence count

for i in range(len(strText)):
    if(strText[i]) == ".":
        sentence_total += 1
    elif(strText[i]) == "?":
        sentence_total += 1
    elif(strText[i]) == "!":
        sentence_total+= 1
    
print(f"Approximate sentence count: {sentence_total}")

# Approximate letter count (per word)

letters_per_word = round(len(strText)/word_total,2)

print(f"Approximate letters per word: {letters_per_word}")

# Average sentence length (in words)

words_per_sentence = round(word_total/sentence_total, 2)

print(f"Average sentence length: {words_per_sentence} words.")




