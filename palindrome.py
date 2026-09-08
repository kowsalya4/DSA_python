n=int(input("enter :"))
org=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if org==rev:
    print("palindrome")
else:
    print("not a palindrome")
