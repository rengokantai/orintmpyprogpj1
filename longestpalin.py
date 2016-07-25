__author__ = 'Hernan Y.Ke'
import scrabble
longest=""
for word in scrabble.wordlist:
    if list(word) == list(word[::-1]) and len(word) > len(longest):
        longest=word
print(longest)