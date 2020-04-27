#my attempts at this project
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
def decode_message(message):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            translated_message += alphabet[(letter_index + 10) % 26]
        else:
            translated_message += letter
    return translated_message
#apparently I wasn't supposed to make this a function until step 3 but oh well

#here's the example message
coded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
print(decode_message(coded_message))

#here's the encoding function
def encode_message(message):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            translated_message += alphabet[(letter_index - 10) % 26]
        else:
            translated_message += letter
    return translated_message


#here's my example. I'll also pass my encoded message through the decoder to confirm each works.
test_message = "the eagles better draft a wide reciever tonight!"
test_encoded = encode_message(test_message)
test_decoded = decode_message(test_encoded)
print(test_encoded)
print(test_decoded)
