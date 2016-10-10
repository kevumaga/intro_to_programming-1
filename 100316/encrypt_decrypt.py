#Enryption and Decryption Assignment
#This program uses The Vigenère Cipher Method and was wrtiten by:
#Joshua Ihejiamaizu; Ahmad Bilesanmi; Kelvin Wachira and Thabiso Mokoena 

#We assign the key to be any string of random characters from the ALPHABETS.
#The key can be any length, may not be a correct dictionary word and is in UPPER case. 
import time, os, sys

ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#get the text in the file
def get_content(filename):
	if not os.path.exists(filename):
		print('The file %s does not exist. Quitting...' % (filename))
		sys.exit()
	f = open(filename, 'r+')
	my_content = f.read()
	f.close()
	return my_content

#decrypt function
def encrypt_content(key, content):
	return translate_content(key, content, 'encrypt')

#encrypt function
def decrypt_content(key, content):
	return translate_content(key, content, 'decrypt')

#This is the function that does the actual encypting or decrypting
def translate_content(key, content, mode):
	translated = []

	key_index = 0
	key = key.upper()

	for alphabet in content:
		its_ordinal = ALPHABETS.find(alphabet.upper()) #find the index or ordinal of the upper case of the alphabet in ALPHABETS
		if its_ordinal != -1: # -1 means that it is not an alphabet
			if mode == 'encrypt':
				its_ordinal += ALPHABETS.find(key[key_index]) #add the value of the index of the first alphabet of the key
			elif mode == 'decrypt':
				its_ordinal -= ALPHABETS.find(key[key_index]) #subtract the value of the index of the first alphabet of the key

			its_ordinal %= len(ALPHABETS) #this checks that the ordinal does not exceed or fall short of the index of the ALPHABET

			if alphabet.isupper():
				translated.append(ALPHABETS[its_ordinal])
			elif alphabet.islower():
				translated.append(ALPHABETS[its_ordinal].lower())

			key_index += 1
			if key_index == len(key): #reset the key to start from the beginning arter its length is exhausted
				key_index = 0
		else:
			translated.append(alphabet)

	return ''.join(translated)

#the main function that contains the key, file and mode
def crypt_file(filename):
	filecontent = get_content(filename)
	my_key = 'DZEKOEDIN'
	my_mode = 'decrypt'

	if my_mode == 'encrypt':
		translated = encrypt_content(my_key, filecontent)
	elif my_mode == 'decrypt':
		translated = decrypt_content(my_key, filecontent)

	f = open(filename, 'r+')
	f.write(translated)
	f.close()
	
	if my_mode == 'encrypt':
		print('The file has been encrypted successfully')
	else:
		print('The file has been decrypted successfully')

if __name__ == '__crypt_file__':
	crypt_file()

crypt_file('meltwater.txt')