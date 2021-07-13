import pandas as pd

encryptionKey = pd.read_csv('decodekeynew.csv')

df = pd.DataFrame(data=encryptionKey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

#print(df)


def split(message):
    message = str(message)
    array = []
    for char in message:
        array.append(char)
    return array


print(split("33" + " he"))
