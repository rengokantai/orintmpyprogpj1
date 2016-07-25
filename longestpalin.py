__author__ = 'Hernan Y.Ke'
import scrabble
longest=""
for word in scrabble.wordlist:
    ispalin=True
    for index in range(len(word)):
        if word[index]!=word[-(index+1)]:
            ispalin=False
    if ispalin and len(word)>len(longest):
        longest=word
print(longest)