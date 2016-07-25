__author__ = 'Hernan Y.Ke'
import scrabble
import string
#print all words containing aa

for word in scrabble.wordlist:
    if "aa" in word:
        print(word)

#any letter doubles in the word
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter*2 in word:
            exists = True
            break
    if not exists:
        print("No word with double" + letter)
