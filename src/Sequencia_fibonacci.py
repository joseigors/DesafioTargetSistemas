number = 13 # número a ser verificado na sequência de Fibonacci
sequence = [0, 1] # lista com os dois primeiros números da sequência

while sequence[-1] < number: # enquanto o último número da lista for menor que o número fornecido
    next_number = sequence[-1] + sequence[-2] # calcula o próximo número da sequência
    sequence.append(next_number) # adiciona o próximo número à lista

if number in sequence:
    print(number, "pertence à sequência de Fibonacci!")
else:
    print(number, "não pertence à sequência de Fibonacci!")
