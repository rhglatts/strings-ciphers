#Rebecca Glatts
#Project 2
#Problem 1

#Counts each character in the string
def get_num_of_characters(string):
    count = 0
    for char in string:
        count += 1
    return count

#Replaces whitespace in the string with nothing
def output_without_whitespace(string):
    return string.replace(" ", "")
   
#Gets the acronym of a phrase
def get_acronyn(string):
    #Splits the phrase into an array of words
    words = string.split()
    acronym = ""
    temp = ""
    #For the amount of words, gets the first letter of each word and adds it 
    #to the acronym
    for i in range(len(words)):
        temp = words[i][0]
        acronym += temp
    return acronym.upper()

#Creates a cipher using letter replacement
def get_safe(string, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    key = list(key)
    cipher = ""

    #For each character in the string, if the character equals the letter
    #in the alphabet, replace that letter with the corresponding position
    #in the key. ie: B=2, M=2, B->M
    for char in string:
        for i in range (25):
            if char == alphabet[i]:
                cipher += key[i]
                
    return cipher

#Gets user input and calls other methods
def main():
    phrase = input("Enter a sentence or phrase: ")
    print("You entered:", phrase)
    print("Number of characters:", get_num_of_characters(phrase))
    print("String with no whitespace:", output_without_whitespace(phrase))
    phrase = input("Enter a phrase to generate an acronym: ")
    acronym = get_acronyn(phrase)
    print("The acronym is: ", acronym)
    key = input("Enter a key with 26 characters: ")
    code = get_safe(acronym, key)
    
    print("Encrypting RAM using the key ", key,":", code)
    

main()

"""
Tests:

Enter a sentence or phrase: This is a test
You entered: This is a test
Number of characters: 14
String with no whitespace: Thisisatest
Enter a phrase to generate an acronym: central processing unit
The acronym is:  CPU
Encrypting RAM using the key ZMNXBCVALDKSJFHGPQOWIEURYT: NGI

Enter a sentence or phrase: hello how are you
You entered: hello how are you
Number of characters: 17
String with no whitespace: hellohowareyou
Enter a phrase to generate an acronym: computer processing unit
The acronym is:  CPU
Enter a key with 26 characters: LZXBFITKYDWPHRCMGVSOUNAJEQ
Encrypting RAM using the key  LZXBFITKYDWPHRCMGVSOUNAJEQ : XMU

Enter a sentence or phrase: this is a program
You entered: this is a program
Number of characters: 17
String with no whitespace: thisisaprogram
Enter a phrase to generate an acronym: to be honest
The acronym is:  TBH
Enter a key with 26 characters: XKJIVGZMUWBSATHYPFCEOQRDNL
Encrypting RAM using the key  XKJIVGZMUWBSATHYPFCEOQRDNL : EKM
"""
