def fibonacci(n):

    fib1, fib2 = 0, 1

   
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2

    
    if fib2 == n:
        return True
    else:
        return False


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci(numero):
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")