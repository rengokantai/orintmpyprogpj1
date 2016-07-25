__author__ = 'Hernan Y.Ke'
import scrabble

#words contains all vowels
vowels ="aeiou"
def has_all_vowel(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for word in scrabble.wordlist:
    if has_all_vowel(word):
        print(word)