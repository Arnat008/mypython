#หาพื้นที่วงกลม 22/7*(r**2)
def circle(r):
    f = r**2
    area = (22/7)*f
    return area

    print("พื้นที่วงกลม %.2f" % circle(9))