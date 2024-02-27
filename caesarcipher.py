# this will take a string and output the string encrypted using the Caesar Cipher

def Encrypt(string, offset):
    
    strunpacked = [*string]
    encrypted = ""
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for letter in strunpacked:
        try:
            element = letters.index(letter)
        except:
            encrypted = encrypted + letter
            continue
        
        if element + offset > 25:
            newletter = 25 - (element + offset)
            element = abs(newletter)-1
            encrypted = encrypted + letters[element]
        else:
            element = element + offset
            encrypted = encrypted + letters[element]
            
        

    return encrypted




string = input("What is the string you want encrypt?")
offset = input("How much to offset by?")

encryptedString = Encrypt(string,int(offset))

print("The encrypted string is: ",encryptedString)