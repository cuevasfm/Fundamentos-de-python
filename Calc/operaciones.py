def resta(*nums:float)->float:
    resultado = nums[0]
    for num in nums:
        resultado -= num
    return resultado

def suma(*nums:float)->float:
    resultado = 0
    for num in nums:
        resultado += num
    return resultado

def multiplicacion(*nums:float)->float:
    resultado = 1
    for num in nums:
        resultado *= num
    return resultado

def division(num1:float, num2:float)->float:
    resultado = num1 / num2
    sobra = num1 % num2
    return resultado, sobra