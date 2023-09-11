#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1 
# Write a program that returns the number and whether it is a power of 3 or not. 
number = int(input("Enter a number: "))
case = False

if number > 0:
    while number % 3 == 0:
        number //= 3
        case = True

if case:
    print("it is a power of 3")
else:
    print("it is not a power of 3")
    
#*******************************************************************
# Question 2
# Write a program that checks whether the given number is a perfect square or not. Return the answer as True or False. For example, it will return True if 4 or 16 or 100 is given, and False if 5 is given


number = int(input("Enter a number: "))
root = round(number**(1/2))
if number==(root**2):    
    print("number is square")
else : print("not")
    
    
#*******************************************************************

# Question 3
# Write a program that calculates the tax based on the price of the product. 
# A 10% tax is levied on products whose price is below AZN 500. 
# Products with a price of 500-1000 AZN will be taxed at 15%. Above 1000 AZN, there will be an 18% tax. 
# If a negative value is entered, have the program return "ERROR. MUST BE A POSITIVE VALUE". 
# Please return the new price with tax.

price = int(input("Enter a number: "))
if price<0:
    print ("ERROR. MUST BE A POSITIVE VALUE")
elif price<500:
    print ("tax calculated 10% ,price with tax is: ", price + price*.1, " AZN")
elif price<1000:
    print ("tax calculated 15% ,price with tax is: ", price + price*.15, " AZN")
else:
    print ("tax calculated 18% ,price with tax is: ", price + price*.18, " AZN")
    
#*******************************************************************
# Question 4
# Write a program that takes 3 numbers and shows which one is bigger and by how much. 
# Also add a case when 3 numbers are equal.
list = []
for i in range(5):
    number = int(input("enter number :"))
    list.append(number)
list.sort()
diff = (list[-1])-(list[-2])
print("big number is :" , list[-1])  
print("difference is :", diff)

#*******************************************************************

# Question 5
# Write the program so that it says "Even" if the input is even, and "Odd" if it is odd.

number = int(input("enter only number : "))
if number%2==0:
    print("number is even")
else: print("number is odd")


#*******************************************************************

# Question 6
# Write a program that takes a person's age and tells if they are old enough to vote. 
# If the person is very young (under 18), indicate how many years they will be able to vote.

age = int(input("enter your age : "))
vote_age=18
if age>=18:
    print("You can vote")
else:
    vote_age-=age    
    print("You can't vote")
    print(f'you will vote after {vote_age} years')

#*******************************************************************

# Question 7
# Write a program that checks whether the sum of the first and last numbers in a list is greater than, 
# less than, or equal to the sum of all other numbers.

list1 = [12,5,7,6,4,10]
#print(list[1:-1])
#print(list[0],list[-1])
#print(list2)
#print(list3)    
list3=list1[1:-1]
list2=[]
list2.append(list1[0])
list2.append(list1[-1])

sum1 = 0;
sum2 = 0;
for i in list2:
    sum1+=i
print(sum1)
for j in list3:
    sum2+=j
print(sum2)
if sum1>sum2:
    print("sum of first and last items of list is greater than others.")
elif sum1<sum2:
    print("sum of first and last items of list is smaller than others.")
else: print("sum of firts and last otems of list is equal with others.")

















