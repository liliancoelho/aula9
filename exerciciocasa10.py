def forma_triangulo(a, b, c): 
   if a < b + c and b < a + c and c < a + b: 
       return True 
   else: 
       return False 
 
# Testando a função 
print(f"Lados (3, 4, 5) formam triângulo? {forma_triangulo(3, 4, 5)}")  # True 
print(f"Lados (1, 1, 3) formam triângulo? {forma_triangulo(1, 1, 3)}")  # False 
print(f"Lados (5, 5, 5) formam triângulo? {forma_triangulo(5, 5, 5)}")  # True
