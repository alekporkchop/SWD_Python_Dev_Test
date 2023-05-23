# เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial 
# เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

def factorial(n):
    i = n
    ans = 1
    while i > 0:
        ans = ans * i
        i -= 1
    return ans

def countNumOfZero(n):
    string = str(n)
    i = len(string) - 1
    numOfZero = 0
    while i >= 0:
        if(string[i] == '0'):
            numOfZero += 1
        else:
            break
        i -= 1
    return numOfZero

print(countNumOfZero(factorial(10)))