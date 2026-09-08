n=input()
#print(n[::-1])#rev
rev=""
#for ch in n:
 #   rev=ch+rev
#print(rev)#not using builtin function
if n==n[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#without slicing 
for ch in n:
    rev=ch+rev
if rev==n:
    print("palindrome")
else:
    print("not palindrome")
