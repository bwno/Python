from operator import truediv
# cria a classe calculadora
class Calculadora:
    # cria o metodo de soma
    def soma(self, numero1, numero2):
        resultado = numero1 + numero2
        return resultado
    
    # cria o metodo de subtracao
    def subtracao(self, numero1, numero2):
        resultado = numero1 - numero2
        return resultado
# cria a funcao de validacao
def recebe_numero():
    while True:
        numero = input("Numero um numero: ")
        # funcao de comparacao
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print("Digite apenas numeros inteiros")

    return numero

soma = Calculadora().soma(recebe_numero(),recebe_numero())
subtracao = Calculadora().subtracao(recebe_numero(),recebe_numero())

print(f"O resultado da soma é {soma} e o resoltado da subtracao é {subtracao}")

