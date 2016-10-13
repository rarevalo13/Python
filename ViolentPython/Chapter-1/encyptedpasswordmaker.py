import hashlib	
pw = input("Please input a password: ")
encryptpw = hashlib.sha1(pw.encode('utf-8'))
dictFile = open('words.txt', 'r')
print(encryptpw.hexdigest().strip('b'))