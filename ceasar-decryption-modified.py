
#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
        result += chr((ord(char) - s - 32) % 96 + 32) 
    return result 
  
#check the above function 
text = "#)A)~C`A"
s = 4
print "Text  : " + text 
print "Shift : " + str(s) 
print "Cipher: " + encrypt(text,s) 
