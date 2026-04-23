s="The quick brown fox jumps over the lazy dog"
words=s.split()
longest=max(words,key=len)
print("The longest word is:",longest)