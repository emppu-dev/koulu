print("""
  *
  **
  ***
B **** A
  *****
  ******
    C
""")
a = float(input("B sivun pituus > "))
b = float(input("C sivun pituus > "))
print(f"{a}^2 + {b}^2 = x^2\nx^2 = {a**2} + {b**2}\nx^2 = {a**2+b**2} || √\nx = (+-) √{a**2+b**2}\nx = {round((a**2 + b**2)**0.5)}")
