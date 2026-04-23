s="Shashank"
count=0
for ch in s:
    if ch.lower()in "aeiou":
        count+=1
print("The number of vowels in the string is:",count)