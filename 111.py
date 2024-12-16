from fractions import Fraction 
import numpy as np 
class Polynomial:

    # определение класса
    def __init__(self, coefficients):
        self.coefficients = [Fraction(c) for c in coefficients]
# Метод __init__ инициализирует объект класса.
    
    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                i if power == 0: 
                    terms.append(f"{coef}") 
                elif power == 1: 
                    terms.append(f"{coef}x") 
                else: 
                    terms.append(f"{coef}x^{power}") 
        return " + ".join(terms)
#Метод __str__ позволяет представить многочлен в виде строки. 
#список terms, содержит строковые представления каждого члена #многочлена, создаем строку для каждого члена многочлена в зависимости #от его степени. 
    # Сложение многочленов
    # self - первое слагаемое
    # second - второе
    def __add__(self, second):
        max_len = max(len(self.coefficients),  
for i in range(len(self.coefficients)): 
            new_coefficients[max_len - len(self.coefficients) + i] += self.coefficients[i] 
         
        for i in range(len(second.coefficients)): 
            new_coefficients[max_len - len(second.coefficients) + i] += second.coefficients[i]         
return Polynomial(new_coeffs)

    # Поиск значения в точке x
    def value(self, x):
        result = 0
        for coef in self.coefficients: 
            result = result * x + coef 
        return result 
    # Поиск производной
     def derivative(self): 
        new_coefficients = [] 
        for i in range(len(self.coefficients) - 1): 
            new_coefficients.append(self.coefficients[i] * (len(self.coefficients) - i - 1)) 
        return Polynomial(new_coefficients) 
    # Поиск целых корней многочлена
  def gcd(poly1, poly2): 
    while len(poly2.coefficients) > 1 or poly2.coefficients[0] != 0: 
        remainder = Polynomial(np.polynomial.polynomial.polydiv(poly1.coefficients, poly2.coefficients)[1]) 
        poly1, poly2 = poly2, remainder 
    return poly1 
        return f"целые корни полинома: {roots}"