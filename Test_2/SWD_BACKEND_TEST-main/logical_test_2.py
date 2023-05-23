
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

import random

def ArabicNumToRomanNum(num):
    
    if(num < 1 or num > 1000):
        return "Input must be 1 - 1000"
    
    thousands = num // 1000
    hundreds = num % 1000 // 100
    tens = num % 1000 % 100 // 10
    unit = num % 1000 % 100 % 10

    romanThousands = ""
    if(thousands == 1):
        romanThousands = "M"

    romanHundreds = ""
    if(hundreds == 9):
        romanHundreds = "CM"
    elif(hundreds < 9 and hundreds >= 5):
        romanHundreds = "D"
        for i in range(hundreds % 5):
            romanHundreds = romanHundreds + "C"
    elif(hundreds == 4):
        romanHundreds = "CD"
    elif(hundreds < 4):
        for i in range(hundreds):
            romanHundreds = romanHundreds + "C"


    romanTens = ""
    if(tens == 9):
        romanTens = "XC"
    elif(tens < 9 and tens >= 5):
        romanTens = "L"
        for i in range(tens % 5):
            romanTens = romanTens + "X"
    elif(tens == 4):
        romanTens = "XL"
    elif(tens < 4):
        for i in range(tens):
            romanTens = romanTens + "X"

    
    romanUnit = ""
    if(unit == 9):
        romanUnit = "IX"
    elif(unit < 9 and unit >= 5):
        romanUnit = "V"
        for i in range(unit % 5):
            romanUnit = romanUnit + "I"
    elif(unit == 4):
        romanUnit = "IV"
    elif(unit < 4):
        for i in range(unit):
            romanUnit = romanUnit + "I"

    romanNum = romanThousands+romanHundreds+romanTens+romanUnit
    return romanNum


randomNum = random.randrange(1,1000)
print("Input : {} \nOutput : {}".format(randomNum, ArabicNumToRomanNum(randomNum)))