s={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print("Original Dictionary:", s)
for key in list(s.keys()):
    if key in [2, 3, 5]:  
        s.pop(key)  
print("Dictionary after removing prime number keys:", s)
