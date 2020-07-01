
#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Decrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) - s - 65) % 26 + 65) 
  
        # Decrypt lowercase characters 
        else: 
            result += chr((ord(char) - s - 97) % 26 + 97) 
  
    return result 
  
#check the above function 
text = "QsleqihrEwpeq"
s = 4
print "Cipher  : " + text 
print "Shift : " + str(s) 
print "Text: " + encrypt(text,s) 
