import random
print('-' * 65)
print('{:^60}'.format('JOGO DA ADIVINHAÇÃO V2.0'))
print('-' * 65)
print('Escolha o nível de dificuldade: \n'
      '[ 1 ] FÁCIL \n'
      '[ 2 ] MÉDIO \n'
      '[ 3 ] DIFÍCIL ')
escolha_nivel = int(input('Escolha seu nível: '))
computador = random.randint(1, 10)
tentativas = 0
print('Eu já pensei em um número, agora é sua vez, adivinhe qual número eu pensei de 1 a 10. ')
usuario = int(input('Entre com um número inteiro: '))
while usuario != computador:
    if usuario < computador:
        print('Mais... Você errou. Tente novamente.')
    elif usuario > computador:
        print('Menos.. Você errou. Tente novamente.')
    usuario = int(input('Entre com um número inteiro: '))
    tentativas += 1
print(f'Parabéns, você ganhou, eu pensei no número {computador}.')
print(f'Suas tentativas foram de {tentativas} vezes.')
