a=int(input('Enter first no:'))
b=int(input('Enter second no:'))
s1='Both Are Equal'
s2='First Number is Greater Than Second Number'
s3='First Number is Less Than Second Number'
print(s1 if a == b else s2 if a>b else s3)
