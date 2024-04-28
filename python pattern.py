1 .    for i in range(5):
            for j in range(i+1):
               print(j+1,end=" ")
           print()


2. n = int(input())

for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
    


3. 

   n = int(input())
val = 1
for i in range(n):
    for j in range(i+1):
        print(val,end=" ")
        val= val + 1
    print()

output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 



4.
n = int(input())

for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()

output:
* 
# # 
* * * 
# # # # 


5.   
    n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*",end = " ")
    print()

output:
* * * * * 
* * * * 
* * * 
* * 
* 


6.   
     n = int(input())
space = n-1
start= 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print("*",end = " ")
    print()

    space= space-1
    start = start+1

output:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 


7.
     n = int(input())
space = n-1
start= 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print(j+1,end = " ")
    print()

    space= space-1
    start = start+1

output:
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 


8.  
	n = int(input())
space = n-1
start= 1
val = 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print(val,end = " ")
        val= val + 1
    print()

    space= space-1
    start = start+1

output:
      1 
    2 3 
  4 5 6 
7 8 9 10 


9>  
   n = int(input())
space = n-1
start= 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print("*",end = " ")
    print()

    space= space-1
    start = start+1

output: 
      * 
    * * 
  * * * 
* * * * 

10.  
	l = [15, 18, 2, 22, 181,2,45]
n = len(l)
target = 2
result = 0

for index in range(n):
    if l[index]==target:
        result = result + 1

print("total no of occurrenceis ",result)


output:
	total no of occurrenceis  2




11.
	def findtotaloccurences(listofnumbers, target):
    result = 0
    n = len(listofnumbers)
    for index in range(n):
        if listofnumbers[index] == target:
            result = result + 1
        return result

listofnumbers = [12,34,21,-12,34,55,56,34,12]
target = 35

result = findtotaloccurrences(list2,target2)
print(result)

output: error


12.
	def totalevenno(l):
    result = 0
    n = len(l)
    for index in range(n):
        if l[index] %2 == 0:
            result = result + 1
    return result

l = [12,34,21,-12,34,55,56,34,12]

result = totalevenno(l)
print("total even numbers is",result)

:output:
 	total even numbers is 7


13.

	def findgreaterelement(nmbers):
    result = 0
    n = len(numbers)

    for index in range(n):
        if numbers[index] > result:
            result = numbers[index]
    return result

numbers = [12,34,21,-12,34,55,34,11]
result = findgreaterelement(numbers)
print("greatest number is:" , result)


output:
	greatest number is: 55



14.	def findsmallerelement(numbers):
    result = 100
    n = len(numbers)

    for index in range(n):
        if numbers[index] < result:
            result = numbers[index]
    return result

numbers = [12,34,21,34,55,34,11]
result = findsmallerelement(numbers)
print("smallest number is:" , result)



output: smallest number is: 11


