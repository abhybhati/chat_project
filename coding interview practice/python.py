# reverse string through slicing
# s = "python"
# rev = s[::-1]
# print(rev)


# rev without slicing
# rev =""
# s = "python"
# for char in s:
#     rev = char + rev
# print(rev)


# prime number 
# def is_prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if (n%i)==0:
#             return False
#     return True
# print(is_prime(8))



# no. of prime numbers

# def prime_generator(n):
#     for num in range(2,n+1):

#         for i in range(2, int(num**0.5)+1):
            
#             if num % i == 0:
#                 break
#         else:
#             yield num
# prime = prime_generator(20)
# for num in prime:
#     print(num)



#factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# n = int(input("Enter a number: "))
# print("Factorial of", n, "is:", factorial(n))


# factorial without recursion 
# def fact(n):
#     f = 1
#     for i in range(1 , n+1):
        
#         f = i*f
#     return f
# print(fact(7))



# factorial of n number

# def fact(n):
#     fact = 1
#     for num in range(1,n+1):
        
#         for i in range(num,num+1):
#             fact *= i

#             print(f"factorial of {num} is ",fact)
# fact(10)


# given str is polindrom or not 
# def polindrom(s):
#     return s == s[::-1]

# print(polindrom("python"))
# print(polindrom("madam"))


# polindrom a sentance 
# def polindrom(s):
#     print(s)
#     m = " ".join(s).split()
#     print(m)
#     if m == m[::-1]:
#         print("is polindrom")
# polindrom("hay madam yah")




# minimum no in list
# l1 = [10,10,5,4,6,8,1,0]
# min = l1[0]
# for i in range(len(l1)):
#     if min>l1[i]:
#         min = l1[i]
# print(min)


# maximum no from list
# l1 = [10,30,12,23,67,90]
# max = l1[0]
# for i in range(len(l1)):
#     if max<l1[i]:
#         max = l1[i]
# print(max)


# frequency
# n = "a"
# f = ["a", "b", "a", "c", "b", "a"]
# count = 0
# for i in f:
#     if n == i:
#         count +=1
# print(count)


# frequency of each charcter in list 
# f = ["a", "b", "a", "c", "b", "a"]
# for i in set(f):
#     count=0
#     for n in f:
#         if i == n:
#             count+=1
#     print(f"{i}:{count}")
        
    


# fibonaci series
# n = 5
# a = 0
# b = 1
# print(a,b,end=" ")
# for i in range(n):
#     fib = a+b
#     a = b
#     b = fib
#     print(fib,end=" ")
    
# remove duplicate elements from list
# def remove_dupicates(l):
#     return list(set(l))

# print(remove_dupicates([1, 2, 2, 3, 4, 4, 5]))


# remove duplicates from list without using set
# def unique(lst):
#     l2 =[]
#     for num in lst:
#         if num not in l2:
#             l2.append(num)
        
#     return l2

# lst = [1, 2, 2, 3, 4, 4, 5]
# print(unique(lst))




# # find missing number from the sequence 
# lst = [1,2,3,4,7,8,9]

# for i in range(1,10):
#     if i not in lst:
#         print(f"{i} is missing")


# second larget 
# def second_largest(nums):
#     n = list(set(nums))
#     n.sort()
#     return n[-2]

# print(second_largest([10, 20, 4, 45, 99]))


# find second largest without set 
# ls = [10, 20, 4, 45, 99]
# large = max(ls)
# ls.remove(large)
# print(max(ls))

# ## Anagrams 
# def is_anagrams(str1,str2):
#     return sorted(str1) == sorted(str2)
# print(is_anagrams("silent","listen"))


# Armstrong = An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the total number of digits(153 , (1^{3}+5^{3}+3^{3}=1+125+27=153))
# n = 153
# power = len(str(n))
# num =0
# temp = n
# while(temp>0):
#     digit = temp%10
#     num += digit**power
#     temp //= 10
# if num == n:
#     print(f"{num} is armstrong number")
# else:
#     print("not armstrong")


# Reverse Words in a String
# s = "i love python"
# word= s.split()
# rev=word[::-1]
# print(" ".join(rev))



# Count Frequency of Each Character
# name = "apple"
# freq = {}
# for n in name:
#     if n in freq:
#         freq[n]+=1
#     else:
#         freq[n] = 1
# print(freq)


 
        
