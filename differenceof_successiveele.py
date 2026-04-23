s=[10,15,25,40,50]
differences = []
for i in range(len(s)-1):
    diff = s[i+1] - s[i]
    differences.append(diff)
    print("original list:", s)
print("differences of successive elements:", differences)
