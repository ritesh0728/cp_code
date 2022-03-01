#The smallest string that needs to be added in front of the input string to be made a palindrome

n=input()
c=0;cn=0
while True:
    if n[0]==n[len(n)-1-c]:
        break
    else: 
       cn+=1
        c+=1
f=1
#print(n[0],n[len(n)-cn-1])
for i in range((len(n)-cn+1)//2):
    if n[i]!=n[len(n)-cn-1-i]:
        f-=1
        break
if n==n[::-1]:
    print('None')
elif f:
    print(n[len(n)-cn:][::-1])

else:
    print(n[1:][::-1])
