s=[1,3,7,9,4,6,8]
leftmost_even=None
for num in s:
    if num % 2 == 0:
        leftmost_even: int = num
        break
    if leftmost_even is not None:
        print("leftmoat even number:",leftmost_even)
    else:
        print("no even number found in the list")
