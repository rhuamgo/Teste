# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


# resumo quer que eu veja se o numero informado pertence a sequencia fibonacci

valor =int(input("Informe o valor que deseja verifciar: "));
iniciador = 1;
verificador = 0;
resultado = 1;
finalizador = 0;
i = 0;
while i <= valor:
    print(f'{verificador} + {iniciador} = {verificador+iniciador}')
    resultado = verificador + iniciador
    verificador = iniciador
    iniciador = resultado

    
    i +=1
    if(iniciador == valor):
       print(f"o numero: {valor} faz parte da sequencia fibonacci")
       finalizador = 1
       break

if finalizador == 0:
    print(f"O Numero: {valor}, nao faz parte da iniciador");