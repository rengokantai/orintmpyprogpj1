__author__ = 'Hernan Y.Ke'
import scrabble
longest=""
for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest):
        longest=word
print(longest)