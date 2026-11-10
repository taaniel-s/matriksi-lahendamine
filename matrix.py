print("Siseta matriks")
a11 = float(input("a11: ").replace(",", "."))
a12 = float(input("a12: ").replace(",", "."))
v1 = float(input("Vabaliige v1: ").replace(",", "."))
a21 = float(input("a21: ").replace(",", "."))
a22 = float(input("a22: ").replace(",", "."))
v2 = float(input("Vabaliige v2: ").replace(",", "."))



def divide(a, b, c): # jagab rea
    for i in range(3):
        if a == 0:
            print("ei saa 0 jagada")
    
    return a / a, b / a, c / a  



def multiply(a, b, c, x, y, z): # korrutab rea
    

    return a - (a * x), b - (a * y), c - (a * z)    

        

def calculate(a11, a12, v1, a21, a22,  v2): # kalkuleerib
    if a11 == 0 and a21 != 0:
        a11, a12, v1, a21, a22, v2 = a21, a22, v2, a11, a12, v1 # vahetab read vajadusel (kui a11 on 0)

    if a11 != 0:
        a11, a12, v1 = divide(a11, a12, v1)
        a21, a22, v2 = multiply(a21, a22, v2, a11, a12, v1)
        a22, a21, v2 = divide(a22, a21, v2)
        a12, a11, v1 = multiply(a12, a11, v1, a22, a21, v2)

        print(f"[{a11}, {a12}, {v1}]")
        print(f"[{a21}, {a22}, {v2}]")

        print(f"x1 = {v1}")
        print(f"x2 = {v2}")

    else:
        print("Error: ei tea mis juhtus")

calculate(a11, a12, v1, a21, a22, v2)
