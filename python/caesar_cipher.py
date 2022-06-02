def caesar_cipher(string, shift_amount):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    ciphered_text = ""

    for char in string:
        is_upper_case = char.upper() == char
        char_index = alphabet.index(char.lower())
        substitution_index = (char_index + shift_amount) % 26
        if char.lower() not in alphabet:
            ciphered_text += char
        elif is_upper_case:
            ciphered_text += alphabet[substitution_index].upper()
        else:
            ciphered_text += alphabet[substitution_index]
            
    return ciphered_text
caesar_cipher("The man from U.N.C.L.E", 13)
