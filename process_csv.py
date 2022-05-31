import pandas as pd

from image_search import googleImageSearch, googleSearch

def conversion(text):
    if(text):
        return googleImageSearch(text)
        # return text
    return ""
    

df = pd.read_csv("in.csv")

df['Images'] = df['Name'] + " " + df['Category']
print(df.head(5))

df['Images'] = df['Images'].apply(conversion)
print(df.head(5))

df.to_csv('out.csv', index=False)