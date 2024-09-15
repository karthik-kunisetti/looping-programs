#!/usr/bin/env python
# coding: utf-8

# # 1.check the number is armstrong or not

# In[4]:


n = int(input("Enter the number: "))
s = n  # Store the original number
b = len(str(n)) # Find the number of digits in n
sum = 0

# Loop to calculate the sum of digits raised to the power of number of digits
while n != 0:
    r = n % 10  # Extract the last digit
    sum += r ** b  # Add the digit raised to the power of b to the sum
    n = n // 10  # Remove the last digit

# Compare the original number with the calculated sum
if s == sum:
    print(f"{s} is an Armstrong number")
else:
    print(f"{s} is not an Armstrong number")


# # 2.Revese a number using loop

# In[7]:


n=int(input("enter the number"))
rev=0
while(n>0):
    rem=n%10
    rev=rev * 10 + rem
    n=n//10
print(rev)


# In[ ]:


#use slicing to reverse the number


# In[5]:


num=62974
a=str(num)[::-1]
print(a)


# In[21]:


def reverse(n):
    rev=0
    while(n>0):
        rem=n%10       #get the last digit
        rev=rev*10+rem #print the result
        n=n//10        #remove the last digit
    print("After reversed the number is:",rev)   
n=int(input("enter your number"))
reverse(n)


# # 3.sum of digit of a number using loop

# In[31]:


# Function to calculate the sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit  # Add the digit to the total sum
        n = n // 10     # Remove the last digit
    return total

# Example usage
number = 12345
sum_digits = sum_of_digits(number)
print("Sum of Digits:", sum_digits)


# In[38]:


n=19863
sum=0
while(n>0):
    digit=n%10
    sum+=digit
    n=n//10
print(f"the sum of the number is",sum)


# # 4.check the number is palindrome using the loop

# In[52]:


n=656
original_num=n
print(f"{original_num} is the original number")
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(f"{rev} is the reversed number")
if(original_num==rev):
    print("palindrome ")
else:
    print("Not palindrome")
print("Hence Checked!")


# # 5.count the number of digits in an integer

# In[53]:


# Function to count the number of digits in a number
def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10  # Remove the last digit
        count += 1   # Increment the count
    return count

# Example usage
number = 12345
num_digits = count_digits(number)
print("Number of digits:", num_digits)


# In[54]:


# Function to count digits using string conversion
def count_digits(n):
    return len(str(n))

# Example usage
number = 12345
num_digits = count_digits(number)
print("Number of digits:", num_digits)


# # 6.sum of natural numbers using loop

# In[13]:


def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = 10  # Example input
print(sum_of_natural_numbers(n))


# In[ ]:


#6.sum of natural numbers using formula


# In[3]:


def sum_of_the_numbers(n):
    return n*(n+1)//2
n=10
sum_of_the_numbers(n)


# In[11]:


n=10
tot=0
for i in range(1, n+1):
    tot += i
print(tot)


# # 7.find LCD and GCD of two numbers using loop

# In[14]:


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 24
num2 = 36
gcd = find_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")


# In[15]:


def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

# Example usage:
num1 = 24
num2 = 36
lcm = find_lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {lcm}")


# # 8.print fabinocci series using loop

# In[20]:


num=10
n1,n2=0,1
print(n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")


# In[22]:


def fibonacci(n):
    fib_series = [0, 1]  # Starting elements of the Fibonacci series
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series[:n]

n = 10  # Number of terms in the series
print(fibonacci(n))


# # 9.calulate the power of number

# In[26]:


def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

# Example usage:
base = 2
exponent = 10
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")


# # 10.find factors of a number

# In[29]:


def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Example usage:
num = 54
print(f"Factors of {num} are: {find_factors(num)}")

