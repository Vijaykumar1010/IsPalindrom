# find given string is palindrom or not

def isPalindrom(string: str)-> bool:

# we are assume left index  is zero and we also increment left index 

    left_index = 0

# total countin of string and subsrtating right index backwards and it is descement right index

    right_index = len(string) - 1

    result = True  # falg assuming the reslut is coorect or true

    while (left_index < right_index):

# we are left_index is not equal to right index (lift_index is going througth ------> and rigt_index come from <------, once both met break the loop)

        if string[left_index] != string[right_index]:


         result = False

        left_index += 1 # increment 

        right_index -=1 # decrement

    return result

# invocation code

input1 = 'mam'

input2 = 'hello'

result = isPalindrom(input1)

result1 = isPalindrom(input2)

if result:
    print("string is palindrom")
else:
    print("string is not palindrom")


if result1:
    print("string is palindrom")
else:
    print("string is not palindrom")

