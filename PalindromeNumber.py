def is_palindrome(str):
    end = len(str(str)) - 1
    start = 0
    while start < end:
        if str(str)[start] != str(str)[end]:
            return False
        start += 1
        end -= 1
    return True
    

def palindrome(number):
    reverse = 0
    temp = number
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    return reverse == number

def is_palindrome(number):
    return str(number) == str(number)[::-1]

print(palindrome(123321))