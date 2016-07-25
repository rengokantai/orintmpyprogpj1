__author__ = 'Hernan Y.Ke'

LIST = "test.txt"
wordlist = open(LIST).readlines()

wordlist=[word.lower().strip() for word in wordlist]
scores = {"a":1,"b":4,"c":7,"d":1,"e":8,"f":2,"g":3,"h":7,"i":1,"j":3,"k":1,"l":1,"m":4,"n":2,"o":2,"p":6,"q":4,"r":9,"s":2,"t":3,"u":3,"v":3,"w":6,"x":2,"y":2,"z":5}
#print(len(scores))
