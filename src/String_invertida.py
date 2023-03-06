# define a string a ser invertida
string = 'Este é um exemplo de string'

# inicializa a nova string vazia
nova_string = ''

# percorre a string original do último ao primeiro caractere
for i in range(len(string)-1, -1, -1):
    # adiciona o caractere na nova string
    nova_string += string[i]

# imprime a nova string invertida
print(nova_string)
