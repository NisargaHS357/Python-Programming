s="nisargashetty357@gmail.com"
digits=""
letters=""
special=""
for ch in s:
    if ch.isdigits():
        digits+=1
    elif ch.isalpha():
        letters+=1
    else:
        special+=1
print("The number of digits in the email is:",digits)
print("The number of letters in the email is:",letters) 
print("The number of special characters in the email is:",special)

