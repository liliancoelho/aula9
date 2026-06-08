# Metodo 1 da questão
def Soma_par (a, b, c, d ,e ,f):
    soma1 = a + b
    soma2 = c + d
    soma3 = e + f
    print("A soma do primeiro par é: ", soma1)
    print("A soma do segundo par é: ", soma2)
    print("A soma do terceiro par é: ", soma3)

Soma_par(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")), 
         int(input("Digite o terceiro numero: ")), int(input("Digite o quarto numero: ")), 
         int(input("Digite o quinto numero: ")), int(input("Digite o sexto numero: ")))

#metodo 2 da questão

for i in range(3):
    resultado = Soma_par(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
    print("A soma dos dois numeros é: ", resultado)


for i in range(3):
    Num1 = int(input("Digite o primeiro numero: "))
    Num2 = int(input("Digite o segundo numero: "))
    print(F"A soma de {Num1} e {Num2} é: {Soma_par(Num1, Num2)}")