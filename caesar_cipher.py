logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# index ranges from 0 to 25

def caesar(text, shift, direction):
	new_text = ''
	if direction == 'decode':
		shift *= -1
	for letter in text:
		if letter in alphabet:
			index = alphabet.index(letter)
			new_index = index + shift
			if new_index > 25 or new_index < -26:
				new_index %= len(alphabet)

			new_text += alphabet[new_index]
		else:
			new_text += letter

		# if direction == 'encode':
		# 	enc_index = alphabet.index(letter) + shift
		# 	if enc_index>25:
		# 		enc_index -= len(alphabet)
		# 	new_text += alphabet[enc_index]

		# if direction == 'decode':
		# 	dec_index = alphabet.index(letter) - shift
		# 	new_text += alphabet[dec_index]

	print(f'{direction}d text is: {new_text}')

# def encrypt(text, shift):
# 	#shift each letter in the text by the given shift number
# 	encrypt_text = ''
# 	for letter in text:
# 		# add the shift index to the original index in alphabet
# 		enc_index = alphabet.index(letter) + shift
# 		# if shift index is more than 25 then circle back to start of the list
# 		if enc_index>25:
# 			enc_index -= len(alphabet)
# 		encrypt_text += alphabet[enc_index]
		
# 	print(encrypt_text)

# def decrypt(text, shift):
# 	decrypt_text = ''
# 	for letter in text:
# 		dec_index = alphabet.index(letter) - shift
# 		decrypt_text += alphabet[dec_index]

# 	print(decrypt_text

# caesar(text, shift, direction)

continue_cipher = True
while continue_cipher:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	caesar(text, shift, direction)

	choice = input('Enter \'yes\' to continue, \'no\' to exit: ')
	if choice == 'no':
		continue_cipher = False
		print('Good Bye')
