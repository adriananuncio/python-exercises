#!/usr/bin/env python
# coding: utf-8

# ### 1. Conditional Basics
# 
# #### a. Prompt the user for a day of the week, print out whether the day is Monday or not
# 
# #### b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 
# #### c. Create variables and make up values for
#     #### i. The number of hours worked in one week
#     #### ii. The hourly rate
#     #### iii. How much the week's paycheck will be
#     #### iv. Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours.

# In[18]:


# a. Prompt the user for a day of the week, 
## print out whether the day is Monday or not

day_of_the_week = input('What day of the week is today? ')


# In[20]:


if day_of_the_week == ('Monday' or 'monday'): 
    print('Yay it\'s Monday!') 
else: print('Boo it\'s not Monday!')

print(day_of_the_week)


# In[21]:


# b. Prompt the user for a day of the week, 
## print out whether the day is a weekday or a weekend

if day_of_the_week == ('Saturday' 
                       or 'saturday' 
                       or 'Sunday' 
                       or 'sunday'):
        print('It\'s the weekend!')
else: print('It\'s not the weekend!')
    
print(day_of_the_week)


# In[164]:


# c. Create variables and make up values for
### The number of hours worked in one week
### The hourly rate
### How much the week's paycheck will be
### Write the python code that calculates the weekly paycheck.
####You get paid time and a half if you work more than 40 hours.

hourly_pay = 50
over_time_pay = hourly_pay * 1.5

hours_worked_in_a_week = int(input(int))
standard_work_week_hours = 40
over_time_hours = hours_worked_in_a_week - standard_work_week_hours

regular_paycheck = standard_work_week_hours * hourly_pay
over_time_pay = over_time_hours * over_time_pay


# In[165]:


paycheck = (hourly_pay * hours_worked_in_a_week)

if hours_worked_in_a_week > standard_work_week_hours:
    over_time_paycheck = regular_paycheck + over_time_pay
    print(over_time_paycheck)
else:
    print(paycheck)


# ### Loop Basics
# 
# #### a. While
# ##### i. Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration, output the current value of i, then increment i by one.

# In[5]:


i = 5

while i <= 15:
    print(i)
    i += 1


# ##### ii. Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[7]:


n = 0
while n <= 100:
    print(n)
    n += 2


# In[9]:


# ii Alter your loop to count backwards by 5's from 100 to -10

n = 100
while n <= 100 and n >= -10:
    print(n)
    n -= 5


# In[21]:


# iii Create a while loop that starts at 2, and 
## displays the number squared on each line while 
### the number is less than 1,000,000

x = 2
while x < 1000000:
    print(x)
    x *= x


# In[20]:


# iv

p = 100
while p >= 5:
    print(p)
    p -= 5


# #### For Loops

# In[22]:


# i.
pick_a_number = input('Input a number.')

for number in range(1,11):
    print(f'{pick_a_number} x {number} = {int(pick_a_number) * number}')


# In[1]:


# ii.
### Need help understanding

for x in range(1,10):
    print(x * str(x))


# #### break and continue

# In[9]:


#i. Write a program that prompts the user for a 
## positive integer. Next write a loop that prints 
### out the numbers from the number the user entered 
#### down to 1.

user_numb = input('Enter a positive number: ')


# In[10]:


user_numb = int(user_numb)
for x in range (user_numb,0,-1):
    print(x)


# In[ ]:


# ii. The input function can be used to prompt for input
## and use that input in your python code. Prompt the user 
## to enter a positive number and write a loop that counts 
## from 0 to that number. (Hints: note that the input 
## function returns a string, so you'll need to convert this
## to a numeric type.)


# In[12]:


user_numb = input('Enter a positive number: ')

for x in range (int(user_numb)+1):
    print(x)


# In[18]:


# ii.

user_numb = input('Enter an odd number between 1 and 50: ')

if user_numb.isdigit() == True:
    print('this is a digit')
    if int(user_numb) % 2 == 1:
        print('this is odd')
        if (int(user_numb) > 1) and (int(user_numb) < 50):
            print('this is in range')
                
user_numb = int(user_numb)

for x in range(1,50):
    if x == user_numb:
        continue
    if x % 2 == 1:
        print(x)


# ### Fizzbuzz

# In[19]:


# Write a program that prints the numbers from 1 to 100.

for x in range (1,101):
    print(x)


# In[31]:


for x in range (1,101):
    if x % 3 == 0:
        print('Fizz')
        continue
    if x % 5 == 0:
        print('Buzz')
        continue
    if x % 15 == 0:
        print('FizzBuzz')
        continue
    print(x)


# ### Display a table of powers

# In[34]:


user_numb = input('Enter a number: ')


# In[35]:


user_numb = int(user_numb)


# In[36]:


user_numb, user_numb**2, user_numb**3


# In[38]:


for x in range(1,user_numb+1):
    print(f'{x}    |{x**2}    |{x**3}    ')


# In[ ]:


while True:
    user_numb = input('Enter a number: ')
    user_numb = int(user_numb)
        
    for x in range(1,user_numb+1):
        print(f' {x}    |{x**2}    |{x**3}    ')
            
    user_yn = input('Would you like to continue? (y/n) ')
    if user_yn.lower() != 'y':
        break


# In[ ]:




