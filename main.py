import pandas as pd

encryptionKey = pd.read_csv('decodekeynew.csv')

df = pd.DataFrame(data=encryptionKey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


# the caesar cipher shifts the encryption key by 4 rows down
# the 4 rows at the end of the key cannot be shifted down so it starts from the top
def caesar_cipher(char):
    # finds the encoded byte that is associated with the character
    if char == "Ѕ":
        encoded_byte = df.loc[df['Character'] == " ", 'Byte'].iloc[0]
    elif char == "І":
        encoded_byte = df.loc[df['Character'] == "!", 'Byte'].iloc[0]
    elif char == "Ї":
        encoded_byte = df.loc[df['Character'] == '"', 'Byte'].iloc[0]
    elif char == "Ј":
        encoded_byte = df.loc[df['Character'] == "#", 'Byte'].iloc[0]
    else:
        encoded_byte = df.loc[df['Character'].shift(4) == char, 'Byte'].iloc[0]

    return encoded_byte


# shifts the encryption key by 4 rows up
# the 4 rows at the top of the key cannot be shifted up so it starts from the bottom
def caesar_decode(encoded_byte):
    # finds the row that contains the correct encoded byte
    if encoded_byte == "20":
        shifted_row = df[df.eq("d085").any(1)]
    elif encoded_byte == "21":
        shifted_row = df[df.eq("d086").any(1)]
    elif encoded_byte == "22":
        shifted_row = df[df.eq("d087").any(1)]
    elif encoded_byte == "23":
        shifted_row = df[df.eq("d088").any(1)]
    else:
        shifted_row = df[df.shift(-4).eq(encoded_byte).any(1)]

    # returns the character from the row
    return shifted_row['Character'].tolist()[0]


# uses UTF-8 encoding and caesar cipher
def encrypt(message):
    message = str(message)
    if message == "":
        return "This message/password is empty"

    encoded_message = ""

    for char in message:
        try:
            encoded_message += caesar_cipher(char)

        except:
            return "unrecognized character, cannot encrypt"

    return encoded_message


def decrypt(message):
    message = str(message)
    if message == "":
        return "This message/password is empty"

    decoded_message = ""
    i = 0
    while i < len(message):
        try:
            encoded_byte = ""
            # encoded byte can either be 2 or 4 characters
            # we know that it will be 4 if the encoded byte starts with "c" or "d"
            if message[i] == "c" or message[i] == "d":
                encoded_byte += message[i]
                encoded_byte += message[i + 1]
                encoded_byte += message[i + 2]
                encoded_byte += message[i + 3]

                decoded_char = caesar_decode(encoded_byte)
                decoded_message += decoded_char
                i += 4
            else:
                encoded_byte += message[i]
                encoded_byte += message[i + 1]

                decoded_char = caesar_decode(encoded_byte)
                decoded_message += decoded_char
                i += 2
        except:
            return "error, cannot decrypt"

    return decoded_message


# testing
print(encrypt("my name is danny ! ЈЇJ"))
print(decrypt("717d2472657169246d7724686572727d24252423224e"))
print(encrypt("my name is danny ! ЈЇJ五"))
print(decrypt("717d2472657169246d7724686572727d24252423224e五"))
