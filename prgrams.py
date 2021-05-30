# Python program to find smallest number in a list

 
list1 = [10, 20, 4, 45, 99]
 
list1.sort()
 
print("Smallest element is:", *list1[:1])

# 2 Python program to find smallest number in a list

l=[ int(l) for l in input("List:").split(",")]
print("The list is ",l)
 
min1 = l[0]
 
for i in range(len(l)):
 
    
    if l[i] < min1:
        min1 = l[i] 
 
print("The smallest element in the list is ",min1)


#Program to find the largest number in a list. 
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])

#Python Program to check if a number is a prime number. 

a=int(input("Enter number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")


 #Python Program to find the second largest number in a list.

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Second largest element is:",a[n-2])


# Python program to print Even Numbers in given range
  
start, end = 4, 19
  

for num in range(start, end + 1):
      

    if num % 2 == 0:
        print(num, end = " ")


 # Python program to print Even Numbers in given range
  
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
  
for num in range(start, end + 1):
      
    if num % 2 == 0:
        print(num, end = " ")


  
 # To Create Star pattern
rows = 10
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")


#start 5 and End 1 Star Pattern
    rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


#quilateral triangle Pyramid 
    print("Print equilateral triangle Pyramid using asterisk symbol ")

size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")

#Sandglass pattern of star

    rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# Pyramid of horizontal tables of numbers
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()






