
import sys
import getopt
from random import randint
 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
def usage():
    print 'Usage: python alberti.py "text you want to encode"'
 
def main(argv):
    if len(argv[1:]) < 1:
        usage()
        sys.exit(2)
    else:
        print (argv[1:][0]).lower()
        print processText((argv[1:][0]).lower())
 
def processText(text):
    out = ""
    offset = 0
    count = 0
    while len(text) > 0:
        char = text[0]
        text = text[1:]
        if char not in alphabet: # just pass blanks
            out = out + char
            continue
        else:  #lookup character
            result = alphabet[(alphabet.find(char)+offset)%26]
        if randint(0,26) == 13: # change char sets occasionally
            offset = randint(0,26)
            count = count + 1
            result = result.upper()
        out = out+result
    print 'number of offset changes:',count
    return out
 
if __name__ == "__main__":
    main(sys.argv)