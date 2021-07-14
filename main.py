import pandas as pd

encryptionKey = pd.read_csv('decodekeynew.csv')

df = pd.DataFrame(data=encryptionKey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


def caesar_cipher(char):
    # the caesar cipher shifts the encryption key by 4 characters down
    # the 4 characters at the end of the key cannot be shifted down so it starts from the top
    if char == "Ѕ":
        shifted_code = df.loc[df['Character'] == " ", 'Byte'].iloc[0]
    elif char == "І":
        shifted_code = df.loc[df['Character'] == "!", 'Byte'].iloc[0]
    elif char == "Ї":
        shifted_code = df.loc[df['Character'] == '"', 'Byte'].iloc[0]
    elif char == "Ј":
        shifted_code = df.loc[df['Character'] == "#", 'Byte'].iloc[0]
    else:
        shifted_code = df.loc[df['Character'].shift(4) == char, 'Byte'].iloc[0]

    return shifted_code


def encrypt(message):
    message = str(message)
    if message == "":
        return "This message/password is empty"

    encoded_message = ""

    for char in message:
        try:
            # finds the encoded byte that is associated with the character
            encoded_char = caesar_cipher(char)

        except:
            return "unrecognized character, cannot encrypt"

        encoded_message += encoded_char
    return encoded_message


def decrypt(message):
    message = str(message)
    if message == "":
        return "This message/password is empty"

    decoded_message = ""
    i = 0
    while i < len(message):
        try:
            curr_byte = ""
            # encoded byte can either be 2 characters or 4
            # we know that it will be 4 if the encoded byte starts with "c" or "d"
            if message[i] == "c" or message[i] == "d":
                curr_byte += message[i]
                curr_byte += message[i + 1]
                curr_byte += message[i + 2]
                curr_byte += message[i + 3]

                # .eq is used to find the row that contains the correct byte
                row = df[df.eq(curr_byte).any(1)]
                # gets the character from the row
                curr_char = row['Character'].tolist()[0]
                decoded_message += curr_char
                i += 4
            else:
                curr_byte += message[i]
                curr_byte += message[i + 1]

                # .eq is used to find the row that contains the correct byte
                row = df[df.eq(curr_byte).any(1)]
                # gets the character from the row
                curr_char = row['Character'].tolist()[0]
                decoded_message += curr_char
                i += 2
        except:
            return "error, cannot decrypt"

    return decoded_message





# Є   Ѕ І Ї Ј
print(encrypt("Ј"))
print(caesar_cipher("Ј"))
