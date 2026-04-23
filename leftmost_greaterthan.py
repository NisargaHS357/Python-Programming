s=[1,3,7,9,4,6,8]
even_numbers=[num for num in s if num%2==0]
if even_numbers:
    leftmost_even=even_numbers[0]
    print("leftmost even number:",leftmost_even)