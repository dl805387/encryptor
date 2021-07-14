import pandas as pd

encryptionKey = pd.read_csv('decodekeynew.csv')

df = pd.DataFrame(data=encryptionKey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


def encrypt(message):
    message = str(message)
    if message == "":
        return "This message/password is empty"

    encoded_message = ""

    for char in message:
        try:
            # finds the encoded byte that is associated with the character
            encoded_char = df.loc[df['Character'] == char, 'Byte'].iloc[0]

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
        except:
            return "error, cannot decrypt"

    return decoded_message
