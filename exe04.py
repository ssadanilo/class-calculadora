# Crie uma classe Calculadora que tenha métodos para realizar operações matemáticas básicas (+ , - , *, / ).

class Calculadora():
    def somar(self, num1, num2):
        return num1 + num2
    
    def subtrair(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return 'Não divide por zero'
        
# Uso da class Calculadora
cal = Calculadora()

print('Soma:', cal.somar(10,5))
print('Subtração:', cal.subtrair(10,5))
print('Multiplicação:', cal.multiplicar(10,5))
print('Divisão:', cal.dividir(10,5))
print('Divisão por zero:', cal.dividir(10,0))

    
