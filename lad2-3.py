print("หาค่าBMI")
A = float(input("น้ำหนักตัวkg : "))
B = float(input("ส่วนสูงCm : " ))
C = A/(B/100 * B/100)
print("ค่า BMI %2f"%C)
if 18.50 > C :
     print("ไม่กินไรเลยหรือไง")
elif 18.50 <= C and 23.00 > C :
    print("สุภาพแจ๋มๆ")
elif 23.00 <= C and 24.90> C :
    print("โรคอ้วนระดับ 1 ")
elif 25.00 <= C and 29.90> C :
    print("โรคอ้วนระดับ 2 ")
else:
    print("โรคอ้วนระดับ 3  ลดบ้างน่ะไอ้อ้วน")