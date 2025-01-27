# TODO 1 - create a function called encrypt() that takes 'original_text' and 'shift_amount' as two inputs
import string

def encrypt(original_text, shift_amount) :
    alphabet = list(string.ascii_lowercase)
    """
    TODO 2 - Inside the 'encrypt' function, shift each letter of the original_text forwards in
    the alphabet by the and print the encrypted text
    You can use the built-in Python index() function to find out the position of an item in
    a list e.g.
    
    fruits = ['Apple', 'Pear', 'Orange']
    fruits.index('Pear') -> returns 1
    """
    #print(f'Original Text: {original_text}')
    cipher_text = ''
    for letter in original_text:
        #index_of_letter = alphabet.index(letter)
        shifted_position = alphabet.index(letter) + shift_amount
        #print(f'Index of letter: {index_of_letter}')
        #print(f'Shifted position: {shifted_position}')
        """
        TODO 4 - What happens if you try to shift z forwards by 9? can you fix the code 
        """
        if shifted_position > 25:
            shifted_position = shifted_position - 26
        cipher_text += alphabet[shifted_position]
    print(f'Encoded Word: {cipher_text}')

"""
TODO - 5 Create a function called decrypt() that takes 'original_text' and 'shift_amount' 
as two inputs
"""
def decrypt(original_text, shift_amount):
    alphabet = list(string.ascii_lowercase)
    cipher_text = ''
    """
    TODO 6 - Inside the decrypt() function, shift the letters of the 'original_text' by the
    shift amount and print the decrypted text
    """
    for letter in original_text:
        index_of_letter = alphabet.index(letter)
        shifted_position = alphabet.index(letter) - shift_amount
        #print(f'Index of letter: {index_of_letter}')
        #print(f'Shifted position: {shifted_position}')
        if shifted_position < 0:
            shifted_position = shifted_position + 26
        cipher_text += alphabet[shifted_position]
    print(f'Decoded Word: {cipher_text}')

def caesar(encode_or_decode, original_text, shift_amount):
    alphabet = list(string.ascii_lowercase)
    cipher_text = ''
    for letter in original_text:
        # Check to see if character is in ascii lower case alphabet
        # if not, don't do anything
        if letter not in string.ascii_lowercase:
            cipher_text += letter
        # else shift the lower case letter based on encode or decode
        else:
            # shift based on encode or decode direction
            if encode_or_decode == 'encode':
                shifted_position = alphabet.index(letter) + shift_amount
            else:
                shifted_position = alphabet.index(letter) - shift_amount
            if shifted_position < 0:
                shifted_position = shifted_position + 26
            elif shifted_position > 25:
                shifted_position = shifted_position - 26
            cipher_text += alphabet[shifted_position]
    if encode_or_decode == 'encode':
        print(f'{encode_or_decode}d word: {cipher_text}')
    elif encode_or_decode == 'decode':
        print(f'{encode_or_decode}d word: {cipher_text}')
