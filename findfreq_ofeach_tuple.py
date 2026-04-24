t = (1, 2, 2, 3, 3, 3, 4)

freq = {}

for i in t:
    freq[i] = freq.get(i, 0) + 1

print("Frequencies:")
for key, value in freq.items():
    print(key, ":", value)
