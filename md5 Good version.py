#When given a hashed password out of a given dictionary this code will guess the original password 
import hashlib
#code iterates through the given dictionary
input_file = open("Dictionary.txt", "r")
dictionary = input_file.read()
dictionary = dictionary.split()
input_file.close()

#methods for hashing a password using MD5
def ha1(username, realm, password):
    md5 = hashlib.new('MD5')
    byte = username + ":" + realm + ":" + password
    byte = byte.encode('UTF-8')
    md5.update(byte)
    return md5.hexdigest()

def ha2(method, uri):
    md5 = hashlib.new('MD5')
    byte = method + ":" + uri
    byte = byte.encode('UTF-8')
    md5.update(byte)
    return md5.hexdigest()

def response(ha1, nonce, ha2):
    md5 = hashlib.new('MD5')
    byte = ha1 + ":" + nonce + ":" + ha2
    byte = byte.encode('UTF-8')
    md5.update(byte)
    return md5.hexdigest()


def main(password):
    username = "817009159"
    realm = "Mordor"
    password = str(password)
    method = "GET"
    uri = "/Public/CS/Home.png"
    nonce = "03e2abb8a924e966bee59d41cef32851"
    opaque = "4043168947418128" 

    one = ha1(username, realm, password)
    two = ha2(method, uri)
    #print("ha1 for password is:" + ha1)
    return response(one, nonce, two)
    
#output is what the stored hashed password is (we don't know the original password)
output = "4e4f4cf0f8842013aadcc83f05613845"
#for each word in the dictionary the code is hashing the word using the md5 methods and then checking the hash against the hash we have called output.
#If there is a matching hash we can confirm this word was used as the original password. 
for word in dictionary:
    endhash = main(word)
    #prints the hash and the word which was used as the password.
    if output == endhash:
        print(endhash)
        print("password is: " + word)
    
