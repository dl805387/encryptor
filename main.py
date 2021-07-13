import pandas as pd

encryptionKey = pd.read_csv('decodekeynew.csv')

df = pd.DataFrame(data=encryptionKey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


def split(message):
    message = str(message)
    array = []
    for char in message:
        array.append(char)
    return array


def encrypt(message):
    message = split(message)
    encoded_message = ""

    for i in range(len(message)):
        curr_char = message[i]

        try:
            encoded_char = df.loc[df['Character'] == curr_char, 'Byte'].iloc[0]

        except:
            print('unrecognized character')
            encoded_char = '@@@'

        encoded_message = encoded_message + encoded_char
    return encoded_message


print(encrypt("个"))

# check for empty message
