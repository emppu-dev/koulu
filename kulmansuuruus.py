import math # kirjasto jolla pystyy tekemään useita eri matemaattisia tarpeita

print("""
Määritä kolmion sivujen pituudet

  *
  **
  ***
A **** C
  *****
  ******
    B
""") # printtaa kolmion joka näyttää missä kolmion kirjaimet ovat

# kysymykset
A = float(input("A > "))
B = float(input("B > "))
C = float(input("C > "))
kulma = input("Kulma jonka haluat laskea\nKulma > ") # kysyy kulman jonka haluat laskea
 
# listat
x1 = {"A":B*B + A*A, "B":C*C + B*B, "C": A*A + C*C}
x2 = {"A":C*C, "B":A*A, "C":B*B}
x3 = {"A": 2*B*A, "B": 2*C*B, "C": 2*A*C}

# laskut
osa = (x1[kulma] - x2[kulma])/x3[kulma] # ottaa listoista oikeat laskut ja yhdistää niistä yhden laskun
vKulma = math.degrees(math.acos(osa)) # kääntää luvun kulmaksi
print(f"Kulma {kulma} = {vKulma} astetta") # tulostaa vastauksen
