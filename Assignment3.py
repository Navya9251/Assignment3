#Write a Python function to sum all the numbers in a list.

list1 = [8, 2, 3, 0, 7]
total = sum(list1)
print("Sum of all elements in given list: ",total)

#Write a Python program to reverse a string.

def reverse(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    return " ".join(string)
s = "rama123"
print("The original string is : ", s)
print("The reversed sring(using reversed) is : ", reverse(s))

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

str="HiHowAreYou"
lower=0
upper=0
for i in str:
    if(i .islower()):
        lower += 1
    else:
        upper += 1
print("The number of lowercase characters is : ",lower)
print("The number of uppercase characters is : ",upper)