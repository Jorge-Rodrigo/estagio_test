 
# Sequências
sequencias = [
    [1, 3, 5, 7],     # a)
    [2, 4, 8, 16, 32, 64],  # b)
    [0, 1, 4, 9, 16, 25, 36],  # c)
    [4, 16, 36, 64],  # d)
    [1, 1, 2, 3, 5, 8],  # e)
    [2, 10, 12, 16, 17, 18, 19]  # f)
]

for i, sequencia in enumerate(sequencias):
    if i == 0:  # Sequência a)
        sequencia.append(sequencia[-1] + 2)
    elif i == 1:  # Sequência b)
        sequencia.append(sequencia[-1] * 2)
    elif i == 2:  # Sequência c)
        sequencia.append(sequencia[-1] + 13)
    elif i == 3:  # Sequência d)
        sequencia.append(sequencia[-1] + 64)
    elif i == 4:  # Sequência e)
        sequencia.append(sequencia[-1] + 5)
    elif i == 5:  # Sequência f)
        sequencia.append(sequencia[-1] + 1)


for i, sequencia in enumerate(sequencias, start=1):
    print(f"Sequência {chr(96+i)}:", sequencia)