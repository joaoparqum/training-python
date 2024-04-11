def calcular(operacao):
    
    def soma(a,b):
        return a + b
    
    def subtrai(a,b):
        return a - b
    
    def mult(a,b):
        return a * b
    
    def div(a,b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtrai
        case "*":
            return mult
        case "/":
            return div

print(calcular("-")(20,10))
print(calcular("+")(20,10))
