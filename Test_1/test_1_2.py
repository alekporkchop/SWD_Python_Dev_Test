# โจทย์ที่ 1.2
# เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 
# โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข


def indexOfHighestValue(arr):
    highestValue = 0
    indexOfHighest = -1

    # using enumerate to access index of arr
    for i, val in enumerate(arr):
        if(val > highestValue):
            highestValue = val
            indexOfHighest = i
    return indexOfHighest

    # # using arr.index to get index of highest value
    # for val in arr:
    #     if(val > highestValue):
    #         highestValue = val
    # return arr.index(highestValue)



print(indexOfHighestValue([1,2,1,3,5,6,4]))