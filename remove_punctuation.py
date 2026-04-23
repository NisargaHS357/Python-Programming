import string
s="Shashank is so courageous, he is a lion hearted person."
result=""
for ch in s:
    if ch not in string.punctuation:
        result+=ch
        print(result)
        