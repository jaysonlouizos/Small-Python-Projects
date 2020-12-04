todo = input('"encrypt" or "decrypt": ')
phrase = input('what is your phrase: ')
key = int(input('what is your key: '))

def encrypt(phrase,key,message):
# this function is calle upon by calling()

    # starting the for loop
    for i in phrase:
        
        # standard offset for uppercase
        if str.isupper(i):
            offset = ord('A')
        # standard offset for lowercase
        elif str.islower(i):
            offset = ord('a')   
        # executing formula, and cycling through nonletters
        if str.isalpha(i):
            i = chr((ord(i) + key - offset) % 26 + offset)

        # adding value to existing string
        message += i

    # returning the message to be used in other programs
    return message

def calling(todo,phrase,key):
# this funcitons sets up the encrypt function by determining what it's doing what its changing and how    
    
    # starting with blank message
    message = ""
    
    # creating a reverse value for decryption
    if todo == 'decrypt':
        key = -key
    
    # returning the encrypted value using the encrypt function
    return encrypt(phrase,key,message)

phrase = (calling(todo,phrase,key))

print(phrase)
