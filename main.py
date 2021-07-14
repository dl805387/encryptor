import pandas as pd

encryptionKey = pd.read_csv('decodekeynew.csv')

df = pd.DataFrame(data=encryptionKey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


def encrypt(message):
    message = str(message)
    encoded_message = ""

    for char in message:
        try:
            # finds the encoded byte that is associated with the character
            encoded_char = df.loc[df['Character'] == char, 'Byte'].iloc[0]

        except:
            print('unrecognized character')
            encoded_char = '@@'

        encoded_message += encoded_char
    return encoded_message


# print(encrypt("€"))
print(encrypt(" €   hello world "))

# check for empty message
# add comments to code


def decrypt(message):
    message = str(message)
    decoded_message = ""
    i = 0
    while i < len(message):
        curr_byte = ""
        # encoded byte can either be 2 characters or 4
        # we know that it will be 4 if the encoded byte starts with c
        if message[i] == "c":
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
    return decoded_message


# c280
# print(decrypt(encrypt("€ will this work?")))

# these below dont work; need error handling
# print(decrypt("@"))
# print(decrypt("111"))
print(len(decrypt("20c28020202068656c6c6f20776f726c6420")))

