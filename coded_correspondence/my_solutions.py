#my attempts at this project
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
def decode_message(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            translated_message += alphabet[(letter_index + offset) % 26]
        else:
            translated_message += letter
    return translated_message
#apparently I wasn't supposed to make this a function until step 3 but oh well

#here's the example message
coded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
print(decode_message(coded_message, 10))

#here's the encoding function
def encode_message(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_index = alphabet.find(letter)
            translated_message += alphabet[(letter_index - offset) % 26]
        else:
            translated_message += letter
    return translated_message


#here's my example. I'll also pass my encoded message through the decoder to confirm each works.
test_message = "the eagles better draft a wide reciever tonight!"
test_offset = 10
test_encoded = encode_message(test_message, test_offset)
test_decoded = decode_message(test_encoded, test_offset)
print(test_encoded)
print(test_decoded)


#Now I have to make these functions. previously I didn't have a variable set in the function for the offset of letters
#I'll add these and adjust the tests as well

#Next I have to decode two more messages
message1 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
print(decode_message(message1, 10))

message2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
print(decode_message(message2, 14))


#step 4 has me trying to figure out an offset for a coded message without being told.
message3 = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
print(decode_message(message3, 7))


#new decoder below.
keyword1 = 'friends'
last_message = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'

def vigenere_decoder(message, keyword):
    keyword_phrase = ''
    keyword_index = 0
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_phrase += message[i]
        else:
            keyword_phrase += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
    translated_message = ''
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            new_index = alphabet.find(message[i]) - alphabet.find(keyword_phrase[i])
            translated_message += alphabet[new_index % len(alphabet)]
        else:
            translated_message += message[i]
    return translated_message

print(vigenere_decoder(last_message, keyword1))


#and finally the encoder with a check using the decoder
def vigenere_encoder(message, keyword):
    keyword_phrase = ''
    keyword_index = 0
    for i in range(0, len(message)):
        if message[i] in punctuation:
            keyword_phrase += message[i]
        else:
            keyword_phrase += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)
    translated_message = ''
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            new_index = alphabet.find(message[i]) + alphabet.find(keyword_phrase[i])
            translated_message += alphabet[new_index % len(alphabet)]
        else:
            translated_message += message[i]
    return translated_message

actual_last_message = 'i hope the reciever the eagles drafted is going to be good!'
actual_last_keyword = 'spongebob'
print(vigenere_encoder(actual_last_message, actual_last_keyword))
last_coded = vigenere_encoder(actual_last_message, actual_last_keyword)
print(vigenere_decoder(last_coded, actual_last_keyword))
