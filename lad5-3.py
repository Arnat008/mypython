def p(c):
    F = ((9/5)*c)+32
    return F

def o(c):
    K = c + 273.15
    return K

c = float(input("ใส่องศาC : "))
print("อุณหภูมิ %.2f" % p(c))
print("อุณหภูมิ %.2f" % o(c))