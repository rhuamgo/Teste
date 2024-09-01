#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

palavra = input("Escreva um texto: ")
soma = 0;

for char in palavra:
    if 'a' in char or 'A' in char:
        soma +=1

print(f'A letra "a" aparece {soma}, vezes no texto informada.')
