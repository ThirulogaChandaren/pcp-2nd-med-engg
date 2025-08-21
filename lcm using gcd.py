def gcd(x, y):
    cnt = 0
    while y:
        x, y = y, x % y
        cnt = cnt + 1
    return x
def lcm(a, b):
    product = a * b
    gcd_result = gcd(a, b)
    lcm_result = product // gcd_result 
    return lcm_result

num1 = 48
num2 = 18
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")

num1 = 564674
num2 = 184847
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")

num1 = 6
num2 = 8
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")

num1 = 1548008755920
num2 = 2503700422160
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")