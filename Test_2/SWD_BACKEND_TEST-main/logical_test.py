
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

import random

thaiDict = {
    "0": "ศูนย์",
    "1": "หนึ่ง",
    "2": "สอง",
    "3": "สาม",
    "4": "สี่",
    "5": "ห้า",
    "6": "หก",
    "7": "เจ็ด",
    "8": "แปด",
    "9": "เก้า",
    "10": "สิบ",
}


def NumberToThai(num):

    if(num < 0 or num > 10**7):
        return "Input must be 0 - 10^7"
    
    millions = num // 10**6
    hundredThousands = num % 10**6 // 10**5
    tenThousands = num % 10**6 % 10**5 // 10**4
    thousands = num % 10**6 % 10**5 % 10**4 // 10**3
    hundreds = num % 10**6 % 10**5 % 10**4 % 10**3 // 100
    tens = num % 10**6 % 10**5 % 10**4 % 10**3 % 100 // 10
    unit = num % 10**6 % 10**5 % 10**4 % 10**3 % 100 % 10

    #tt stands for thai text

    tt_millions = ""
    if(millions > 0):
        tt_millions = thaiDict[str(millions)]+"ล้าน"

    tt_hundredThousands = ""
    if(hundredThousands > 0):
        tt_hundredThousands = thaiDict[str(hundredThousands)]+"แสน"

    tt_tenThousands = ""
    if(tenThousands > 0):
        tt_tenThousands = thaiDict[str(tenThousands)]+"หมื่น"

    tt_thousands = ""
    if(thousands > 0):
        tt_thousands = thaiDict[str(thousands)]+"พัน"

    tt_hundreds = ""
    if(hundreds > 0):
        tt_hundreds = thaiDict[str(hundreds)]+"ร้อย"

    tt_tens = ""
    if(tens > 2):
        tt_tens = thaiDict[str(tens)]+"สิบ"
    elif(tens == 2):
        tt_tens = "ยี่สิบ"
    elif(tens == 1):
        tt_tens = "สิบ"

    tt_unit = ""
    if(num == 0):
        tt_unit = thaiDict[str(num)]
    elif(num > 10 and unit == 1):
        tt_unit = "เอ็ด"
    elif(unit > 0):
        tt_unit = thaiDict[str(unit)]
    
    thaiText = tt_millions+tt_hundredThousands+tt_tenThousands+tt_thousands+tt_hundreds+tt_tens+tt_unit
    return thaiText


print(NumberToThai(8*10**7))
randomNum = random.randrange(1,10**7)
print("Input : {} \nOutput : {}".format(randomNum, NumberToThai(randomNum)))