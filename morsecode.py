# this will take a string and output the string encrypted using the Caesar Cipher
from colorama import Fore


def Encrypt(string):
    
    lowercase = string.lower()
    strunpacked = [*lowercase]
    converted = ""
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
    
    
    
    for letter in strunpacked:
        if letter == " ":
            converted = converted + "/ "
            continue
        

        try:
            element = letters.index(letter)
        except:
            converted = converted + letter + " "
            continue
        
        
        converted = converted + code[element] + " "
            
        

    return converted




string = input("What is the string you want convert to Morse Code?")

morseCode = Encrypt(string)

print(Fore.WHITE + "The Morse code for " + Fore.RED + string + " is: " + Fore.GREEN + morseCode + Fore.WHITE)